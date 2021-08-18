import json

data_acc = dict()
'''with open('data_acc.json', 'w') as f:
    json.dump(data_acc, f)'''


def register(login, password):
    with open('data_acc.json', 'r') as f:
       data_acc = json.load(f)
       if login not in data_acc.keys():
           data_acc[login] = password
           with open('data_acc.json', 'w') as f:
               json.dump(data_acc, f)
       else:
           print('already exist')
    return print(data_acc)


register(input("login"), input('password'))
