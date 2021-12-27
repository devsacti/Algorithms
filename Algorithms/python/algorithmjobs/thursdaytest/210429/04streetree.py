# streetree
# 오후 7:17 2021-04-29
# summary
# using gcd between intervals

# tcp 1
# invervals가 2개이면 idx==0 or 1 일때, continue가 아니라, totalgcd 정의해줘야

import sys
from math import gcd

if __name__=="__main__":
    N=int(sys.stdin.readline().strip())
    nums=[]
    for _ in range(N):
        nums.append(int(sys.stdin.readline().strip()))

    intervals=[]
    for idx,val in enumerate(nums):
        if(idx==0):continue
        else:
            intervals.append(val-nums[idx-1])
    
    # print(intervals)

    for idx,val in enumerate(intervals):
        if(idx==0 or idx==1): 
            totalgcd=gcd(intervals[0],intervals[1])
        else:
            totalgcd=gcd(totalgcd,val)

    # print(totalgcd)

    totallen=nums[-1]-nums[0]
    # print(totallen)
    maxcnt=totallen//totalgcd
    cntTree=len(nums)

    print(maxcnt+1-cntTree)
