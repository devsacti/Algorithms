from math import gcd

if __name__=='__main__':
    m1, d1 = map(int, input().split())
    m2, d2 = map(int, input().split())

    origin_d=d1*d2
    origin_m=m1*d2+m2*d1

    gcd_md=gcd(origin_m,origin_d)

    shortfraction_m, shortfraction_d = int(origin_m/gcd_md), int(origin_d/gcd_md)

    print(shortfraction_m, shortfraction_d)