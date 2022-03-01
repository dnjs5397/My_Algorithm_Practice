# 최단 경로 문제 종류

# 1. 단일 출발 및 단일 도착 
#    - 그래프 내의 특정 노드 u에서 출발, 다른 특정 노드 v에 도착하는 가장 짧은 경로를 찾는 문제

# 2. 단일 출발 
#    - 그래프 내의 특정 노드 u와 그래프 내 다른 모든 노드들 간의 가장 짧은 경로를 찾는 문제

# 3. 전체 쌍 최단경로
#    - 그래프 내의 모든 쌍(u,v)에 대한 최단 경로를 찾는 문제

# heapq 라이브러리 활용을 통해 우선순위 큐 사용

import heapq

mygraph = {
    'A':{'B':8, 'C':1, 'D':2},
    'B':{},
    'C':{'B':5, 'D':2},
    'D':{'E':3, 'F':5},
    'E':{'F':1},
    'F':{'A':5}
}

def dijkstra(graph, start):
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    print(distances)
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_distance:
            continue
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if (distance < distances[adjacent]):
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
                
    print(distances)
    
dijkstra(mygraph, 'C')

# 시간 복잡도
# 인접한 간선들 검사 O(E)
# 우선순위 큐에 노드/거리 정보 넣고 삭제 O(E+logE)
# O(E + ElogE) = O(ElogE)