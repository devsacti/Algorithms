def judge(result,inequalities):
    global satifies

    fomular=''
    val_token=0


    for idx in range(k):
        fomular+=result[idx]
        fomular+=inequalities[idx]
    fomular+=result[-1]

    result_inequal=eval(fomular)

    # print(result, inequalities, end=' ')
    # print(fomular,result_inequal,end=' ')

    if(result_inequal==True):
        # print(result,end='')
        #곳곳에 존재하는 쉘로우카피문제를 생각하자
        # satifies.append(result)

        satifies.append(result[:])
        val_token=1
        return val_token
    else:
        return val_token

def numsfunctiondownward(depth, result):
    global k
    global inequalities
    global token_downward

    if(depth>=(k+1)):
        # print(result)
        token_downward=judge(result,inequalities)
        # print(token_downward)
        #최종출력물 형태보면 여기서 받지 말자
        # if(token_downward==1):
        #     satifies.append(result)

    else:
        for element in '9876543210':
            if(token_downward==1):
                continue
            
            # print(element, result)
            if(element not in result):
                result[depth]=element
            else:
                continue
            numsfunctiondownward(depth+1, result)
            result[depth]=0

def numsfunctionupward(depth, result):
    global k
    global inequalities
    global token_upward

    if(depth>=(k+1)):
        # print(result)
        token_upward=judge(result,inequalities)
        # print(token_upward)
        # if(token_upward==1):
        #     satifies.append(result)

    else:
        for element in '0123456789':
            if(token_upward==1):
                continue
            
            # print(element, result)
            if(element not in result):
                result[depth]=element
            else:
                continue
            numsfunctionupward(depth+1, result)
            result[depth]=0

if __name__=="__main__":
    global k
    k=int(input())
    global inequalities
    inequalities=input().split()
    # print(inequalities)

    depth=0
    result=[0]*(k+1)

    satifies=[]
    
    global token_downward
    token_downward=0

    global token_upward
    token_upward=0

    numsfunctiondownward(depth, result)
    # print(satifies)
    numsfunctionupward(depth, result)
    # print(satifies)

    for item in satifies:
        print(''.join(item))
