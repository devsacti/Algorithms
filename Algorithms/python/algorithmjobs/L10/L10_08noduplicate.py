'''
step1
 로직 생각, 참고로 완벽세련보단 느슨근사 그러나 빈틈없이
 변수 받기
 필요변수 만들기 ex list_parameters 또는 start, end

step2
 필요 함수 구현

 +
 if __name__=="__main__":
        n=int(input())
    seqs=list(map(int, input().split()))

    #list_parameters=[i+1 for i in range(n)]

    start_dx=1
    end_dx=n

    while(end_dx-start_dx>=0):
        mid_dx=int( (end_dx+start_dx)/2 )
        # print('mid_dx',mid_dx)

        #checking seqs

        for i in range(n-mid_dx+1):
            # print(i, mid_dx,n-mid_dx)
            sample=seqs[i:(i+mid_dx)]
            # print(sample)

            if(len(set(sample))==len(sample)):
                token_result=1
                break
            else:
                token_result=0
        
        if(token_result==1):
            result=mid_dx
            start_dx=mid_dx+1
        else:
            end_dx=mid_dx-1
    
    print(result)

일케 했는데 80점 나오고 타임리밋 넘음 아마도 사실상 2중폴문(forNsplice이 문제인듯)
인줄 알았는데

내장함수 set이 너무 무거웠나봐, NN단표도 sorted로 커버안된거처럼

+추가설명 보고, 다른 내장함수로 해봤는데, 아무래도 C의 경우 sample을 만들면서
필요한 작업이 되지만, 파이썬의 내장함수를 쓸경우 다 포장했다가 풀어헤치는 작업이
껴서 더 느려짐 65점나옴

if __name__=="__main__":
    n=int(input())
    seqs=list(map(int, input().split()))

    #list_parameters=[i+1 for i in range(n)]

    start_dx=1
    end_dx=n

    while(end_dx-start_dx>=0):
        mid_dx=int( (end_dx+start_dx)/2 )
        # print('mid_dx',mid_dx)

        #checking seqs

        for i in range(n-mid_dx+1):
            # print(i, mid_dx,n-mid_dx)
            sample=seqs[i:(i+mid_dx)]
            # print(sample)

            dict_sample={element:sample.count(element) for element in sample}

            # print(dict_sample)

            cnt_2=0
            for val in dict_sample.values():
                if(val>=2):
                    cnt_2+=1

            if(cnt_2==0):
                token_result=1
                break
            else:
                token_result=0
        
        if(token_result==1):
            result=mid_dx
            start_dx=mid_dx+1
        else:
            end_dx=mid_dx-1
    
    print(result)

+
아래 코드 바탕으로 겨우겨우 타임리밋안에는 들어왔는데,
지금보니까 예시에 한정되서 
14
1 2 3 4 4 7 2 1 5 1 11 12 13 14
같이 과정 중에서 1이 들어오고 1이 나갈때 생기는 문제 커버 못함

if __name__=="__main__":
    n=int(input())
    seqs=list(map(int, input().split()))

    #list_parameters=[i+1 for i in range(n)]

    start_dx=1
    end_dx=n

    while(end_dx-start_dx>=0):
        mid_dx=int( (end_dx+start_dx)/2 )
        print('mid_dx',mid_dx)

        #checking seqs
        test_list=[0]*n
        subidx=0
        cnt_2=0

        #seqs에 대해서 유닛별로 체킹
        while((subidx)+(mid_dx-1)<=(n-1)):
            print('sample',seqs[subidx:subidx+(mid_dx-1)+1])
            
            if(subidx==0):
                for i in range(subidx, subidx+(mid_dx-1)+1):
                    print('#subidx',subidx,subidx+mid_dx)
                    print('#i',i, test_list)

                    test_list[seqs[i]-1]+=1
                    print('#val',seqs[i],'\nidxfortestlist',seqs[i]-1, test_list)

                    if(test_list[seqs[i]-1]>=2):
                        cnt_2+=1
                    print()
            else:
                print('subidx post new ',subidx,seqs[subidx-1] ,seqs[subidx+(mid_dx-1)])
                print(test_list)
                print('cnt_2', cnt_2)

                test_list[seqs[subidx-1]-1]-=1
                print(test_list)

                if(test_list[seqs[subidx-1]-1]==1):
                    cnt_2-=1
                else:
                    pass

                print('cnt_2', cnt_2)
                
                test_list[seqs[subidx+(mid_dx-1)]-1]+=1
                print(test_list)

                #느낌상 여기서 시간 다 잡아먹는듯
                #cnt_2=test_list.count(2)


                if(test_list[seqs[subidx+(mid_dx-1)]-1]==2):
                    cnt_2+=1
                else:
                    pass

                # print('cnt_2', cnt_2)

            subidx+=1
        
            if(cnt_2==0):
                token_result=1
                break
            else:
                token_result=0


        if(token_result==1):
            result=mid_dx
            start_dx=mid_dx+1
        else:
            end_dx=mid_dx-1
    
    print(result)

위가 95점

+마지막 5점을 찾아보자
'''

if __name__=="__main__":
    n=int(input())
    seqs=list(map(int, input().split()))

    #list_parameters=[i+1 for i in range(n)]

    start_dx=1
    end_dx=n

    while(end_dx-start_dx>=0):
        mid_dx=int( (end_dx+start_dx)/2 )
        # print('mid_dx',mid_dx)

        #checking seqs
        test_list=[0]*n
        subidx=0
        cnt_2=0

        #seqs에 대해서 유닛별로 체킹
        while((subidx)+(mid_dx-1)<=(n-1)):
            # print('sample',seqs[subidx:subidx+(mid_dx-1)+1])
            
            if(subidx==0):
                for i in range(subidx, subidx+(mid_dx-1)+1):
                    # print('#subidx',subidx,subidx+mid_dx)
                    # print('#i',i, test_list)

                    test_list[seqs[i]-1]+=1
                    # print('#val',seqs[i],'\nidxfortestlist',seqs[i]-1, test_list)

                    if(test_list[seqs[i]-1]==2):
                        cnt_2+=1
                    # print()
            else:
                # print('subidx post new ',subidx,seqs[subidx-1] ,seqs[subidx+(mid_dx-1)])
                # print(test_list)
                # print('cnt_2', cnt_2, end=' ')

                test_list[seqs[subidx-1]-1]-=1
                # print(test_list)

                if(test_list[seqs[subidx-1]-1]==1):
                    cnt_2-=1
                else:
                    pass

                # print('cnt_2', cnt_2, end=' ')
                
                test_list[seqs[subidx+(mid_dx-1)]-1]+=1
                # print(test_list)

                if(test_list[seqs[subidx+(mid_dx-1)]-1]==2):
                    cnt_2+=1
                else:
                    pass

                # print('cnt_2', cnt_2, end='  ')

            subidx+=1
        
            if(cnt_2==0):
                token_result=1
                break
            else:
                token_result=0


        if(token_result==1):
            result=mid_dx
            start_dx=mid_dx+1
        else:
            end_dx=mid_dx-1
    
    print(result)