import string

from itertools import permutations

import sys
input=sys.stdin.readline

# variables for backtracking
global n,r
global samplespace,isused

# 여기서 isused의 의미는, 1~n의 숫자 후보가 있고 이들이 0~n-1로 인덱싱되었을 때,
# 현 result 리스트에 [2,4,미정,미정]으로 2와 4가 이미 사용된 상태라면, [False,True,False,True]이다
# 이는 recursiveBruteforce 함수의 depth가 result 인덱스 2를 가리킬때, 
# 현재까지 2와 4는 사용된 상태이고, 이들을 제외하고 result 인덱스 2를 채울라면 활용하세요. 이다.

# dfs도 결국 재귀구조로 대게 구현된다는 점에서 
# 아래 재귀구조를 9개의 노드가 모두 서로 연결된 상태에서 dfs를 돌리는 것으로 이해가능
# isused는 visited로 이해가능하고, 신가하다.

def recursiveBruteforce(depth,result,r):
    global samplespace

    if(depth>=r):
        # print(result)
        print(''.join(map(str,result)))
    else:
        for item in samplespace:
            if(item in result): continue
            else:
                result[depth]=item
                recursiveBruteforce(depth+1,result,r)
                result[depth]=0

if __name__=="__main__":
    n,r=map(int,input().split())

    source=string.ascii_lowercase
    samplespace=source[:n]
    

    depth=0
    result=[0]*r

    recursiveBruteforce(depth,result,r)