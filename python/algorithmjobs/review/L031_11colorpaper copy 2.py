import sys

if __name__=="__main__":
    N=int(sys.stdin.readline().strip())

    vectors=[]

    max_ci_r=-1000 
    max_ci_c=-1000

    for _ in range(N):
        cidx_r, cidx_c, length_r, length_c = map(int, sys.stdin.readline().split())
        vectors.append( (cidx_r, cidx_c,length_r,length_c) )

        cand_max_cir=cidx_r+length_r-1
        cand_max_cic=cidx_c+length_c-1

        # about row
        if(cand_max_cir>max_ci_r):
            max_ci_r=cand_max_cir

        # about col
        if(cand_max_cic>max_ci_c):
            max_ci_c=cand_max_cic

    # print(vectors)
    # print(max_ci_r)
    # print(max_ci_c)

    # 맨오른쪽 아래 좌표 구하기
    # max_r or c is equal limit
    matrix=[[0]*(max_ci_c+1) for _ in range(max_ci_r+1)]
    # print(*matrix, sep='\n')
    # print('row, col ',len(matrix), len(matrix[0]))
    # print('---')


    for flag, vector in enumerate(vectors,1):
        cidx_r, cidx_c, length_r, length_c = vector
        
        valid_coordinates=[(i,j) for i in range(cidx_r,cidx_r+length_r) for j in range(cidx_c,cidx_c+length_c)]
        # print(valid_coordinates)

        for valid_coordinate in valid_coordinates:
            tmp1=valid_coordinate[0]
            tmp2=valid_coordinate[1]
            matrix[tmp1][tmp2]=flag
        
    # print(*matrix, sep='\n')
    
    flags={ flag : 0 for flag in range(1,N+1)}

    for ci_r in range(max_ci_r+1):
        for ci_c in range(max_ci_c+1):
            if(matrix[ci_r][ci_c] in flags.keys()):
                flags[matrix[ci_r][ci_c]]+=1
            
    # print(flags)

    # 0은 없다니까 삭제해주자
    if 0 in flags.keys():
        del flags[0]

    for key, val in flags.items():
        print(val)