# 숫자 피라미드
# 오후 6:14 2021-04-29
# 핵심
# 눈에 보이는 있는 그대로의 규칙성을 최대한 이용, 숨겨진 10 찾지말자
import sys

if __name__=="__main__":
    N,S = map(int, sys.stdin.readline().split())

    samplespace=[i for i in range(1,10)]
    start=samplespace.index(S)

    lensRow=[2*i-1 for i in range(1,N+1)]
    # print(lensRow)

    totalnum=sum(lensRow)
    nums=[]
    while(totalnum):
        nums.append(samplespace[start])
        start=(start+1)%9
        totalnum-=1
    # print(nums, len(nums))

    matrix=[]
    s=0
    for idx,lenrow in enumerate(lensRow):
        e=s+lenrow
        row=nums[s:e]
        if(idx%2==0): row=list(reversed(row))
        
        space=' '*(N-1-idx);print(space,end='')
        print(''.join(map(str,row)))

        s=e
    # print(*matrix,sep='\n')
