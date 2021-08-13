# 요약
## dynamic programming with memozation 과 피보나치, 그리고 선형 디오판토스 방정식
## 시간복잡도 : O(n)


# 문제풀이 1~3단계 ; 정확한 해석 >> 알고리즘 활용 및 통합 >> 구현

## 1단계 : 정확한 문제 해석
## N,K 는 정수, 그리고 N 은 3 이상
## K 가 피보나치 규칙 관점에서 분석되야할 대상
## N 은 위와같은 규칙 상에서 K의 순서
## 조건에 부합하는 a,b 1쌍만 구하면됨.

## !! 피보나치 규칙에 근거해서 해석하자면 !!
## K 란 'p * a + q * b'로 분석가능 하고, and p, q 를 N과 관련시켜서 이해할 수 있음
## 가령 N 이 3으로 주어지면, 피보나치 규칙상 K 는 p=1, q=1  일 때 'p * a + q * b'임(즉, a+b)
## 가령 N 이 4로 주어지면, K는 p=1,q=2 일때 'p * a + q * b'임(즉, a+2b)
## 가령 N 이 5로 주어지면, K는 p=2,q=3 일때 'p * a + q * b'임(즉, 2a+3b)

## 2-1 단계 : 해석에 알고리즘을 활용
## dp table과 메모제이션을 활용하면

## index       0  1  2  3  4  5  6 ... N
## a dp table  *  1  0  1  1  2  3 ... p
## b dp table  *  0  1  1  2  3  5 ... q
## sum of p,q  *  A  B  C  D  E  F ... K

## 문제 조건과의 조화를 위해 0번째는 쓰지 않고,
## A = 1*a + 0*b
## B = 0*a + 1*b
## C = 1*a + 1*b
## D = 1*a + 2*b
## E = 2*b + 3*b
## ...
## K = p*a + q*b
## p, q는 다이너믹 프로그래밍과 메모제이션을 통해 상수로서 도출가능

## 만약 p,q가 5,8일때, K = 5*a + 8*b
## 이를 충족하는 정수해 a,b를 구하는 것은 디오판토스(or 디오판틴) 방정식 문제이다
## (혼란을 피하기 위해 미지수를 통일하자면, p * a + q * b = c)

## 그리고, 이 방정식의 일반해는 특수해를 기반으로 정의되는데,
## 가령 x=x0+ (q/d) * t, y=y0+ (p/d) * t ; x0,y0는 방정식의 특수해, d is gcd of p,q
## 이 특수해를 구하는 과정은 유클리드 호제법을 역순으로 적용하는 과정이다.
## 따라서 브루트포스하게 '정수 a,b'를 구하면 리턴하고 종료

## 2-2 단계 : 통합 및 시간복잡도 계산
## part 1
## N 번째까지 플러스 연산하면 되서 시간복잡도는 O(n)

## part 2
## 그 다음이나, 독립적으로 디오판토스 방정식의 시간복잡도는 O(n)
## 그러나 gcd가 1 인경우, 일반적인 방법으로 해결되지 않고, 확장법 또한 현재로썬 발견하지 못했다
## 그리하여 이 경우에 대해서 'a,b가 모두 양수인 경우에 한정하고' 이렇게 되면 시간복잡도는 O(k/p)이다. pa+qb=K의 절편이다.

## O(n)+O(n) >> O(n)

## 한편, dp table은 recursive하게도 구현가능하나, 시간복잡도가 급증하므로 차선
## 그리고 피보나치 수열에 대한 특성방정식 조건도 활용가능은 하나, 무리수가 포함되서 근사값이라 오차 발생하므로 차선

## 3 단계 구현

# for 디오판토스
from math import fabs, gcd
## 추가로 디오판토스 방정식의 해가 존재하지 않을 시 -1을 리턴한다.

def makeDPtable(N,K):
    # dp table about p and q
    a_table=[0]*N
    b_table=[0]*N

    # 첫번째부터 시작하는 문제특성에 맞추어 1 base indexing
    a_table = ['*'] + b_table
    b_table = ['*'] + b_table
    
    # 초기값 설정
    a_table[1]=1
    b_table[2]=1

    # N이 3이상의 값으로 들어온다는 보장 하에
    # 가령, 3 이상 4 미만, 3이상 5 미만 등등
    for i in range(3,N+1):
        a_table[i]=a_table[i-1]+a_table[i-2]
        b_table[i]=b_table[i-1]+b_table[i-2]

    # print(a_table)
    # print(b_table)

    p,q=a_table[-1],b_table[-1]
    return p,q

# 출처 https://blog.yum3.ga/22
# ax+by=c 인 경우로 아규먼트설정; 우리는 pa+qb=K
def diophantine(a, b, c):
	r1, r2 = a, b
	s1, s2 = 1, 0
	t1, t2 = 0, 1
	
	while r2!=0:
		q = r1/r2
		r1, r2 = r2, r1%r2
		s1, s2 = s2, s1-q*s2
		t1, t2 = t2, t1-q*t2

	return (c/r1*s1, c/r1*t1)

if __name__=="__main__":
    # N,K에 대한 조건에 따라 테스트 케이스가 구성되는 것은 반드시 지켜져야하나
    # 문제 조건 이상의 예외사항, 즉 '휴먼 에러' 방지차원에서 아래 추가
    try :
        # 일단 파이썬에서는 3과 3.14 모두 int로 기입되서 아래로 되지만
        N,K=map(int,input().split())

        if N>=3:
            pass
        else:
            raise Exception("3이상의 N값을 입력하세요!")

    except Exception as e:
        print("입력값 조건 불충족! 소수점이 없는 정수로 입력하세요", e)

    else:
        # 최소한 입력값은 보장된 상황으로 결과값 result를 정의한다.
        p,q=makeDPtable(N,K)
        # print(p,q)
        result=0

        # K = p*a + q*b 성립, 가령 55 = 5*a + 8*b
        # 공식에 따르면, p,q의 최대공약수 d가 K의 약수가 아니라면 정수해는 존재하지 않으므로 
        # 참고로 gcd는 1도 가능하므로 K가 정수라면 성립한다,
        # 그러므로 현재 조건상 판별할 필요는 없지만 논리상 기입
        d=gcd(p,q)
        # print(d)
        
        if(K%d!=0):
            print('no answer')
        else:
            # 유클리스 호제법을 역순으로 전개하는 과정을 통해 특수해를 구한다
            # 단, gcd가 1 이면 별도의 처리 값을 처리해야됨을 확인하였다.

            # 이런 한계 극복을 위해 pa+qb=K를 좌표계로 옮기고, 벡터화해보고 했지만
            # '정수해'라는 강력한 조건은 무조건 디오판토스로 향하게 함을 확인했습니다.

            # 물론 단순히 0 부터 1씩 증가시켜 정수해쌍을 구할수도 있지만
            # 최악의 경우 평생 1씩 증가할 수 있으므로,# 부득이 한정적인 답을 설정했습니다.
            # a,b가 양수일경우

            if(d==1):
                # print('죄송하게도 gcd가 1이면 a,b가 양수라는 한정하에 답을 리턴합니다.')
                # a 절편 기준으로 구함 ; pa+qb=K >> b = (K-p*a) / q
                equal_limit=K//p

                notfindtoken=True
                for i in range(equal_limit+1):
                    a=i
                    b=((K-p*a)/q)
                    if(b%1==0):
                        print(a,int(b))
                        notfindtoken=False
                        break
                
                if(notfindtoken): print('죄송하게도 양수 내에선 답이 없습니다.')

            else:
                a,b=diophantine(p,q,K)
                print(a,b)