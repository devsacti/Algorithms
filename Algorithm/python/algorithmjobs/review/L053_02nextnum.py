import sys

if __name__=="__main__":
    progressions=[]
    while(1):
        a1, a2, a3 =map(int, sys.stdin.readline().split())
        if(a1 == 0 and a2 == 0  and a3==0):
            break

        progressions.append( (a1, a2 , a3) )

    # print(progressions)

    for progression in progressions:
        a1, a2,a3=progression

        if( 2*a2 == a1+a3 ):
            print('AP',a3+(a2-a1))

        if( a2**2 == a1*a3 ):
            print('GP', a3*(a2//a1))