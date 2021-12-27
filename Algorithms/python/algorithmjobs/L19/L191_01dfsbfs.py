import sys
from collections import deque

#curNode : INDEX OF COMPUTER
def dfs_basic(curNode):
    global graph,visited

    visited.append(curNode)
    print(curNode, end=' ')

    for adj in graph[curNode]:
        if(adj not in visited): dfs_basic(adj) 
        else: continue

def dfsplus():
    global N,visited
    num_vertex=[node for node in range(N)]
    for node in num_vertex:
        if node not in visited:
            dfs_basic(node)

# 발전형
# visited 리스트가 직관적이지만 역시 길어지면 문제
# 근데 생각해보니까, 노드의 이름이 불규칙하면 어쩔수없이 써야함
def bfs_basic(start_v):
    global graph, willbevisited

    q=deque()
    willbevisited.append(start_v)
    q.append(start_v)

    while q:
        v=q.popleft()
        print(v, end=' ')
        
        for adj in graph[v]:
            # willbevisited는 false로 초기화라 not 만날 시 true
            if(adj not in willbevisited):
                willbevisited.append(adj)
                q.append(adj)

def bfsplus():
    global N,willbevisited
    num_vertex=[node for node in range(N)]

    for node in num_vertex:
        if(node not in willbevisited):
            bfs_basic(node)


if __name__=="__main__":
    global N
    N,M = map(int, sys.stdin.readline().split())

    global graph, visited,willbevisited
    graph = [[] for _ in range(N)]
    visited = []
    willbevisited = []

    for _ in range(M):
        idx_node, adj = map(int, sys.stdin.readline().split())
        graph[idx_node].append(adj)
        graph[adj].append(idx_node)

        # 작은 값부터 들어가게 정렬이 필요했었다.
        graph[idx_node].sort()
        graph[adj].sort()
    print(graph)

    dfs_basic(0)
    print()
    bfs_basic(0)
    print()
    # dfsplus()
    # print()
    # bfsplus()