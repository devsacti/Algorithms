# ps1

# ps2

# ps3 Impl

if __name__=="__main__":
    n = int(input())
    
    nums=list(map(int,input().split()))

    print(nums)
    
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