import time
from threading import Thread
name = ['Biba', "Boba", 'Alice']


def get_thread(thread_name):
  time.sleep(1)
  print(f'Thread started is name: {thread_name._name}\n')

test = Thread()
thread1 = Thread(target=get_thread, args=(test,))
thread2 = Thread(target=get_thread, args=(thread1,))
thread3 = Thread(target=get_thread, args=(thread2,))
thread4 = Thread(target=get_thread, args=(thread3,))
thread5 = Thread(target=get_thread, args=(thread4,))

more_thread = [thread1, thread2, thread3, thread4, thread5]

for t in more_thread:
  t.start()
for t in more_thread:
  t.join()
