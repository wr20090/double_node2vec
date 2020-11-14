import pandas as pd

vertex = []
for line in open('/Users/ragami/Documents/node2vec/data/vertex_class.txt', 'r'):
    vertex.append(list(line.strip('\n').split(' ')))
vc = []
for i in range(len(vertex)):
    vertex[i][0] = vertex[i][0][:-1]
    vc.append(['0', '0'])
    vc[i][0] = vertex[i][0][0:15]
    vc[i][1] = vertex[i][0][16:]

w = '/Users/ragami/Documents/node2vec/emb/w'
emb = '.emb'
s = '/Users/ragami/Documents/node2vec/csv/'
csv = '.csv'


for a in range(50, 550, 50):

    lines = []
    weight = w + str(a) + emb
    for line in open(weight, 'r'):
        lines.append(list(line.strip('\n').split(' ')))
    del lines[0]

    for i in range(len(lines)):

        zeronum = 15 - len(lines[i][0]) - 4
        lines[i][0] = 'ENSP' + zeronum * '0' + lines[i][0]
        for j in range(len(vc)):
            if lines[i][0] == vc[j][0]:
                lines[i].insert(0, vc[j][1])



# a=[['1','ES12','-0.12'],['2','aaa2','-4.12']]
# s=['a',2,3]

    name = range(1, a+1)
    for i in range(0, a):
        name[i] = 'd' + str(name[i])
    name.insert(0, 'name')
    name.insert(0, 'category')

    saver=s+str(a)+csv
    test = pd.DataFrame(columns=name, data=lines)
    test.to_csv(saver, index=False)
    del test
    print str(a) + 'done'
# print vertex[0]
# print vertex[0][0][:15]
# s=vertex[0][0][16:]
# print len(s)
# print s[-1]=='\r'
# print vertex[1][0]
