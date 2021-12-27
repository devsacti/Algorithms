def getArgs():
    #N, M = map(int,input().split())
    N=int(input())
    seq = map(int,input().split())

    return N, seq

def countViolation(N, seq):
    cnt=0
    for num_car in seq:
        if(num_car == N):
          cnt+=1
    
    print(cnt)
    
if __name__=='__main__':
    N, seq = getArgs()
    countViolation(N,seq)