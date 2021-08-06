import sys

#  동적 계획이란?
#  부분 문제들을 모아서 전체의 문제를 해결
#  ?. 단순히 분할 정복의 확장?
#  분할 정복은 기본적으로 탑다운 방식, dp는 다운탑방식, 공통적으로 '분석'이란 개념 존재

#  스텝
#  1~2.전체와 부분 문제를 정의 점화식 설정
#    이때, 선행 부분은 풀렸다고_현 코드가 이렇게 작동한다는 전제가 공리_ 가정하고 코드
#    또한, 초항 같은 기저조건을 정의하거나 구한다.
#  3. 문제해결=코드화, 코드화 시 위의 전제는 배열 속에 이전값을 작업 중 구해서 따로 저장함으로서 구현

# 가령, 피보나치 문제의 경우
# 1  전체 관점의 문제 F(i) = F_i의 값을 구하는것,
# |  부분 관점의 문제  F_i-1에서 F_i를 도출
# 2. F_5를 구할 때 F_1~4는 주어진다. -> F_i = F_i-1 + F_i-2
# 3. 문제를 해결하다.(코드화)

# 가령, 블럭 채우기의 경우
# 1  F(i)_특정 규격의 블럭을 통해서 주어진 공간을 채우는 방법의 수_을 구한다.
# |  F_i-1 이 주어졌다는 가정하에 거기서 특정규격의 블럭을 잘이어붙여서 F_i가 된다.
# 2  F_i = F_i-1 +F_i-2
# 3.  


# 아래 형태는 dp같은 재귀구조일뿐이다. 왜냐하면 데이터의 누적이 전혀없이
# 매번 하위계산이 '반복'되고 타임 리밋 오버가 뜬다.
def Nodp_JustRecursive(n):
    data=[]
    if(n==1 or n==2 or n==3):
        return data[n-1]
    else:
        result=Nodp_JustRecursive(n-1)+Nodp_JustRecursive(n-2)+Nodp_JustRecursive(n-3)
        # 여러번 작동 시에는 아래와같이 데이터가 축적되야
        # data[n-1]=tmp
        result=result%1000007
        return result

# 재귀구조를 써서 n-1번째 인덱스의 값이 산출되면 리턴해주는 형태로 짤수있지만,
# 그러한 개념을 안다면 굳이 코드가 짧지도 않고, 덜 안정된 재귀보단 아래처럼
# 폴문으로 커버 
def safedp(n):
    global results
    idx_results=n-1

    if(idx_results<3):
        return results[idx_results]
    else:
        # 4 1 0
        # 5 2 0 1
        for i in range(idx_results-2):
            results.append((results[-1]+results[-2]+results[-3])%1000007)
        
        return (results[-1])

if __name__=="__main__":
    n = int(input())
    global results
    
    # 1~2
    # an = a_n-1 + a_n-2 + a_n-3
    results=[]
    # 1 =1
    # 2 = 1+1 or 2
    # 3 = 1+1+1 or 2+1 or 1+2 or 3
    a1=1
    a2=2
    a3=4
    tmp=[a1,a2,a3]
    results.extend(tmp)

    print(safedp(n))