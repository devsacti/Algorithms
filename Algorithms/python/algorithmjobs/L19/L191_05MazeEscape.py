import sys
from collections import deque

# dist 를 매번 들고갈지 아니면, 그냥 좌표사이 거리로 갱신할지 하자면
# 후자가 더 간단해보이니까 그렇게 핮.

# !! 중요질문 나는 bfs가 돌다가 End에 도달하면 출력하게 설정했더니 60점
# 혹시나 해서 그냥 해설 cost 매트릭스 대응하여 비용매트릭스에서 End좌표를 출력 100점
# N,M이 1이고 벽이 없다면 경우 최단거리는 0이 출력되야한고 실제 내껀 그렇다.
# 근데, 길이 막혀서 End에 못가는데도 0이 뜨는 근거가 있나?

def bfs(startR, startC):
    global N,M, dist
    global matrix, length_matrix, willbevisited
    q=deque()

    willbevisited[startR][startC]=1
    q.append( (startR,startC,dist) )

    #
    magnitude=1
    dr=[0,0,magnitude,-magnitude]
    dc=[magnitude,-magnitude,0,0]

    kinds_dir=len(dr)

    while(q):
        # curR,curC : INDEX OF COMPUTER
        curR, curC, curDist = q.popleft()
        
        length_matrix[curR][curC]=curDist
        # print(curR,curC,'//',dist)
        # if(curR==0 and curC==M-1): print(dist)

        dist=curDist+1

        for d in range(kinds_dir):
            adjR=curR+dr[d]
            adjC=curC+dc[d]

            if(adjR<0 or adjR>N-1 or adjC<0 or adjC>M-1):
                continue

            if(matrix[adjR][adjC]==1):
                continue

            if(willbevisited[adjR][adjC]==1):
                continue

            #now updatte
            willbevisited[adjR][adjC]=1
            q.append((adjR,adjC,dist))

if __name__=="__main__":
    global N,M, dist
    N,M = map(int, sys.stdin.readline().split())
    dist=0

    global matrix, length_matrix, willbevisited
    matrix=[]
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        matrix.append(row)
    # print(*matrix,sep='\n')

    length_matrix=[[0]*M for _ in range(N)]
    willbevisited=[[0]*M for _ in range(N)]

    # print(*length_matrix,sep='\n')
    # print(*willbevisited,sep='\n')

    startR, startC = N-1, 0
    bfs(startR,startC)

    # print(*length_matrix,sep='\n')

    print(length_matrix[0][M-1])