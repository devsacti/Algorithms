'''
step1 input, transposed, revered

step2 count 0 num 

step2.1 best place and points

'''

if __name__=='__main__':
    C,R=map(int, input().split())

    matrix=[]

    for i in range(R):
        matrix.append(list(map(int,input().split())))

    #print(*matrix,sep='\n')

    transposed_matrix=[list(item) for item in zip(*matrix)]
    #print(*transposed_matrix,sep='\n')
    # [0, 0, 1, 1, 1, 1, 1]
    # [0, 0, 1, 1, 1, 1, 1]
    # [0, 0, 1, 1, 1, 1, 1]
    # [0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 1, 1, 1]
    # [0, 0, 1, 1, 1, 1, 1]

    reversed_transposed_matrix=[list(reversed(item)) for item in transposed_matrix]

    #print(*reversed_transposed_matrix,sep='\n')
    # [1, 1, 1, 1, 1, 0, 0]
    # [1, 1, 1, 1, 1, 0, 0]
    # [1, 1, 1, 1, 1, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0]
    # [1, 1, 1, 0, 0, 0, 0]
    # [1, 1, 1, 1, 1, 0, 0]

    '''step2~2.1'''
    #print(id(reversed_transposed_matrix))
    scenarios=[]

    len_rstd=len(transposed_matrix)
    len_cstd=len(transposed_matrix[0])

    temp=[[0]*len_cstd for i in range(len_rstd)]
    cnt_zeros=0
    gameover=0

    for n in range(len_rstd):
        column=n+1
        #deep copy, 위 n과 완전 별개로 여겨야한다. 변수선언 수준
        for i in range(len_rstd):
            temp[i]=transposed_matrix[i][:]

        #print(id(temp))

        #행 분석
        block=[1,1,1,1]
        len_block=len(block)
        cnt_zeros=0
        gameover=0

        for element in temp[n]:
            if(element==0):
                cnt_zeros+=1
            else: 
                break

        if(cnt_zeros<len_block):
            gameover+=1
        else:#0 : 4개이상 '위에서'
            if 1 in temp[n]:
                idx_one=temp[n].index(1)
                temp[n][idx_one-4:idx_one]=block
            else:
                temp[n][-1:-5:-1]=block

        #print(*temp, sep='\n')

        '''step2.1'''
        transposed_temp=[list(item) for item in zip(*temp)]

        point=0

        #테트리스 득점 판단
        for row in transposed_temp:
            if 0 not in row:
                point+=1
            else:
                continue

        #plus condition about point and game over
        if(point==0 or gameover==len_rstd):
            column=0;point=0
        else:
            pass

        scenarios.append([column,point])
        # print(scenarios)
        # print()

    #deep copy check
    #print(*reversed_transposed_matrix[:],sep='\n')

    scenarios_sorted=sorted(scenarios,key=lambda x:x[1],reverse=True)
    #print(scenarios_sorted[0])
    column, max_point=scenarios_sorted[0]

    print(column, max_point)