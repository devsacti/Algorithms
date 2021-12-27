'''
def gcd(A,B):
    # print(A,B)    
    c=A%B
    # print('c',c)
    if(B%c==0):
        return c
    val_gcd=gcd(B,c)

    return val_gcd

if __name__=='__main__':
    A, B = map(int, input().split())

    gcd=gcd(A,B)
    # print(gcd)

    lcm=int(A*B/gcd)
    print(lcm)

runtime error 나서 포기, 그래도 93점이긴함.
'''
from math import gcd

def lcm(x,y):
    GCD=gcd(x,y)
    LCM=x*y//GCD

    return GCD,LCM
'''
while, for문으로도 생성가능, 새삼스럽지만 for문도 C기준 2번째가 조건이다.

'''
if __name__=='__main__':
    A, B = map(int, input().split())

    gcd,lcm=lcm(A,B)
    print(lcm)