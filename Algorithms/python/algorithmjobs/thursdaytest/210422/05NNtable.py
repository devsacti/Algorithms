'''
파이썬 내장함수만으로 했는데도..메모리리밋 뜸
if __name__=='__main__':
    N=int(input())

    K=int(input())

    overall=list()

    for i in range(1,N+1):
        row=[i*j for j in range(1,N+1)]
        overall.extend(row)

    sorted_overall=sorted(overall)

    print(sorted_overall[K-1])
1. 이중배열이 너무 길거나
2. 그런 와중에 정렬만으로도 리밋 초과인듯

->필요한 부분만 선언하고 살피자
N*N 행렬 특징상 작은 값은 좌측상단부터 분포되있고(WRONG!!)
4번째는 (2,2)
9번째는 (3,3)
16번째 작은수는 (4,4)에 위치하는 특징(WRONG!!)과
sqrt를 이용해서 필요한 단만 선언

->2*2 행렬에 대해서 4번째를 물을때, 혹은 4*4행렬에서 16번째일때등, 특수한 경우임
수학적으로 n*n일때 넓이가 가장 큰 정사각형 나오듯이,
좌측상단은 최소, 우측하단은 최대 그리고 그 외는 서로 혼재해서 아래처럼 못품

    previous_row=int(math.sqrt(K))

    differ=K-previous_row*previous_row

    if(differ==0):
        #
        print(K)
    else:
        val1=differ//2
        val2=differ%2

        val3=val1+val2
        # print(val1, val2,val3)

        critical_row=[(previous_row+1)*j for j in range(1,(previous_row+1)+1)]

        # print(critical_row)
        print(critical_row[val3-1])

+역함수 개념 활용; k번째->val를 val->k번째추론, https://daily-life-of-bsh.tistory.com/7
수학적으론 정렬하면 되는데 시간 너무 오래걸려서, 역방향

1~N*N 중 bs를 바탕으로 추출해서 그게 몇번째인지 확인하면서 이동
이때 해당 val이 몇번째인지 확인하는데는
각 행마다 배수형태로 숫자가 배치되므로 val를 그 배수단위로 나눗으로서
그 val보다 작은 게 몇개있나 확인가능

한편, 왜 1~N*N인가? 3*3행만해도 1~9가 아닌데,
생각해보니까 테이블에 없는 수여도 결과에는 괜찮긴함, 근사 개념으로서
-> 아닌듯, 테이블에 없는 수일 경우를 추가처리해야 82점에서 올라갈듯함
이와 관련하여 1~N*N과 th_mid가 1대1대응이 아닌 걸 확인,
하지만 이를 또다른 패턴으로 회피 필요
-> 현재 구조상 4, 5, 6 ,7 모두 tmp_k로 연결될수 있다, 테이블안에 없는 값도 있으니
-> 이런 현재의 구조적 오류 위에서 답을 찾기 위해선 경계까지 다가가야 하므로

        if(th_mid>=k):
            result=val_mid
            val_end=val_mid-1

같더라도, break하지 말고 while을 돌려서 범위가 2개->1개로 줄때까지 가야한다.

'''

'''
만약 break을 넣는다면 아래 checkintable로도 문제해결 가능하지만
매우 복잡
'''
def checkintable(result, root_end):
    if(result<=root_end):
        result2=result
        return result2
    else:
        testresults=[(result%i) for i in range(2,root_end+1)]

        if(0 in testresults):
            result2=result
            return result2
        else:
            result2=result-1
            return result2


def bs(start, root_end,k):
    val_start=start
    val_end=root_end*root_end

    while(val_end-val_start>=0):
        # print('start~end',val_start,val_end)
        val_mid=int( (val_start+val_end)/2 )
        # print('#val_mid',val_mid)

        ##calcul order for comparing k
        subsets=[int(val_mid//(i)) for i in range(1,root_end+1)]
        processed_subsets=[root_end if element>root_end else element for element in subsets]
        # print(processed_candidates)
        th_mid=sum(processed_subsets)
        # print('th_mid',th_mid)

        if(th_mid>=k):
            result=val_mid
            val_end=val_mid-1
        elif(th_mid<k):
            #result=th_mid를 할수는 있는데 그러면 추가적으로 처리 요구
            val_start=val_mid+1
        else:
            pass

    print(result)
    # result2=checkintable(result,root_end)
    # print(result2)

if __name__=='__main__':
    N=int(input())

    K=int(input())

    root_end=N

    bs(1,root_end,K)
