import sys

def division(depth,subsum):
    global n,cnt
    global result

    if(subsum>=n):
        print('+'.join(map(str,result[:depth])))
        cnt+=1
        return
    else:
        if(depth==0):
            start_val_col=(n-1)
        else:
            start_val_col=n-subsum

        for num in range(start_val_col,0,-1):
            result[depth]=num
            
            if(depth > 0 and result[depth-1] < result[depth]):
                continue

            division(depth+1,subsum+num)


if __name__=="__main__":
    global n,cnt
    n=int(sys.stdin.readline().strip())
    cnt=0
    # print(chars)
    global result
    result=[0]*n

    depth=0
    subsum=0

    division(depth,subsum)
    print(cnt)