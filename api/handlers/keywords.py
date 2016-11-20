import logging

import tornado.gen
import tornado.web
import elasticsearch

from settings import LIVE_INDEX, DOC_TYPE

class KeywordsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		# todo: edit to accept host for production
		es = elasticsearch.Elasticsearch()
		
		try: 
			response = es.search(index=LIVE_INDEX, doc_type=DOC_TYPE, filter_path=['hits.hits._source.keyword'])
		except TransportError as e:
			raise tornado.web.HTTPError(e.status_code, errors=e.info)
		
		results = [obj['_source']['keyword'] for obj in response['hits']['hits']]

		self.set_status(200)
		self.set_header('Content-Type', 'application/json')
		self.finish({'response': results})