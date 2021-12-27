'''
1. greedy flag
step1 input
make total matrix from coordinates of rectangular

step2 by using flag make field per rectangular
for for-> 0 to 1~N(flag1~flagN)

step3 count the flag per rectangular
'''

'''
여기 예제와는 본질이 전혀다른 행렬 뒤집기이지만 
파이썬 응용차원에서 중요한 코딩

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
'''

if __name__ == '__main__':
    N=int(input())

    rectangulars=[]

    for i in range(N):
        rectangulars.append(list(map(int, input().split())))

    #print(rectangulars)

    source_matrix=list(map(list,zip(*rectangulars)))

    min_x=min(source_matrix[0])
    min_y=min(source_matrix[1])

    #주어진 것이 dx,dy이지 위치벡터가 아니므로 max()만으로 max_x는 못구함
    # 처음 input받을 때 전처리 겸 정보 생성하거나 
    # 현재 단계에서 추가연산으로 구하거나
    # 실전에 맞추자면 후자, 완벽함 보단 느슨하지만 빈틈은 없는

    #flag1~N
    flags=[flag+1 for flag in range(N)]

    idx_flag=0

    for rect in rectangulars:
        rect.append(rect[0]+rect[2]-1)
        rect.append(rect[1]+rect[3]-1)
        rect.append(flags[idx_flag])
        idx_flag+=1

    #print(rectangulars)

    source_matrix=list(map(list,zip(*rectangulars)))

    max_x=max(source_matrix[4])
    max_y=max(source_matrix[5])

    #이제보니까, min xy는 필요가 없었다. matrix를 그림에있어서. 하지만
    #이런 시행착오야 말로 코딩테스트 실전과정이라 볼수 있으므로 남김

    '''
    아래와 같은 용법의 경우 앞이 col 뒤가 row이다. 의식적으로 x y이지만 유의
    그간 아마 정사각형꼴이었던 지라 운좋게 피해간듯
    '''
    # matrix=[[0]*(max_x+1) for i in range((max_y+1))]
    matrix=[[0]*(max_y+1) for i in range((max_x+1))]
    #print(*matrix, sep='\n')

    for x in range(max_x+1):
        for y in range(max_y+1):
            #print('(',x,y,matrix[x][y],')', end=' ')
            for rect in rectangulars:
                if(x >= rect[0] and x<=rect[4] and y >= rect[1] and y<=rect[5]):
                    #print('(',x,y,')', end=' ')
                    matrix[x][y]=rect[6]

        #print()

    #print(*matrix, sep='\n')

    '''step3'''

    # 지금은 완벽함 보단 느슨하되 빈틈없이!
    # 아래 코딩은 위 부분과 유사하다는 점에서 융합가능
    # 근데 값을 갱신하다보면 경험적으로 어디선가 예상치 못한 영향 발생

    dict_flags={flag:0 for flag in flags}

    for x in range(max_x+1):
        for y in range(max_y+1):
            if(matrix[x][y] in dict_flags.keys()):
                dict_flags[matrix[x][y]]+=1

    #print(dict_flags)
    #{1: 64, 2: 36}

    for val in dict_flags.values():
        print(val)










