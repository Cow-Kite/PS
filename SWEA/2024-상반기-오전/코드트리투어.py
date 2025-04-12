import heapq

graph = []
costs = []
n = 0
m = 0
products = []
products_id = set()
deleted = set()

def make_roads(data):
    global n, m, graph

    n = data[0]
    m = data[1]
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(2, len(data), 3):
        if graph[data[i]][data[i + 1]] == 0 or graph[data[i]][data[i + 1]] > data[i + 2]:
            graph[data[i]][data[i + 1]] = data[i + 2]
            graph[data[i + 1]][data[i]] = data[i + 2]

    dijkstra(0)

def dijkstra(start_node):
    global costs, graph, n

    costs = [float('inf') for _ in range(n)]
    minHeap = [(0, start_node)]
    costs[start_node] = 0

    while minHeap:
        current_distance, current_node = heapq.heappop(minHeap)

        if current_distance > costs[current_node]:
            continue

        for i in range(n):
            if graph[current_node][i] != 0:
                distance = graph[current_node][i] + current_distance

                if distance < costs[i]:
                    costs[i] = distance
                    heapq.heappush(minHeap, (distance, i))

def add_product(product_id, revenue, dest):
    global costs, products

    cost = costs[dest]
    value = revenue - cost
    heapq.heappush(products, (-value, product_id, revenue, dest))
    products_id.add(product_id)

def cancel_product(product_id):
    if product_id in products_id:
        deleted.add(product_id)
        products_id.remove(product_id)

def sell_best_product():
    global products

    if products:
        while products:
            value, id, revenue, dest = products[0]
            if id in deleted:
                heapq.heappop(products)
                deleted.remove(id)
                continue

            if  value <= 0:  # 삭제되지 않은 상품만 처리
                heapq.heappop(products)
                products_id.remove(id)
                print(id)
                return
            else:
                print(-1)
                return
    print(-1)  # 판매 가능한 상품이 없을 때

def change_departure(new_start):
    dijkstra(new_start)
    # 기존 상품들에 대한 비용을 다시 계산
    new_products = []
    for value, product_id, revenue, dest in products:
        if product_id not in deleted:
            new_cost = costs[dest]
            value = revenue - new_cost
            heapq.heappush(new_products, (-value , product_id, revenue, dest))
    deleted.clear()
    products[:] = new_products

def solv():
    Q = int(input())

    for _ in range(Q):
        commands = list(map(int, input().split()))
        if commands[0] == 100:
            make_roads(commands[1:])
        elif commands[0] == 200:
            product_id, revenue, dest = commands[1], commands[2], commands[3]
            add_product(product_id, revenue, dest)
        elif commands[0] == 300:
            product_id = commands[1]
            cancel_product(product_id)
        elif commands[0] == 400:
            sell_best_product()
        elif commands[0] == 500:
            new_start = commands[1]
            change_departure(new_start)


solv()
