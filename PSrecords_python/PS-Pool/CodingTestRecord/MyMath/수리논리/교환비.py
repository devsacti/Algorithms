import sys
input=sys.stdin.readline

if __name__=="__main__":
    std=int(input().strip())

    exR1=(1/1250)
    exR2=(1/1)
    exR3=(250)
    exR4=(9)

    result=std*exR1*exR2*exR3*exR4
    print(result)