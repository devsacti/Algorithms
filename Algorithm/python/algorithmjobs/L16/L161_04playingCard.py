import sys
input=sys.stdin.readline

def dp(n,nums):
    if(n<=3):dptable=[0]*(1+3)
    else: dptable=[0]*(1+n)

    dptable[1]=nums[1]
    dptable[2]=nums[1]+nums[2]
    CANDs=[nums[1]+nums[3],nums[1]+nums[2],nums[2]+nums[3]]
    dptable[3]=max(CANDs)

    for i in range(4,n+1):
        a1=dptable[i-1]
        a2=dptable[i-2]+nums[i]
        a3=dptable[i-3]+nums[i-1]+nums[i]
        CANDs=[dptable[i-1],dptable[i-2]+nums[i],dptable[i-3]+nums[i-1]+nums[i]]
        dptable[i]=max(CANDs)

    return dptable[n]

if __name__=="__main__":
    n=int(input().strip())
    nums=[0]+list(map(int,input().split()))

    print(dp(n,nums))