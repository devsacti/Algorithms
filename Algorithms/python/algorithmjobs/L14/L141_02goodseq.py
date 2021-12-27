import sys
'''
hint 영상 요약
7번째까지는 최소값들간의 패턴이 있는듯하지만 8번째부터 깨짐
=>칸별로 완전탐색; 백트래킹

'''

def isPossilbe(x, length):
    # result[x] 가 오른쪽 끝, 길이가 length의 중복이 있는지 판별
    # 중복이 없다면 true 아니면 false

    # unit별 비교해야할 위치의 1자리씩 비교하는 과정;
    # 123 
    # 654 
    # 3과 4, 2와 5, 1과 6

    # 한번이라도 같은 위치의 수가 다르다? ->한번이라도 if 조건 충족과 실행 -> 좋은 수열
    # 한번도 그렇지 못하다 -> 한번도 if 불충족과 미실행> 나쁜 수열
    # 321
    # 421
    # 1과 1, if 미실행
    # 2와 2, if 미실행
    # 3과 4, if 실행 true 리턴
    # 만약 마지막도 3이었다? -> 2번째 return문 실행

    for i in range(length):
        if( result[x-i] !=  result[x-i-length]):
            return True
    
    return False


def getResult( x ):
    global n,result,isFinished
    # result[x]를 결정한 후, result[x+1]를 결정해나가는 함수
    # result[x] ~ result[ n- 1]까지 결정하는 함수.

    # 1) x번째 숫자를 결정한다.
    # 2) x+1번째 숫자를 결정하러 간다. --> getResult(x+1)

    # COMPUTER INDEX 0 1 2 3 4 5 6 7 '8' at getResult(8)
    # val            1 2 1 3 1 2 3 1  ?

    # insert 1 and check the satisfiction, if ok, goto getResult(x+1)
    # insert 2 and same

    # how to check? if ? is 1

    # unit 1 ; 1 2
    # unit 2 ; 23 12
    # unit 3 ; 312 312 
    if(isFinished): return

    if(x>=n):
        for i in range(n):
            print(result[i],end='')

        isFinished=True
        return

    for num in [1,2,3]:
        result[x]=num

        # '나쁜 수열 이냐 아니냐'에 대한 flag로
        # 나쁜 수열이면 true, 안 나쁜 수열이면 false
        flag=False
        # j means unit
        for j in range(1,int((x+1)/2)+1 ):
            if(isPossilbe(x,j)==False):
                # wrong flag
                flag=True
                break
        if(flag == False):
            getResult(x+1)

if __name__=="__main__":
    global n, result, isFinished

    n= int(sys.stdin.readline().strip())
    result=[[0] for _ in range(100)]
    isFinished=False

    getResult(0)