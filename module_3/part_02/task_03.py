d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
res = dict()
x = []

for i in d.keys():
    x.append(i)
for j in d.values():

    res[j] = x
print(res, x)
