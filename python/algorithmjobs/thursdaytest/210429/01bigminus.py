# 큰자릿수 뺄셈
# 오후 5:45 2021-04-29
# 핵심; 
# 파이썬은 부족하면 메모리를 더 끌어와서 최종적으론오버플로우가 없지만,
# 별도로 int로 소수점쳐낼 때 추가메모리를 불러오는 과정 중의 문제로 오차 발생해 보임
# 일단 여기선 그범위까진 안감

import sys

if __name__=="__main__":
    n1=int(sys.stdin.readline().strip())
    n2=int(sys.stdin.readline().strip())

    print(n1-n2)