from math import gcd

def getArgs():
    M, N = map(int, input().split())
    
    return M,N

def lcm(x,y):
    GCD=gcd(x,y)
    LCM=x*y//GCD

    return GCD,LCM

if __name__=='__main__':
    M,N=getArgs()
    gcd,lcm=lcm(M,N)
    print(gcd)
    print(lcm)