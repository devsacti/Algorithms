# 요약
## 선별적 브루트 포스와 문자열 비교
## 시간복잡도 : O(n^(3/2))


# 문제풀이 1~3단계 ; 정확한 해석 >> 알고리즘 활용 및 통합 >> 구현
## 1단계 : 정확한 문제 해석
## n 은 1 이상 1000 이하, 홀짝 모두 포함
## 짜르는 단위는 n
## 문자열은 소문자만

## !! 패턴의 길이보단 되도록이면 작은 단위이되, 그 반복이 많을 수록 효과적 !!
## 가령 (인식을 위해 띄어씀) ab ab ab ab ab ab 에서
## 패턴 길이를 크게 잡으면 최적값에 어느정도 도달하지만 ; 3ababab
## 패턴의 길이를 작게 잡을 때 6ab일때 가장 짧다.(1은 제외)

## 2-1 단계 : 해석에 알고리즘을 활용
## 현재로써는 짜르는 단위_unit_과 패턴의 길이 사이에 정확한 비례성이 판단안됨 >> 모든 unit 체크
## 단, 1~n 모든 unit이 문자열을 나누는 기준이 될 수 없다
 
## !! 왜냐하면 우리가 반복되는 '같은 unit'을 판단함은
## 수학적으로 볼 때, '동일한' 것이고, 컴퓨터 변수상 그것은 자료형과 길이로 정의할 수 있기 때문이다
# 그러므로 1~n 중 n의 약수만 탐색한 뒤 문자열을 비교한다.

## 문자열의 같다는 파이썬 기본기능을 활용 ex 'abc'=='abc'

## 2-2 단계 : 통합 및 시간복잡도 계산

## part 1 
## 선별 브루트포스와 문자열 같다 비교
## unit을 1~n 모두 다 살피지 않고, 현재 문자열 길이상, 약수로서 단위화가능한 unit만 선별
## 로직상 O(n^(1/2))
## 문자열 비교란 길이가 k로 동일한 문자열이 있을 시, 0~k-1인덱스로 각 자릿수를 판정하는과정이므로
## O(n)

## O(n^(1/2)) x O(n) >> O(n^(3/2))

## 3 단계 구현
# for preventing human error
from string import ascii_lowercase

def get_divisor(n):
    n = int(n)
    # n이 10이고 약수가 2_div_이면 자동으로 5_corre_div_도 약수
    divs = []
    cor_divs = [] 

    # 약수의 정의상 n의 제곱근까지 살펴보면 된다.
    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            divs.append(i)
            if (i != (n // i)): 
                cor_divs.append(n//i)

    return divs + cor_divs[::-1]

if __name__=="__main__":
    # 조건에 맞게 테스트 케이스가 입력되는 것이 정석이지만,
    # 조건 이상의 상황인 휴먼 에러를 대비하여 try except
    # !! 이러한 휴먼 에러는 조건 상황 이상의 것이므로 시간복잡도서 제외 !!
    
    # 그래도 계산은 해두자면
    ## 파이썬의 경우 in 이 내장함수라 다소 시간복잡도 산출이 불명확하나
    ## 정렬된 ascii_lowercase에 이진 탐색이 적용된것이라면,
    ## n x logn ; n은 문자열의 길이, 그리고 이 문자열의 item마다의 탐색
    ## 아니라면, n x n

    try :
        givenstr=input()

        for item in givenstr:
            if(item not in ascii_lowercase):
                raise Exception("소문자 알파벳만 넣으세요")

    except Exception as e:
        print("입력값 조건 불충족!", e)

    else:
        # 최악의 경우 unit이 1 일 때 혹은 패턴을 자기 자신을 잡을때이다
        # 이런 특징을 result와 len result 초기화에 활용하고
        # 탐색 중 찾는 최소값으로 갱신
        result=givenstr
        len_result=len(givenstr)
        
        # 논리적 명확함을 위해 len_given 별도로 선언
        len_given=len(givenstr)
        candis_unit=get_divisor(len_given)

        # unit이 1 인 경우 혹은 len_given 인 경우의 압축 문자열 길이는 이미 result에 초기화 된 상태이므로 그 다음부터
        for unit in candis_unit[1:-1]:
            # 새로운 unit 길이로 정렬된 문자열
            rearranged_given=[givenstr[i:i+unit] for i in range(0,len_given,unit)]
            # print(rearranged_given)

            # 반복되는 것을 효과적으로 카운트하기 위한 stack
            # 비교를 위해 rearranged의 첫번째를 넣어둔다.
            stack=[rearranged_given[0]]
            # 최종 압축 문자열
            compressed=''
            # 첫번째값은 이미 스택에 넣어놨으므로 1부터 시작
            for i in range(1,len_given//unit):
                # 스택의 top val는 stack[-1]
                # 현재 아이템과 탑을 비교해서 같으면 push, 다르면 pop하고 후속처리
                if(rearranged_given[i]==stack[-1]):
                    stack.append(rearranged_given[i])
                else:
                    cnt_repeat=len(stack)
                    if(cnt_repeat==1):
                        compressed+=stack[-1]
                    else:
                        compressed+=str(len(stack))+stack[-1]
                    # 반복이 깨졌으므로 새로운 stack[0]이자 top
                    stack=[]
                    stack.append(rearranged_given[i])
            
            # 마지막에 도달 시 스택에 비워줌으로서 완성
            cnt_repeat=len(stack)
            if(cnt_repeat==1):
                compressed+=stack[-1]
            else:
                compressed+=str(len(stack))+stack[-1]
            stack=[]

            # print(compressed)
            # 현재 압축한 문자열의 길이와 기준 문자열 비교 시, 전자가 더 짧다면 갱신
            len_cur=len(compressed)
            if(len_cur<len_result):
                len_result=len_cur
                result=compressed
        
        print(result)