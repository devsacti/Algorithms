if __name__=='__main__':
    N=int(input())
    bsequence=list(map(int,input().split()))

    aseq=[]

    for i in range(N,0,-1):
        if(N==1):
            aseq.append(bsequence[0])
            break
        aseq.append(bsequence[i-1]*i-bsequence[i-2]*(i-1))

    aseq=list(reversed(aseq))
    
    
    for element in aseq:
        print(element, end=' ')