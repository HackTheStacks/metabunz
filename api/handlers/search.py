import logging

import tornado.gen
import tornado.web
import elasticsearch


LIVE_INDEX = 'metasearch'
DOC_TYPE = 'entity'

class SearchHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		# todo: edit to accept host for production
		es = elasticsearch.Elasticsearch()
		query = self.get_argument('q')
		
		try: 
			response = es.search(q=query, index=LIVE_INDEX, doc_type=DOC_TYPE)
		except TransportError as e:
			raise tornado.web.HTTPError(e.status_code, errors=e.info)
		
		results = [obj['_source'] for obj in response['hits']['hits']]

		self.set_status(200)
		self.set_header('Content-Type', 'application/json')
		self.finish({'response': results})