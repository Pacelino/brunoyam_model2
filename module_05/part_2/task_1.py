import json

class Model:
    title = '1'
    text = '2'
    author = '3'

    def save(self):
        d = {}
        arg = list(filter(lambda x: not x.startswith('_'), dir(Model)))

        title = Model.title
        text = Model.text
        author = Model.author
        d[arg[0]] = author
        d[arg[1]] = text
        d[arg[2]] = title
        with open('task1.json', 'w') as f:
            json.dump(d, f)
        return print(d)


test = Model()
test.save()


