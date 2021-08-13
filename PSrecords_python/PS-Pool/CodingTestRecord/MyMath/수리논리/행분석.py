import sys
input=sys.stdin.readline
from functools import reduce

if __name__=="__main__":
    # std and target
    unit1=list(map(int,input().split()))
    unit2=list(map(int,input().split()))

    print(sum(unit1))

    # function1=lambda x,y : math.lcm(x,y)
    # commonLCM=reduce(function1, nums)
    results=[]
    function1=lambda std,target:target/std

    for u1,u2 in zip(unit1,unit2):
        result=function1(u1,u2)
        results.append(result)

    print(list(enumerate(results,1)))
    # sorting
    print('--')
    sorted_results=sorted(results)
    print(list(enumerate(sorted_results,1)))
