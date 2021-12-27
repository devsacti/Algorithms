# tcp 어느 한쪽이 못가는 곳의 값들까지 포함해서 출력하면 안됨
# wrong 막히는 인풋은 없다고 함

import sys
from collections import deque

global N,M
global maze

def bfsCarpenter(v, willbevisited, costMatrix):
    global N,M
    global maze
    q = deque()

    curR, curC = v
    willbevisited[curR][curC]=1
    cost = 0
    q.append((curR, curC,cost))

    # dir_vector, m ; maginitude
    m = 1
    dr=[m,-m,0,0]
    dc=[0,0,m,-m]
    kinds_dir=len(dr)

    while(q):
        curR, curC, curCost = q.popleft()
        # print(curR, curC, curCost)

        willbevisited[curR][curC] = 1
        costMatrix[curR][curC] = curCost
        # print(*costMatrix,sep='\n')

        cost = curCost+1

        for d in range(kinds_dir):
            candR= curR+dr[d]
            candC= curC+dc[d]

            if(candR<0 or candR>N-1 or candC<0 or candC>M-1):
                continue

            if(maze[candR][candC] == 1 ):
                # set for cutting the tree, update the cost but dont visit
                if(costMatrix[candR][candC]==0 or curCost + 1<costMatrix[candR][candC]):
                    costMatrix[candR][candC] = curCost + 1 
                continue

            # now cand become valid adj
            if(willbevisited[candR][candC]!=1):
                willbevisited[candR][candC]=1
                q.append( (candR, candC,cost))


if __name__=="__main__":
    N,M = map(int, sys.stdin.readline().split())

    # maze is 2 dimension, and 1-base indexing
    maze=[]
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        maze.append(row)

    # list of coordinates of tree
    trees=[]

    for r in range(N):
        for c in range(M):
            if(maze[r][c]==1):
                trees.append((r,c))

    # costS costE are 2 dimension
    willbevisitedS=[[0]*M for _ in range(N)]
    willbevisitedE=[[0]*M for _ in range(N)]
    
    # bfs 
    S = (N-1, 0)
    E = (0, M-1)

    costS =[[0]*M for _ in range(N)]
    costE =[[0]*M for _ in range(N)]

    bfsCarpenter( S, willbevisitedS, costS)
    # print(*costS, sep='\n')
    # print('--')
    bfsCarpenter( E, willbevisitedE, costE)
    # print(*costE, sep='\n')

    min_cost=10000000000000000
    for tree in trees:
        # r,c INDEX OF COMPUTER
        r,c = tree
        # print(r,c, costS[r][c],costE[r][c])
        if(costS[r][c] != 0 and costE[r][c] != 0):
            totalcost= costS[r][c] + costE[r][c]
            if(totalcost<min_cost):
                min_cost=totalcost

    print(min_cost)