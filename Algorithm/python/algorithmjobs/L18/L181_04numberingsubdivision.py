# 단지 번호 붙이기

# 중요 개념활용
# dfs, bfs는 언제나 인접행렬이나 인접리스트_간선에 대한 자료구조_로 정의된 graph가 주어져야한다?\
# 아니다. 로직이 특정 자료형을 반드시 필수로 한다기보단
# 특정 자료형과 별개로, 로직상으로 넓게 이해하여

# 주어진 정보 내에서 특정 조건을 통해 주변 노드로 접근가능하다면,
# 그 또한 graph로 간주 및 dfs,bfs활용이 가능하다.
# 가령 이번 단지 번호 붙이기는, 별도의 인접리스트 없이 matrix상에서
# 함축된 간선 정보를 바탕으로 dfs가 작동한다.

import sys

numdict_subdivision={
    # index가 key로서 추가되고 val이 증가할 예정
    # key 0 추가 그리고 val 1~
}

def dfs(cur_r, cur_c ,num_subdivision):
    global matrix,visited, num_house
    # cur_r, cur_c : INDEX OF COMPUTER
    # num_subdivision : 1~

    # print('current ', cur_r,cur_c)
    # print('current ',num_subdivision)

    # 요령상 방문 True 대신 단지 번호 활용할 수 있으나 일단 기본에 충실
    visited[cur_r][cur_c]= 1
    num_house[cur_r][cur_c]=num_subdivision
    numdict_subdivision[num_subdivision]+=1

    # direction vector
    magnitude=1
    dr=[0,0,magnitude,-magnitude]
    dc=[magnitude,-magnitude,0,0]

    kinds_dir=len(dr)

    for d in range(kinds_dir):
        cand_r = cur_r + dr[d]
        cand_c = cur_c + dc[d]

        if(cand_r<0 or cand_r>N-1 or cand_c<0 or cand_c>N-1):
            continue

        if(matrix[cand_r][cand_c]==0):
            continue
        else:
            if(visited[cand_r][cand_c]==1):
                continue
            else:
                dfs(cand_r, cand_c,num_subdivision)

    # print('current ', cur_r,cur_c)
    # print('current ',num_subdivision)

    # # print(*visited, sep='\n')
    # # print('--')
    # print(*num_house, sep='\n')
    # print('--')

    
if __name__=="__main__":
    N=int(sys.stdin.readline().strip())

    global matrix, visited,num_house
    matrix=[]
    for _ in range(N):
        row=[int(element) for element in sys.stdin.readline().strip()]
        matrix.append(row)
    # print(*matrix, sep='\n')

    visited=[[0]*N for _ in range(N)]
    num_house=[[0]*N for _ in range(N)]

    num_subdivision=0

    for idx_r in range(N):
        for idx_c in range(N):
            # 집 존재 유무 체크
            if(matrix[idx_r][idx_c]==1):
                # 이전 방문 여부 체크
                if(visited[idx_r][idx_c] == 0):
                    #dfs
                    num_subdivision+=1
                    if( num_subdivision not in numdict_subdivision.keys()):
                        numdict_subdivision[num_subdivision]=0
                    dfs(idx_r,idx_c,num_subdivision)
                else:
                    continue
            else:
                continue

    print(len(numdict_subdivision))
    result=sorted(numdict_subdivision.values())
    for val in result:
        print(val)