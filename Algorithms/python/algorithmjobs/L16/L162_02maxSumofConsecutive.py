# 연속 부분 최대합 L
# 오전 11:45 2021-05-21
# core content; dp from brute force method; 이게 카데인 알고리즘(kadane's algorithm)인듯
# steps of main
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