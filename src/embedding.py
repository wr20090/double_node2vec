import argparse
import numpy as np
import networkx as nx
import node2vec
from gensim.models import Word2Vec

path_front = '/Users/ragami/Documents/node2vec/emb/w'
path_behind = '.emb'
walk_path = '/Users/ragami/Documents/node2vec/data/walk.txt'
l = []
for line in open(walk_path, 'r'):
    l.append(list(line.strip('\n').split(' ')))
for i in range(len(l)):
    del l[i][80]




def learn_embeddings(walks, dimensions, output):
    '''
	Learn embeddings by optimizing the Skipgram objective using SGD.
	'''

    walks = [map(str, walk) for walk in walks]
    model = Word2Vec(walks, size=dimensions, window=10, min_count=0, sg=1, workers=8,
                     iter=1)
    model.wv.save_word2vec_format(output)

    return


for i in range(75, 525, 25):
    path = path_front + str(i) + path_behind
    learn_embeddings(l,i,path)
# learn_embeddings(l,50,'/Users/ragami/Documents/node2vec/emb/test.emb')

