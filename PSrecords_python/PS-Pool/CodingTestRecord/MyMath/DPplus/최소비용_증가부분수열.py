import sys
input=sys.stdin.readline

def findsmallNBiggestcost(num,curidx,prelist,predp):
    print('in find prenums ', prelist)
    print('in find precosts', predp)

    len_prelist=len(prelist)

    certain=len_prelist
    Biggestcost=-9999
    for idx in range(len_prelist-1,-1,-1):
        item=prelist[idx]
        item2=predp[idx]
        if(item<num and item2>Biggestcost):
            Biggestcost=item2
            certain=idx
    # no update at certain
    if(certain==len_prelist):
        certain=curidx
    
    return certain

def dp(nums,costs):
    length=len(nums)
    dptable=[0]*length

    # calcul only dptable during making longest increasing sequence
    for idx in range(length):
        if(idx==0):
            dptable[idx]=costs[idx]
        else:
            # find small one and that idx
            prelist=nums[:idx]
            predp=dptable[:idx]
            print('cur num', nums[idx])
            smallidx=findsmallNBiggestcost(nums[idx],idx,prelist,predp)
            print('where to follow ; idx and num',smallidx, nums[smallidx])
            if(smallidx!=idx):
                dptable[idx]=dptable[smallidx]+costs[idx]
            else:
                dptable[idx]=costs[idx]

    print(dptable)
    print('--result--')
    print(max(dptable))

if __name__=="__main__":
    given = input().split(',')
    # print(given)
    # print(list(given[0]))
    nums=list(map(int,given[0].split()))
    costs=list(map(int,given[1].strip().split()))
    
    # print(nums,costs)

    dp(nums,costs)
    print('--total--')
    print(sum(costs))