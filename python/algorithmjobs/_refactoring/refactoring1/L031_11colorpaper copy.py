import sys

if __name__=="__main__":
    N=int(sys.stdin.readline().strip())

    vectors=[]

    min_ci_r=1000;max_ci_r=-1000 
    min_ci_c=1000;max_ci_c=-1000

    for _ in range(N):
        cidx_r, cidx_c, length_r, length_c = map(int, sys.stdin.readline().split())
        vectors.append( (cidx_r, cidx_c,length_r,length_c) )

        # min값을 구하는 건 추가적인 연산을 요구하고, 의미도 없다는 걸 깨달음
        # cand_min_cir=cidx_r
        # cand_min_cic=cidx_c

        cand_max_cir=cidx_r+length_r-1
        cand_max_cic=cidx_c+length_c-1

        # # about row
        # if(cand_min_cir<min_ci_r):
        #     min_ci_r=cand_min_cir
        
        if(cand_max_cir>max_ci_r):
            max_ci_r=cand_max_cir

        # about col
        # if(cand_min_cic<min_ci_c):
        #     min_ci_c=cand_min_cic

        if(cand_max_cic>max_ci_c):
            max_ci_c=cand_max_cic

    # print(vectors)
    # print(min_ci_r,max_ci_r)
    # print(min_ci_c,max_ci_c)

    # 맨 왼쪽 위 좌표와 맨오른쪽 아래 좌표 구하기
    # max_r or c is equal limit
    matrix=[[0]*(max_ci_c+1) for _ in range(max_ci_r+1)]
    # print(*matrix, sep='\n')
    # print('---')


    # flag를 세우는 방법은 첫번째는 전체 매트릭스를 매번 좌표방문해서 해당 좌표가
    # 해당 영역에 들어가냐 마냐를 매번 판별해서 flag를 세우거나

    # 처음부터 주어진 벡터 정보들로 유효한 좌표들을 만들어서
    # 유효좌표들만 방문해서 플래그 세우는 방법이 있다.
    # 가령, 이중 폴문 안에서 idx_r > start_row and end_row>idx_r and 똑같이 칼럼에 대해서

    # 리스트 컴프리헨션하면
    # 의외로 후자가 구현도 시간도 모두 유리하지 않을까

    for flag, vector in enumerate(vectors,1):
        cidx_r, cidx_c, length_r, length_c = vector
        
        valid_coordinates=[(i,j) for i in range(cidx_r,cidx_r+length_r) for j in range(cidx_c,cidx_c+length_c)]
        # print(valid_coordinates)

        for valid_coordinate in valid_coordinates:
            tmp1=valid_coordinate[0]
            tmp2=valid_coordinate[1]
            matrix[tmp1][tmp2]=flag
        # print(*matrix, sep='\n')
        
    # print(*matrix, sep='\n')
    
    flags={ flag : 0 for flag in range(1,N+1)}
    # 변수가 중간에 바뀌는 상황도 염두하자
    length_r=max_ci_r-min_ci_r+1
    length_c=max_ci_c-min_ci_c+1

    for ci_r in range(max_ci_r):
        for ci_c in range(max_ci_c):
            if(matrix[ci_r][ci_c] in flags.keys()):
                flags[matrix[ci_r][ci_c]]+=1
            
    # print(flags)

    # 0은 없다니까 삭제해주자
    if 0 in flags.keys():
        del flags[0]

    for key, val in flags.items():
        print(val)