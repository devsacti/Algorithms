# 연속 부분 최대합 by divide and conquer
# divide and conquer include 'merge sort'

# 재귀함수를 작성하기 위한 과정 
# 1. 함수를 말로 정의한다.
# 2. 기저 조건을 우선 생각, 그리고 이에 따른 동작 정의
# 3. (하위) 함수가 제대로 작동한다고 가정하고 작성 
#

def getSubMax(start, end):
    # data 전체의 연속부분 최대합을 구해주는 함수
    # =>구체화
    # data의 start 부터 end까지 구간 중 연속 부분 최대합을 반환하는 함수

    if(start>=end): return data[start]

    mid = (start + end )//2
    # left의 최대값, right의 최대값을 구한다. 구했다 친다.
    leftMax = getSubMax(start,mid)
    rightMax= getSubMax(mid+1, end)

    # 중간부분을 포함하는 연속부분 중의 최대합을 구하자
    
    # s     mid          e
    # 1 8 -5 3 | 2 5 -10 2
    # 
    leftSubMax = data[mid];leftSubSum = data[mid]
    rightSubMax = data[mid+1];rightSubSum = data[mid+1]

    for i in range(mid-1,start-1,-1):
        leftSubSum = leftSubSum + data[i]

        if(leftSubMax < leftSubSum):
            leftSubMax = leftSubSum

    for i in range(mid+2,end+1):
        rightSubSum = rightSubSum + data[i]

        if(rightSubMax < rightSubSum):
            rightSubMax = rightSubSum
    
    middleMax = leftSubMax + rightSubMax

    if(leftMax >= rightMax and leftMax>=middleMax): return leftMax
    elif(rightMax>=leftMax and rightMax>=middleMax): return rightMax
    else: return middleMax


if __name__=="__main__":
    MAX=100
    n=0
    data=[[0] for _ in range(MAX)]

    n=int(input())
    data=list(map(int, input().split()))

    print(getSubMax(0,n-1))

