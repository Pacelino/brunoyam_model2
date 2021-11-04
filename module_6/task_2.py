import time
from threading import Thread
from datetime import datetime
# последовательный запуск
def start_rocket(number):
    time.sleep(3)
    print(f'Rocket № {number} started')

t = time.time()

for i in range(5):
    start_rocket(i+1)
print(f'последовательный запуск завершен.Время затраченное на это {time.time()-t}')


# параллельный запуск
t1 = datetime.now()
thread = [Thread(target=start_rocket, args=(i+1, )) for i in range(5)]  # создали потоки и сохранили в список
for t in thread:  # запустили потоки
    t.start()
for t in thread:  # объединли потоки
    t.join()
print(f'Параллельный запуска завершен. Время затраченное на это {(datetime.now()-t1).seconds} секунды.')