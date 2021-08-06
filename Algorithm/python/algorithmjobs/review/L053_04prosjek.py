import sys

if __name__=="__main__":
    N=int(input())

    bseqs=list(map(int, sys.stdin.readline().split()))
    aseqs=[]
    # print(N, bseqs)

    for denominator, val in enumerate(bseqs, 1):
        if(denominator==1):
            aseqs.append(val)
        else:
            subsum=val*denominator
            aseqs.append(subsum-sum(aseqs))

    print(' '.join(map(str,aseqs)))
