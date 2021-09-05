from collections import deque
N, M = map(int, input('введите сначало кол-во вершин, а потом кол-во ребер').split())  # количество вершин и ребер

graph = {i: set() for i in range(N)}  # будем хранить ввиде словаря с множествами
for i in range(M):
    v1, v2 = map(int, input())  # считаем реберо
    graph[v1].add(v2)  # добавляем смежность двух вершин
    graph[v2].add(v1)
# поиск в ширину


start_vertex = 1  # стартовая вершина
queue = deque([start_vertex])  # создаем очередь
dis = [None] * N  # массив расстояний, по умолчанию неизвестен
dis[start_vertex] = 0  # расстояния до себя же равное 0
while queue:  # пока очердь не пуста
    cur_v = queue.popleft()  # достаем первый элемент
    for neigh_v in graph[cur_v]:  # проходим всех его соседей
        if dis[neigh_v] is None:  # если сосед еще не посещен
            dis[neigh_v] = dis[cur_v] + 1  # считаем расстояние
            queue.append(neigh_v)  # добавляем в очередь чтобы проверить его соседа
print(dis)