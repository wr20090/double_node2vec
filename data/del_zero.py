import numpy as np
from numpy import sort

l = []
zeros=[]
lines=[]
for line in open('/Users/ragami/Documents/node2vec/data/net7.txt', 'r'):
    l.append(list(line.strip('\n').split(' ')))
for i in range(len(l)):
    if l[i][2]!= '0':
        zeros.append(i)
for i in zeros:
    lines.append(l[i])
with open('/Users/ragami/Documents/node2vec/data/net7.txt', 'w') as f:
    for i in lines:
        for j in i:
            f.write(j)
            f.write(' ')
        f.write('\n')
    f.close()

