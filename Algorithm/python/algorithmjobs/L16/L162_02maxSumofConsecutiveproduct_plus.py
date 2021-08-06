# 연속 부분 최대'곱'
# 오전 11:45 2021-05-21
# core content; 카데인 알고리즘(kadane's algorithm)의 응용
# steps of main
import sys
input=sys.stdin.readline

def dp(nums):
    length=len(nums)
    dptable=[0]*length
    minusdptable=[0]*length

    for idx in range(length):
        if(idx==0):
            dptable[idx]=nums[0]
            minusdptable[idx]=nums[0]
        else:
            # basic kadane's algorithms
            dptable[idx]=max(dptable[idx-1]*nums[idx],nums[idx])
            # expansion part of kadene
            if(abs(minusdptable[idx-1]*nums[idx])>abs(nums[idx])):
                minusdptable[idx]=minusdptable[idx-1]*nums[idx]
            else:
                minusdptable[idx]=nums[idx]

            dptable[idx]=max(minusdptable[idx-1]*nums[idx],nums[idx])

    # print(dptable)
    # print(minusdptable)
    print(max(dptable))

if __name__=="__main__":

    nums=list(map(int,input().split()))
    print(nums)
    dp(nums)