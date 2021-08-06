import sys
from collections import deque

def bfs_color(v,color):
    global graph,samecolored
    global willbevisited,token_possible

    q=deque()

    willbevisited[v]=True
    q.append( (v,color) )

    while(q):
        curV, curColor=q.popleft()
        # print(curV,curColor, end=' ')
        samecolored[curV]=curColor
        
        # ck color and coloring
        # print('adj', graph[curV])
        for adj in graph[curV]:
            # print('color adj', samecolored[adj], end='/')
            if(samecolored[adj]==curColor):
                token_possible=False
                break
        color = not curColor
        # print('\nnext color', color)
        # basic bfs
        for adj in graph[curV]:
            if(not willbevisited[adj]):
                willbevisited[adj]=True
                q.append( (adj,color) )


if __name__=="__main__":
    N,M=map(int, sys.stdin.readline().split())

    graph=[[] for _ in range(N)]
    '''(0 ≤ a, b ≤ N-1)이 조건때문에 가능, 아니면 리스트로'''
    willbevisited=[False for _ in range(N)]
    samecolored=[None for _ in range(N)]

    token_possible=True

    for _ in range(M):
        #bidirectional
        idx_node,child=map(int, sys.stdin.readline().split())
        graph[idx_node].append(child)
        graph[child].append(idx_node)

        # graph[idx_node].sort()
        # graph[child].sort()

    # print(graph)
    
    # color는 없음 흑 백, NULL 0 1, None False True
    color=True
    bfs_color(0,color)
    # print(samecolored)

    if(token_possible):
        print("YES")
    else:
        print("NO")
