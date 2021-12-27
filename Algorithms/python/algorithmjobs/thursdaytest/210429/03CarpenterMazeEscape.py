# 목수의 미로탈출
# 오후 6:47 2021-04-29
# 핵심
# start와 end의 개별 bfs 그리고 1개 짜르면 양쪽에서 접근

import sys
from collections import deque
global N,M,maze
global trees

def bfs(start,costmatrix, willbevisited):
    global N,M, maze
    q=deque()
    cost=0

    # r,c ; INDEX OF COMPUTER
    r,c = start
    willbevisited[r][c]=1
    q.append((r,c,cost))

    while(q):
        curR,curC,curCost = q.popleft()
        costmatrix[curR][curC]=curCost

        dr=[1,-1,0,0]
        dc=[0,0,1,-1]

        cost=curCost+1
        for d in range(4):
            candR=curR+dr[d]
            candC=curC+dc[d]

            if(candR<0 or candR>N-1 or candC<0 or candC>M-1):
                continue

            if(maze[candR][candC]==1):
                if(costmatrix[candR][candC]==0):costmatrix[candR][candC]=curCost+1
                continue

            if(willbevisited[candR][candC]==1):
                continue

            willbevisited[candR][candC]=1
            q.append((candR,candC,cost))

if __name__=="__main__":
    N,M = map(int, sys.stdin.readline().split())
    # maze ; 2d matrix
    maze=[]
    trees=[]
    for r in range(N):
        row=list(map(int,sys.stdin.readline().split()))
        maze.append(row)

        for c,val in enumerate(row):
            if(val == 1):
                trees.append((r,c))
    # print(trees)

    # start
    start=(N-1,0)
    costmatrix_S=[[0]*M for _ in range(N)]
    willbevisited_S=[[0]*M for _ in range(N)]

    bfs(start,costmatrix_S,willbevisited_S)

    # print(*costmatrix_S,sep='\n')
    # print('---')

    # end
    end=(0,M-1)
    costmatrix_E=[[0]*M for _ in range(N)]
    willbevisited_E=[[0]*M for _ in range(N)]

    bfs(end,costmatrix_E,willbevisited_E)

    # print(*costmatrix_E,sep='\n')
    mincost=100000000000000
    for tree in trees:
        r,c=tree
        if(costmatrix_S[r][c]!=0 and costmatrix_E[r][c]!=0):
            totalcost=costmatrix_S[r][c]+costmatrix_E[r][c]
            if(totalcost<mincost):
                # print(r,c,totalcost)
                mincost=totalcost
    
    print(mincost)