# step2 utilizations and Integrations with Time complexity

## Time complexity
## part1
## sorting => nlogn

## part2
## "for i in range(n)" and bisect per item => nlogn

## total
## nlogn + nlogn => nlogn

# step3 implementation
from bisect import bisect_left

if __name__=="__main__":
    n=int(input())
  
    nums=list(map(int,input().split()))
    nums.sort()
    
    # for i in range(n):
    #   print(i,end=' ')
    
    # print()
    # for item in nums:
    #   print(item,end=' ')
    
    bestpair=[]
    minimum_sum=int(1e20)
    # print(minimum_sum)
    # print()
  
    for i in range(n):
        std=nums[i]
        # print('i-std',i,std,end='/')
        # ideal pair인 -std의 삽입 인덱스를 구해보자
        l_i=bisect_left(nums,-std)
        # print('l_i',l_i)
        
        if(l_i==n):
            pair=nums[n-1]
        else:
            cand1=nums[l_i-1]
            cand2=nums[l_i]
            
            if(abs(std+cand1)<abs(std+cand2)):
                pair=cand1
            else:
                pair=cand2
            
        if(pair==std): continue
        
        # print(std,pair)
        
        val_sum=abs(std+pair)
        if(val_sum<minimum_sum):
            minimum_sum=val_sum
            bestpair=[std,pair]
        
        elif(val_sum==minimum_sum):
            if(min(std,pair)<min(bestpair)):
                bestpair=[std,pair]
        
        # print(bestpair)
    bestpair.sort()
    print(bestpair[0],bestpair[1])
