import networkx as nx
import itertools

""" SAMPLE TOY DATA """
# (keyword_id, user_id)
keywords = [1,1,1,1,1,
            2,2,2,
            3,3,3,3,
            4,4,4,4,4,4,
            5,5,5,
            6,7,8,
            9,9,9,
            10,10]

users = ['a', 'b', 'c', 'd', 'e', 
         'f', 'b', 'e',
         'a', 'b', 'c', 'd',
         'f', 'g', 'h', 'a', 'b', 'c',
         'h', 'i', 'j',
         'j', 'l', 'm',
         'l', 'a', 'b',
          'g', 'h']
raw = zip(keywords, users)


""" ACTUAL FUNCTIONS """

def neighborhood(g, node, n):
    path_lengths = nx.single_source_dijkstra_path_length(g, node)
    return [node for node, length in path_lengths.iteritems()
                    if length == n]

def get_best_rec(g, keyword):
    knodes = list(itertools.product([keyword], neighborhood(g, keyword, 2)))
    scores = [r for r in nx.jaccard_coefficient(g, knodes)]
    sorted_scores = sorted(scores, key=lambda x: -x[2])
    return sorted_scores[0][1]


""" EXAMPLE USAGE """

get_best_rec(g, 1)