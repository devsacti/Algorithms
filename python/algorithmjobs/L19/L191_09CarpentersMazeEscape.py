import sys
from collections import deque

# tcp 1, 한쪽에서는 접근 불가한 영역이 0이라 최소값이 그 좌표의 접근가능한 한쪽으로만 갱신
# tcp 2, 나무 1개 베는 걸로는 서로 못만날때
# 문제 조건 상 목수는 언제나 도달가능
# tcp 3, threshold의 부적절한 N 범위에 맞추어 매우크게 100으론 부족

def bfs_S(startR, startC):
    global N,M, dist
    global matrix, cost_matrix_S, willbevisited_S
    q=deque()

    willbevisited_S[startR][startC]=1
    q.append( (startR,startC,dist) )

    #
    magnitude=1
    dr=[0,0,magnitude,-magnitude]
    dc=[magnitude,-magnitude,0,0]

    kinds_dir=len(dr)

    while(q):
        # curR,curC : INDEX OF COMPUTER
        curR, curC, curDist = q.popleft()
        
        cost_matrix_S[curR][curC]=curDist
        # print(curR,curC,'//',dist)
        # if(curR==0 and curC==M-1): print(dist)

        dist=curDist+1

        for d in range(kinds_dir):
            adjR=curR+dr[d]
            adjC=curC+dc[d]

            if(adjR<0 or adjR>N-1 or adjC<0 or adjC>M-1):
                continue

            if(matrix[adjR][adjC]==1):
                #방문하지는 않고 벽 1개 뿌셨을 때 해당위치까지의 코스트만 갱신
                if(cost_matrix_S[adjR][adjC]==0):cost_matrix_S[adjR][adjC]=curDist+1
                continue

            if(willbevisited_S[adjR][adjC]==1):
                continue

            #now updatte
            willbevisited_S[adjR][adjC]=1
            q.append((adjR,adjC,dist))

def bfs_E(startR, startC):
    global N,M, dist
    global matrix, cost_matrix_E, willbevisited_E
    q=deque()

    willbevisited_E[startR][startC]=1
    q.append( (startR,startC,dist) )

    #
    magnitude=1
    dr=[0,0,magnitude,-magnitude]
    dc=[magnitude,-magnitude,0,0]

    kinds_dir=len(dr)

    while(q):
        # curR,curC : INDEX OF COMPUTER
        curR, curC, curDist = q.popleft()
        
        cost_matrix_E[curR][curC]=curDist
        # print(curR,curC,'//',dist)
        # if(curR==0 and curC==M-1): print(dist)

        dist=curDist+1

        for d in range(kinds_dir):
            adjR=curR+dr[d]
            adjC=curC+dc[d]

            if(adjR<0 or adjR>N-1 or adjC<0 or adjC>M-1):
                continue

            if(matrix[adjR][adjC]==1):
                #방문하지는 않고 벽 1개 뿌셨을 때 해당위치까지의 코스트만 갱신
                if(cost_matrix_E[adjR][adjC]==0):cost_matrix_E[adjR][adjC]=curDist+1
                continue

            if(willbevisited_E[adjR][adjC]==1):
                continue

            #now updatte
            willbevisited_E[adjR][adjC]=1
            q.append((adjR,adjC,dist))

if __name__=="__main__":
    global N,M, dist
    N,M = map(int, sys.stdin.readline().split())
    dist=0

    global matrix, cost_matrix_S,cost_matrix_E,willbevisited_S,willbevisited_E
    matrix=[]
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        matrix.append(row)
    # print(*matrix,sep='\n')

    coordinates_one=[]
    # r,c ; INDEX OF COMPUTER
    for r in range(N):
        for c in range(M):
            if(matrix[r][c]==1):
                coordinates_one.append( (r,c) )

    cost_matrix_S=[[0]*M for _ in range(N)]
    cost_matrix_E=[[0]*M for _ in range(N)]

    willbevisited_S=[[0]*M for _ in range(N)]
    willbevisited_E=[[0]*M for _ in range(N)]

    startR, startC = N-1, 0
    bfs_S(startR,startC)
    
    dist=0
    startR, startC = 0, M-1
    bfs_E(startR,startC)

    # print(*cost_matrix_S,sep='\n')
    # print('--')
    # print(*cost_matrix_E,sep='\n')
    # print('--')

    min_costifcut=100000
    for coordinate_one in coordinates_one:
        # r,c : INDEX OF COMPUTER
        r, c = coordinate_one
        if(cost_matrix_S[r][c] != 0 and cost_matrix_E[r][c] != 0):
            costifcut=cost_matrix_S[r][c]+cost_matrix_E[r][c]
            if(costifcut<min_costifcut):
                min_costifcut=costifcut
                # print( r, c)
    
    print(min_costifcut)