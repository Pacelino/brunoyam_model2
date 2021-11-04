import time
from threading import Thread
name = ['Biba', "Boba", 'Alice']


def get_thread(thread_name):
  time.sleep(1)
  print(f'Thread started is name: {thread_name._name}')


thread = Thread(target=get_thread, args= (1,))
thread2 = Thread(target=get_thread, args=thread)
thread3 = Thread(target=get_thread)

thread3.start()
thread2.start()
thread.start()

thread3.join()
thread2.join()
thread.join()


get_thread(thread3)