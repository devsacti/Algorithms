# 단지 번호 붙이기
import sys
from collections import deque
import itertools

def bfs(start_r, start_c):
    global matrix,willbevisited, num_house,numdict_subdivision

    q=deque()
    # print('current ', cur_r,cur_c)
    # print('current ',num_subdivision)

    willbevisited[start_r][start_c]= 1
    q.append( (start_r,start_c) )

    while(q):
        # curR, curC are correspond with '1 Vertex'
        curR, curC = q.popleft()
        num_house[curR][curC]=num_subdivision;numdict_subdivision[num_subdivision]+=1

        # direction vector
        magnitude=1
        dr=[0,0,magnitude,-magnitude]
        dc=[magnitude,-magnitude,0,0]

        kinds_dir=len(dr)

        # adj 탐색과 방문예정체크 후 큐 삽입
        for d in range(kinds_dir):
            adj_r = curR + dr[d]
            adj_c = curC + dc[d]

            if(adj_r<0 or adj_r>N-1 or adj_c<0 or adj_c>N-1):
                continue

            if(matrix[adj_r][adj_c]==0):
                continue
            else:
                if(willbevisited[adj_r][adj_c]==1):
                    continue
                else:
                    willbevisited[adj_r][adj_c]=1
                    q.append( (adj_r,adj_c) )

        # print('current ', cur_r,cur_c)
        # print('current ',num_subdivision)

        # # print(*visited, sep='\n')
        # # print('--')
        # print(*num_house, sep='\n')
        # print('--')

    
if __name__=="__main__":
    N=int(sys.stdin.readline().strip())

    global matrix, willbevisited,num_house
    matrix=[]
    for _ in range(N):
        row=[int(element) for element in sys.stdin.readline().strip()]
        matrix.append(row)
    # print(*matrix, sep='\n')

    willbevisited=[[0]*N for _ in range(N)]
    num_house=[[0]*N for _ in range(N)]

    global numdict_subdivision
    num_subdivision=0
    numdict_subdivision={}

    for idx_r in range(N):
        for idx_c in range(N):
            # 집 존재 유무 체크 and 이전 방문 여부 체크; 처음부터 '새로운' '집'좌표만 bfs에 들어감
            if(matrix[idx_r][idx_c]==1):
                if(willbevisited[idx_r][idx_c] == 0):
                    num_subdivision+=1
                    if( num_subdivision not in numdict_subdivision.keys()):
                        numdict_subdivision[num_subdivision]=0
                    bfs(idx_r,idx_c)
                else:
                    continue
            else:
                continue

    print(len(numdict_subdivision))
    result=sorted(numdict_subdivision.values())
    for val in result:
        print(val)