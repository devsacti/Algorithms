from bisect import bisect_left, bisect_right
import sys
input=sys.stdin.readline

if __name__=="__main__":
    n,q = map(int,input().split())
    nums=list(map(int,input().split()));len_list=len(nums)
    qs=list(map(int,input().split()))

    for q in qs:
        result_left = bisect_left(nums, q)

        if(result_left<len_list):
            if(nums[result_left]==q):print('YES')
            else:print('NO')        
        else:print('NO')