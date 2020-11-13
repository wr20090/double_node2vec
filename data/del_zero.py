import numpy as np
from numpy import sort
path='/Users/ragami/Documents/node2vec/data/'
net='net'
txt='.txt'
for i in range(8):

    l = []
    zeros=[]
    lines=[]

    if i>0:
        adress=str(path+net+str(i)+txt)
        print adress
        for line in open(adress, 'r'):
            l.append(list(line.strip('\n').split(' ')))
        for i in range(len(l)):
            if l[i][2]!= '0':
                zeros.append(i)
        for i in zeros:
            lines.append(l[i])
        with open(adress, 'w') as f:
            for i in lines:
                for j in i:
                    f.write(j)
                    f.write(' ')
                f.write('\n')
            f.close()
        del adress

