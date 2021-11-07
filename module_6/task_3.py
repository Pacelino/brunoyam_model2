import time
import requests
from threading import Thread
more_link = [['https://httpbin.org/get'], ['https://www.youtube.com/'], ['https://vk.com'], ['https://www.python.org/'], ['https://www.youtube.com/watch?v=xRQeXNZX_cQ']]
# j = ','.join(more_link[0:1])
# print(more_link[1:4])
def get_html(link):
  respone = requests.get(link)
  return respone.text


thread1 = Thread(target=get_html, args=more_link[0])
thread2 = Thread(target=get_html, args=more_link[1])
thread3 = Thread(target=get_html, args=more_link[2])
thread4 = Thread(target=get_html, args=more_link[3])
thread5 = Thread(target=get_html, args=more_link[4])


t1 = time.time()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

print(f'Время параллельного запуска {time.time()-t1}')

t2 = time.time()
for i in more_link:
  j = "".join(i)
  get_html(j)
print(f'Время последовательного запуска {time.time()-t2}')