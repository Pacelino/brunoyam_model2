d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
res = dict()
x = ''
y = ''
for i in d:
    for j in d.values():
        res[j] = i
print(res)
