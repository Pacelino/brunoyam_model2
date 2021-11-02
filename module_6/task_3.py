import time
from threading import Thread
name = ['Biba', "Boba", 'Alice']


def get_thread(thread_name):
  time.sleep(1)

  print(f'Thread started is name: {thread_name}')


thread = [Thread(target=get_thread, args=i) for i in name ]
get_thread(thread)
