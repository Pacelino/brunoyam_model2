import json


class Model:
    title = '1'
    text = '2'
    author = '3'

    def save(self):
        d = {}
        list_attr = list(filter(lambda x: not x.startswith('_'), dir(Model)))
        list_attr.remove('save')
        for i in list_attr:
            d[i] = eval('self.' + i)

        with open('task1.json', 'w') as f:
            json.dump(d, f)
        return print(d)


test = Model()
test.title = '11'
test.text = '22'
test.author = '33'
test.save()
