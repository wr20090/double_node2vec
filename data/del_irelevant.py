lines = []
for line in open('/Users/ragami/Documents/node2vec/data/vertex_class.txt', 'r'):
    lines.append(list(line.strip('\n').split(' ')))
data = []
for i in range(len(lines)):
    data.append(1)
    data[i] = int(lines[i][0][4:15])
# print type(data[0])
# print 2 in data
l = []
res=[]
resul=[]
for line in open('/Users/ragami/Documents/node2vec/data/net7.txt', 'r'):
    l.append(list(line.strip('\n').split(' ')))
for i in range(len(l)):
    if int(l[i][0]) in data and int(l[i][1]) in data:
        res.append(i)
for i in res:
    resul.append(l[i])
with open('/Users/ragami/Documents/node2vec/data/net7.txt', 'w') as f:

    for i in resul:
        for j in i:
            f.write(j)
            f.write(' ')
        f.write('\n')
    f.close()