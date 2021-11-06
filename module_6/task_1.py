import time
from threading import Thread


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
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
for t in more_thread:
  t.start()
for t in more_thread:
  t.join()
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()


# get_thread(thread3)