import sys
input=sys.stdin.readline
import math
from functools import reduce

if __name__=="__main__":
    nums=list(map(int,input().split()))

    
    function1=lambda x,y : math.lcm(x,y)
    commonLCM=reduce(function1, nums)
    
    print('lcm',commonLCM)

    function2=lambda x,y : math.gcd(x,y)
    commonGCD=reduce(function2, nums)

    print('gcd',commonGCD)