import sys
import math

if __name__=="__main__":
    numerator1, denominator1 = map(int, sys.stdin.readline().split())
    numerator2, denominator2 = map(int, sys.stdin.readline().split())

    numerator = numerator1*denominator2 + denominator1*numerator2
    denominator = denominator1*denominator2

    gcd_numanddeno=math.gcd(numerator,denominator)

    print(round(numerator/gcd_numanddeno), round(denominator/gcd_numanddeno))