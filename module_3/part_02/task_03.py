d = {'name1': 'id', 'name2': 'id', 'name3': 'id'}
revers = dict()

for key, values in d.items():
    if revers.get(values):
        list = []
        if type(revers[values]) == list:
            list.extend(revers[values])
            list.append(key)
        else:
            list.append(revers[values])
            list.append(key)

        revers[values] = list
