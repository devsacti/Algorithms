'''
5 기준
5
4,1
3,2
3,1,1
2 2 1
2 1 1 1
1 1,1,1,1
/

1열이 첫번째 for문이고 각 시행에서 조건에 따라 앞열은 pause느낌이고
빼서 뒤로 준다 '느낌으로 이해.
이때 중복 발생
정렬과정에서 내림차순만 선택하는 방법이 있다.

'''

def division(depth,mysum):
    global result2

    if(mysum==n):
        print('+'.join(map(str,result2[:depth])))

    else:
        if(depth==0):
            col_start_num=n-1
        else:
            col_start_num=n-mysum#mysum은 직전까지의 합

        for element in range(col_start_num, 0,-1):
            print(depth,result)
            result2[depth]=element

            if(depth > 0 and result2[depth-1] < result2[depth]):
                continue

            division(depth+1,mysum+element)

result=list()
n=int()
cnt=0

def origingetresult(mySum, index):
    global result
    global cnt
    # print(result)
    print()
    print('/'*(1+index),'start of function\n')

    if(mySum==n or index>=n):
        #
        print('limit of Recursive','-'*(1+index),index,end=' ')
        print(result)
        # print('+'.join(map(str,result[:index])))
        print()
        cnt+=1
    else:
        col_start_num=n-mySum
        print('-'*(1+index),'col_start and mySum ',col_start_num,mySum, result)
        for element in range(col_start_num, 0,-1):
            print('#'*(1+index),'start primitive period of for loop and index, result',index,result)
            result[index]=element
            print('index and element, result : ',index,element,result)
            # if(index > 0 and result[index-1] < result[index]):
            #     continue
            origingetresult(mySum+element, index+1)
            print('before return to 0 index && result : ',index,result)
            result[index]=0
            print('after return to 0 index && result : ',index,result)
            print('end primitive period of for loop','#'*(1+index))
            print()

    print('end of function','/'*(1+index))


def getresult(mySum, index):
    global result
    global cnt
    # print(result)

    if(mySum==n):
        #
        print('+'.join(map(str,result[:index])))
        cnt+=1
    else:
        if(index==0):
            col_start_num=n-1
        else:
            col_start_num=n-mySum#mysum은 직전까지의 합

        for element in range(col_start_num, 0,-1):
            print(index,result)
            result[index]=element

            if(index > 0 and result[index-1] < result[index]):
                continue

            getresult(mySum+element, index+1)

if __name__=="__main__":
    n=int(input())
    result=[0]*n
    result2=[0]*n


    mySum=0 #mySum
    index=0

    origingetresult(mySum,index)

    # getresult(mySum, index)
    print(cnt)

    depth=0
    mysum=0
    # division(depth,mysum)