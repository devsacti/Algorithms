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