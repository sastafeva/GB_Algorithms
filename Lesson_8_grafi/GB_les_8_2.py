# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

# В задаче не требуется генерировать новый взвешенный граф. Пользуемся имеющимся.
# К Д/з приложила скриншот с графом из видео, чтобы можно быть проверить, верно ли работает функция

from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    s = start
    is_visited = [False] * length  # посещена ли вершина
    cost = [float('inf')] * length  # вес пути

    # пока мы не знаем родителя для вершины, мы храним значение -1,
    # а когда узнаем, запишем его
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0  # Будет показывать, двигаемся мы дальше по графу или уже нет

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):

            # Если есть путь в вершину и эта вершина еще не посещена
            if vertex != 0 and not is_visited[i]:

                # Если записанный вес больше, чем текущий vertex + вес до стартовой точки
                if cost[i] > vertex + cost[start]:
                    # Для i-той вершины записываем меньший вес
                    cost[i] = vertex + cost[start]

                    # И указываем, какая вершина является родительской
                    parent[i] = start


        min_cost = float('inf')

        # цикл, который пройдет по всем вершинам графа и проверит, можно ли еще стартовать откуда-то
        for i in range(length):

            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i


    # Доработаем алгоритм, чтобы он возвращал словарь пути от стартовой вершины до каждой.
    # Будем использовать список parent, потому что в него записываются родители по кратчайшему пути

    # Назначим родителем стартовой вершины самого себя
    parent[s] = s

    # Создадим словарь путей и заполним его первым значением, равным конечной точке маршрута
    way = {}
    for i in range(length):
        way[i] = deque([i])

    # Пройдем по словарю и заполним его оставшимися точками
    for i in way:
        # Если указан родитель
        if parent[i] != (-1):

            # Если мы в стартовой точке, то ничего заполнять не надо
            if i == s:
                continue

            spam = i

            # Добавляем родителей из parent в путь до тех пор, пока не доберемся до стартовой точки
            while spam != s:
                way[i].appendleft(parent[spam])
                spam = parent[spam]

        # Если родитель в parent не указан
        else:
            way[i] = ['нет пути']


    return cost, way

# Задаем стартовую точку:
s = int(input('От какой вершины идти (от 0 до 7): '))

# Сделаем проверку корректности ввода:
if 0 <= s <= 7:

    cost, way = dijkstra(g, s)

    print(f'\n Кратчайшие пути от вершины {s}:\n {cost}\n')

    print('Вершины, которые надо обойти')
    # Распечатаем красиво
    for k in way:
        print(k, ':', *way[k])

else:
    print('Некорректный ввод, начните сначала')
