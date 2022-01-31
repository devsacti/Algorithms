import sys
from collections import deque

    #curNode : INDEX OF COMPUTER
def dfs_basic(curNode):
    global graph,visited_dfs

    visited_dfs.append(curNode)
    print(curNode, end=' ')

    for adj in graph[curNode]:
        if(adj not in visited_dfs): dfs_basic(adj) 
        else: continue

def dfsplus():
    global visited_dfs
    for node,val in enumerate(graph):
        if node not in visited_dfs:
            dfs_basic(node)

def ex_bfs_basic(startNode):
    global graph

    q=deque()
    q.append(startNode)

    while(q):
        curNode= q.popleft()
        print(curNode, end=' ')
        
        if curNode not in visited_bfs:
            visited_bfs.append(curNode)
            # 이렇게 해도 2개의 노드에 동시에 인접한 노드(미방문)가 동시에 큐에 
            # 중복으로 들어가는 일 발생. 미래값에 대한 대응필요해보임
            # for adj in graph[curNode]:
            #     if(adj not in visited_bfs): q.append(adj)
            #     else: continue
            
        else: pass

# 동작의 일관성을 위해서, 처음 노드를 방문 직후 큐에 넣지 않고, 넣기 직전 칠한다.
# 또한 나를 위해서, willbevisited로 선언한다.
def ex2bfs_basic(startNode):
    global graph,willbevisited

    q=deque()

    willbevisited.append(startNode)
    q.append(startNode)

    while(q):
        curNode= q.popleft()
        print(curNode, end=' ')

        for adj in graph[curNode]:
            if(adj not in willbevisited):
                willbevisited.append(adj)
                q.append(adj)
            else: pass    

# 발전형
# visited 리스트가 직관적이지만 역시 길어지면 문제
# 근데 생각해보니까, 노드의 이름이 불규칙하면 어쩔수없이 써야함
def bfs_basic(start_v):
    q=deque()
    willbevisited[start_v]=True
    q.append(start_v)

    while q:
        v=q.popleft()
        print(v, end=' ')
        
        for adj in graph[v]:
            # willbevisited는 false로 초기화라 not 만날 시 true
            if(not willbevisited[adj]):
                willbevisited[adj]=True
                q.append(adj)

def bfsplus():
    global willbevisited

    for node, val in enumerate(graph):
        if(not willbevisited[node]):
            bfs_basic(node)


if __name__=="__main__":
    N,M = map(int, sys.stdin.readline().split())

    global graph
    graph = [[] for _ in range(N)]
    visited_dfs = []
    willbevisited = [False for _ in range(N)]
    # print(willbevisited)

    for _ in range(M):
        idx_node, adj = map(int, sys.stdin.readline().split())
        graph[idx_node].append(adj)

        adj, idx_node = idx_node, adj
        graph[idx_node].append(adj)

    # print(graph)

    dfsplus()
    print()
    bfsplus()