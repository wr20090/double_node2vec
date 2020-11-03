import numpy as np

lines = []
for line in open('data/9606.txt', 'r'):
    lines.append(list(line.strip('\n').split(' ')))

for i in range(len(lines)):
    for h in [8, 7, 6, 5, 4, 3, 2]:
        del lines[i][h]
    lines[i][0] = lines[i][0][-7:-1]
    lines[i][1] = lines[i][1][-7:-1]
    for j in range(2):
        lines[i][j] = int(lines[i][j])
        lines[i][j] = str(lines[i][j])

with open('data/net_final.txt', 'w') as f:
    for i in lines:
        for j in i:
            f.write(j)
            f.write(' ')
        f.write('\n')
    f.close()
