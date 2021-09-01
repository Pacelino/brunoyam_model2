import json

data_acc = dict()

def register(login, password):
    with open('data_acc.json', 'r') as f:
       data_acc = json.load(f)
       if login in data_acc.keys():
           print('Логин занят')
       if login not in data_acc.keys():
           data_acc[login] = password
           with open('data_acc.json', 'w') as f:
               json.dump(data_acc, f)
       else:
           print('already exist')





register(input('Введите свой логин для регистрации'), input('введите свой пароль'))