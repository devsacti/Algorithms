# 거듭제곱 구하기 L
import sys

'''오류 못찾겠어서 그냥 힌트영상 복사'''

# print(800000000000000000000000000/2)
# print(int(800000000000000000000000000/2))
# print(800000000000000000000000000//2)

# 소수점 버릴때는 // 필수, int는 문자열 을 변환할때만 써라

def getresult(n, m):
    if(m ==0): return 1
    else:
        if(m % 2 == 0):
            temp = getresult(n, (m//2))
            return (temp*temp) % 10007
        else:
            temp = getresult(n, m-1)
            return (temp*n) % 10007

if __name__=="__main__":

    n, m = map(int, sys.stdin.readline().split())
    print(getresult(n, m))