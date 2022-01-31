import sys
from collections import deque

def bfs_basic(v):
    global graph, willbevisited
    global cnt_infested

    q=deque()
    willbevisited.append(v)
    q.append(v)
    

    while(q):
        curV=q.popleft()
        if(curV!=1): cnt_infested+=1
        # print(curV, graph[curV])
        # 인풋조건상, 노드는 간선이 있을경우에만 정의되는 특성에 따라
        # 해당노드가 정의된 경우, 즉 간선이 있는 경우에 한해서 작동
        if(curV in graph.keys()):
            for adj in graph[curV]:
                if(adj not in willbevisited):
                    willbevisited.append(adj)
                    q.append(adj)


if __name__=="__main__":
    N = int(sys.stdin.readline().strip())
    M =int(sys.stdin.readline().strip())

    global graph, willbevisited
    # 노드 인덱스가 0부터인지 1부터인지 신경안써도되서 사전형 그래프가 나은듯
    # 근데 계속해보니까 인풋이나 뒤에 처리가 추가되서 역시 맞춤형
    graph={}
    willbevisited=[]
    global cnt_infested
    cnt_infested =0

    for _ in range(M):
        idx_node, adj = map(int, sys.stdin.readline().split())
        if(idx_node not in graph.keys()):
            graph[idx_node]=list()
            graph[idx_node].append(adj)
        else:
            graph[idx_node].append(adj)

        if(adj not in graph.keys()):
            graph[adj]=list()
            graph[adj].append(idx_node)
        else:
            graph[adj].append(idx_node)

    # print(graph)
    bfs_basic(1)
    print(cnt_infested)