# 연속 부분 최대합 L => Largest sum of continuous subarray
# dp with 'two pointer'

# 막연히 '모든 경우'에 대해서 생각하는 것이 아니라,
# 2개의 포인터로 모든 경우를 '하위 구간'을 분할하여 문제 해결

# 더 정확히는 2번째 포인터가 가리키는 '끝'지점을
# '기준'으로서 활용함으로서 dp의 영역으로 들어간다고 이해하였다.

# 이렇게 되돌아보면 참 간단하지만, 암기가 아닌 이해이자 기록까지 매우힘들고,
# 이를 바탕으로 더 확장시키려니 까마득하다. 힘내자 내일의 나야

import sys
input=sys.stdin.readline

def dp(nums):
    length=len(nums)
    dptable=[0]*length

    for idx in range(length):
        if(idx==0):
            dptable[idx]=nums[0]
        else:
            dptable[idx]=max(nums[idx],dptable[idx-1]+nums[idx])

    # print(dptable)
    print(max(dptable))

if __name__=="__main__":
    n=int(input().strip())
    nums=list(map(int,input().split()))

    dp(nums)