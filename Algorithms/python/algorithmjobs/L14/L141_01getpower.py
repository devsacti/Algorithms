# 거듭제곱 구하기 L

import sys
'''
python에서 int란 정수긴 하지만 애당초 메카니즘이 부동소수점이라서 근사정수이다.
따라서, 매우 큰 실수에서 소수점을 버리고자 한다면 //1로 규정해야한다.

정확한 스텝을 원하면 // 를 쓰자.
'''
# muliple 구현 기본 메카니즘; 2*100에서 100번 곱하지 말고, 2*50의 제곱, 2*25의 제곱 등등으로 다운
# mod 개념? 없고, 위 과정을 재귀적으로 해석해서 코드화

# 2의 4승, 5승부터 생각해보자.
# 거슬러가다보니, 0승과 1승의 문제 발생
# 1승은 

def getroot(base, exponent, result):
    # 상위 재귀구조 상,'이론상' 1에 대해 -1 후 exponent가 0이 되는 경우 커버해야
    # 물론 홀수더라도 -1해서 짝수가 되고 짝수로 쪼개지다가 지수가 도달하는 곳은 1이라
    # 작동은 안할듯함

    # print('#',base, exponent, result)
    if(exponent%2 == 0):
        if( exponent == 0):
            result = 1
        else:
            val_root=getroot(base,(exponent//2),result)
            result=(val_root)**2
            result=result%10007

    elif(exponent%2 == 1):
        if( exponent==1 ):
            result = base
        else:
            val_root=getroot(base,(exponent-1)//2,result) 
            result= base*(val_root**2)
            result=result%10007

    # print('##',base, exponent, result)
    
    return result

if __name__=="__main__":

    base, exponent = map(int, sys.stdin.readline().split())
    result=0
    result=getroot(base,exponent,result)

    print(result)