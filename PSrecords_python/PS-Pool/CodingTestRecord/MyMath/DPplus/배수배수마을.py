import sys
input=sys.stdin.readline

def dp(nums):
    length=len(nums)

    dptable=[0]*length

    for idx in range(length):
        if(idx==0):
            dptable[idx]=nums[idx]
        else:
            basic=1
            curitem=nums[idx]
            cost=curitem*basic

            std=dptable[idx-1]
            while(cost<std):
                basic+=1
                cost=curitem*basic
                # print(cost)
            
            dptable[idx]=cost

    print(dptable)
    result=list(reversed(dptable))
    print('result',result)

if __name__=="__main__":
    nums=list(map(int,input().split()))
    print(nums)
    reversedNums=list(reversed(nums))
    print(reversedNums)
    # 다음 게이트에서 지불할 비용은 이전 게이트에서의 비용보다 적거나 같아야한다.
    # => reveresed
    # 다음 게이트에서 지불할 비용은 이전 게이트에서의 비용보다 커야한다. with 다른 조건들
    # Wrong!! 명제의 반전이 아니라, 관점의 반전으로 = 도 포함되야
    # 다음 게이트에서 지불할 비용은 이전 게이트에서의 비용보다 크거나 같아도 된다. with 다른 조건
    dp(reversedNums)