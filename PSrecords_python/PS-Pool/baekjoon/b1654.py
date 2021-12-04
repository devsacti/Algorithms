# 랜선 자르기

# ? 왜 e를 max로 잡아야하지, 자른다고 한다면, 최소한 자기자신보다 긴 걸로는 못자르고,
# 최소길이의 랜선이 최대값이 될것같은데....

if __name__=="__main__":
    k,n = map(int, input().split())
    
    nums=[]
    for _ in range(k):
        cand=int(input())
        nums.append(cand)
        
    s=1
    e=max(nums)
    
    while(s<=e):
        mid=(s+e)//2
        
        total_cnt=0        
        for num in nums:
            total_cnt+=(num//mid)
            
        if(total_cnt>=n):
            max_len=mid
            s=mid+1
        else:
            e=mid-1
            
    print(e)