# BFS -> Breadth-First Search -> 너비 우선 탐색 -> 정점들과 같은 레벨에 있는 노드들(형제 노드들)을 먼저 탐색하는 방식
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start_node):
    visited = list()
    need_visit = list()
    
    need_visit.append(start_node)
    
    while (need_visit):
        node = need_visit.pop(0)
        if (node not in visited):
            visited.append(node)
            need_visit.extend(graph[node])
            
    print(visited)
    
bfs(graph, 'A')

# 시간 복잡도
# 노드 수 : V
# 간선 수 : E
# --> O(V+E)

#---------------------------------------------------------------------------

# DFS -> Depth-First Search -> 깊이 우선 탐색

def dfs(graph, start_node):
    visited = list()
    need_visit = list()
    
    need_visit.append(start_node)
    
    while (need_visit):
        node = need_visit.pop()
        if (node not in visited):
            visited.append(node)
            need_visit.extend(graph[node])
            
    print(visited)
    
dfs(graph, 'A')