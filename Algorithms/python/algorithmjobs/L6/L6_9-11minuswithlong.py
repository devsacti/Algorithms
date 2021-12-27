'''
파이썬 특성상 거의 의미가 없는 문제 3개라 그냥 묶음

part1->9번 문제
part2->10번
등

'''

'''파트1'''
def plusbetweenlong(a,b):
    #java, c에서는 자료형상 long같은 문제가 있지만 파이썬은 없음
    return a+b

'''파트2'''
def minusbetweenlong(a,b):
    return a-b

'''파트3'''
def productbetweenlong(a,b):
    return a*b

if __name__=='__main__':
    nums=[]
    for i in range(2):
        nums.append(int(input()))

    #result=plusbetweenlong(nums[0],nums[1])
    result= productbetweenlong(nums[0],nums[1])

    print(result)