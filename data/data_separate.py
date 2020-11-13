import numpy as np

lines = []
for line in open('/Users/ragami/Documents/node2vec/data/9606.protein.links.detailed.v9.1.txt', 'r'):
    lines.append(list(line.strip('\n').split(' ')))
print lines[0][0]
for i in range(len(lines)):
    for h in [8, 7, 6, 5, 4, 3, 2]:
        del lines[i][h]
    lines[i][0] = lines[i][0][-7:]
    lines[i][1] = lines[i][1][-7:]
    for j in range(2):
        lines[i][j] = int(lines[i][j])
        lines[i][j] = str(lines[i][j])
print "net final "
with open('/Users/ragami/Documents/node2vec/data/netfinal.txt', 'w') as f:
    for i in lines:
        for j in i:
            f.write(j)
            f.write(' ')
        f.write('\n')
    f.close()
print " write "





