import sys
from collections import deque

def bfs_color(v,color):
    global graph, willbevisited,color_v,token_possible

    q=deque()
    willbevisited.append( v )
    q.append( (v,color) )

    while(q):
        curV, curColor =q.popleft()
        # print('cur V color ', curV, curColor)
        color_v[curV]=curColor

        # dfs에서는 한번 시행하면 한 갈래 내 모든 정점이 색칠되서
        # 그냥 (그 다음 별개 가래의)현재 노드 기준으로 잡아도 판단되지만
        # bfs는 과정중에는 그게 안되는 특성 발견, bfs 완전 시행 후 판단해야            
        color = not curColor

        for adj in graph[curV]:
            if(adj not in willbevisited):
                willbevisited.append(adj)
                q.append( (adj, color) )

def ck_color():
    global graph,color_v,token_possible

    #ck color of adj
    for v in graph.keys():
        for adj in graph[v]:
            if(color_v[adj]==color_v[v]):
                token_possible=False
                break

        if(token_possible == False):
            break



if __name__=="__main__":
    N,M=map(int, sys.stdin.readline().split())

    global graph, willbevisited,color_v,token_possible

    graph={Node: set() for Node in range(1,N+1)}
    willbevisited=[]
    color_v={Node: None for Node in range(1,N+1)}

    token_possible=True

    for _ in range(M):
        #bidirectioanl
        idx_node,adj=map(int, sys.stdin.readline().split())
        graph[idx_node].add(adj)
        graph[adj].add(idx_node)

    # print(graph)
    # print(color_v)
    # none, false, True ; 색 없음, group 0 , group 1
    color= True
    bfs_color(1,color)
    # print(color_v)

    ck_color()

    if(token_possible):
        print("Yes")
    else:
        print("No")
