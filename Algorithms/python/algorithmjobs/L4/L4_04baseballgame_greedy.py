if __name__=='__main__':

    N=int(input())

    scoresources=[]
    for i in range(N):
        scoresources.append(list(map(int,input().split())))

    #print(scoresources)
    std_correct=len(scoresources)

    #strike 내림차순으로 시행들 정렬
    scoresources=sorted(scoresources, key=lambda x: x[1], reverse=True)
    #print(scoresources)

    #표본공간
    samplespace=[i for i in range(1,10)]

    '''step2'''
    if(scoresources[0][1]==3):
        print(1)
    else:
        totalcases=[[i,j,k] for i in samplespace for j in samplespace if(j!=i) for k in samplespace if (k !=i and k!=j)]
        # print(len(totalcases))
        # print(totalcases[0:10])
        # [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 1, 4], [1, 1, 5], [1, 1, 6], [1, 1, 7], [1, 1, 8], [1, 1, 9], [1, 2, 1]]
        
        candidatecases=[]

        for case in totalcases:
            correct=0
            #모든 경우의 수들_9*8*7_에서 1개 빼서 그게 조건들을 통과하는지 확인하는 스텝
            for scoresource in scoresources:
                std_strike=scoresource[1]
                std_ball=scoresource[2]

                # int to list, ex 123->['1','2','3']->[1,2,3]
                condition=list(map(int,str(scoresource[0])))

                cnt_strike=0
                cnt_ball=0
                #다행히도 문제에서 서로다른 숫자라고 조건을 줌, 만약 아니라면 정답에 있지만 위치가 다른 것과, 정답에 있고 위치도 같은 것을 구분해야
                for idx1,radix_case in enumerate(case):
                    if( (radix_case in condition)):
                        if(radix_case==condition[idx1]):
                            cnt_strike+=1
                        else:
                            cnt_ball+=1
                
                if(std_strike == cnt_strike and std_ball== cnt_ball):
                    correct+=1
                else:
                    continue

                if(correct==std_correct):
                        candidatecases.append(case)

        print(len(candidatecases))