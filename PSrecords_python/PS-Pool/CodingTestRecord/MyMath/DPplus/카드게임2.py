import sys
input=sys.stdin.readline
# 맨처음과 맨 마지막을 반드시 포함해야한다면 어찌?
# 맨처음 맨뒤 떼고 돌리면 되지 않을까?
# => 맨처음과 맨뒤에서 3개 연속 케이스가 발생가능

# 초항과 for의 반복 패턴속에 예외를 두어서 설정
# => 
# 길이가 3이상이면 상관없는데
# 추가 예외 발생, 길이가 3일때 dptable[3]은 for이 작동하지 않고
# 로직상 맨마지막을 선택하는 로직이 누락된다.
# 따라서 길이가 3인경우는 dptable[3]에서 맨마지막 을 선택하는 과정을 추가해줘야한다.

def dp(n,nums):
    if(n<=3):dptable=[0]*(1+3)
    else: dptable=[0]*(1+n)

    dptable[1]=nums[1]
    dptable[2]=nums[1]+nums[2]
    # CANDs=[nums[1]+nums[3],nums[1]+nums[2],nums[2]+nums[3]]
    # 반드시 1을 가진 경우라, 2개 중 선택
    CANDs=[nums[1]+nums[3],nums[1]+nums[2]]
    if(n==3):CANDs=[nums[1]+nums[3]]
    dptable[3]=max(CANDs)

    for i in range(4,n+1):
        CANDs=[dptable[i-1],dptable[i-2]+nums[i],dptable[i-3]+nums[i-1]+nums[i]]
        if(i==n):CANDs=[dptable[i-2]+nums[i],dptable[i-3]+nums[i-1]+nums[i]]

        dptable[i]=max(CANDs)

    return dptable[n]

if __name__=="__main__":
    n=int(input().strip())
    nums=[0]+list(map(int,input().split()))
    print('--result--')
    print(dp(n,nums))