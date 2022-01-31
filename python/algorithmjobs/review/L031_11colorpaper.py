import sys
import math

# 일단 벡터 개념에 따라서 데이터들을 입력받는다
# 이러한 개념을 바탕으로 바탕평면을 만들 벡터의 시작점과 끝점을 구한다
# 평면을 만들고 잘 정돈된 벡터 개념 및 정보에 따라서 해당영역에 플래그를 세운다.
# 그리고 플래그를 센다.

if __name__=="__main__":
    N=int(sys.stdin.readline().strip())

    vectors=[]

    min_ci_r=1000;max_ci_r=-1000 
    min_ci_c=1000;max_ci_c=-1000
    for _ in range(N):
        # 일단 다는 시작점_좌표 개념_에 대해서는 기존 idx명칭을 쓰고,
        # 너비와 높이에 대해서는 length로 묶자 다만 rc 표기
        cidx_r, cidx_c, length_r, length_c = map(int, sys.stdin.readline().split())
        vectors.append( (cidx_r, cidx_c,length_r,length_c) )

        if(cidx_r<min_ci_r):
            min_ci_r=cidx_r
        
        if(cidx_r+length_r-1>max_ci_r):
            max_ci_r=cidx_r+length_r-1

        if(cidx_c<min_ci_c):
            min_ci_c=cidx_c
        '''
        자연스럽고 적절한 변수 생성이 없으니,
        cidx_c+length_c-1>max_ci_c 가 
        아니라,
        cidx_c>max_ci_c를 비교해서 엄만 오류가 발생했다.
        다음에 풀때는 매번 적절한 변수 생성에 대해서 고려하라고 냅둠
        '''
        if(cidx_c+length_c-1>max_ci_c):
            max_ci_c=cidx_c+length_c-1

    # print(vectors)
    # print(min_ci_r,max_ci_r)
    # print(min_ci_c,max_ci_c)

    # 맨 왼쪽 위 좌표와 맨오른쪽 아래 좌표 구하기
    # 원점으로부터의 거리고 판단 WRONG !!
    # 운좋게 첫번째는 기존 색종이 위에 다음 색종이가 올라가는 형태라 맞았지만
    # 기본적으로 지금 만들어야하는건 모든 색종이가 올라갈수있는 바탕이기 때문에
    # 그냥 최소 r과 최소 c을 구해야한다. 그림1만봐도 원점으로부터의 거리방식은
    # 문제가 생긴다.
    '''
    accuracy 부족 시 생기는 뻘짓이 아래 코드 _ start
    '''
    # min_magnitude_startpoint= 1000
    # min_coordinate= (1,1)
    # max_magnitude_endpoint= -1000
    # max_coordinate= (1,1)

    # for vector in vectors:
    #     cidx_r, cidx_c, length_r, length_c = vector
    #     dr=length_r-1
    #     dc=length_c-1
        
    #     mag_startpoint_vector=math.sqrt( cidx_r**2+cidx_c**2 )
    #     mag_endpoint_vector=math.sqrt( (cidx_r+dr)**2+(cidx_c+dc)**2 )

    #     print(vector, mag_startpoint_vector,mag_endpoint_vector)

    #     if(mag_startpoint_vector<min_magnitude_startpoint):
    #         min_coordinate=(cidx_r,cidx_c)
    #         min_magnitude_startpoint=mag_startpoint_vector

    #     if(mag_endpoint_vector>max_magnitude_endpoint):
    #         max_coordinate=(cidx_r+dr,cidx_c+dc)
    #         max_magnitude_endpoint=mag_endpoint_vector
    
    # print(min_coordinate, max_coordinate)



    # 전체 평면 그리기
    # !!! idx-idx는 interval로 아래 계산은 1칸씩 타협하게 되니까 끝나고 +1을하든
    # idx의 의미를 살려서 리스트 컴프리헨션
    # r=max_coordinate[0]-min_coordinate[0]
    # c=max_coordinate[1]-min_coordinate[1]

    # matrix=[[0]*c for _ in range(r)]
    
    # 아쉽게 도 혼합됨.
    # matrix=[[0]*(max_coordinate[1]-min_coordinate[1]+1) for _ in range(min_coordinate[0],max_coordinate+1)]

    # # 그냥 표기를 명확히하고 +1
    # length_r=max_coordinate[0]-min_coordinate[0]+1
    # length_c=max_coordinate[1]-min_coordinate[1]+1
    # matrix=[[0]*length_c for _ in range(length_r)]

    # print(*matrix, sep='\n')


    '''
    accuracy 부족 시 생기는 뻘짓이 위 코드 _ end
    '''
    length_r=max_ci_r-min_ci_r+1
    length_c=max_ci_c-min_ci_c+1
    matrix=[[0]*length_c for _ in range(length_r)]
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

    for ci_r in range(length_r):
        for ci_c in range(length_c):
            if(matrix[ci_r][ci_c] in flags.keys()):
                flags[matrix[ci_r][ci_c]]+=1
            
    # print(flags)

    # 0은 없다니까 삭제해주자
    if 0 in flags.keys():
        del flags[0]

    for key, val in flags.items():
        print(val)