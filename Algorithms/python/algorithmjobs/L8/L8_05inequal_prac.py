def judge(result,inequalities):
    fomular=''
    token_recursive=0

    for idx in range(k):
        fomular+=result[idx]
        fomular+=inequalities[idx]
    fomular+=result[-1]

    result_inequal=eval(fomular)

    if(result_inequal=='True'):
        token_recursive=1
        return fomular, token_recursive
    else:
        return '',0

def numsfunctionupward(depth, result,token_downup):
    global k
    global inequalities
    global satifies

    if(depth>=(k+1)):
        #
        form=''
        print(''.join(result))

        if(''.join(result)=='111'):
            return

    else:
        for element in '0123456789':
            result[depth]=element
            #token이 1이면 그 뒤론 모두 continue가 되게 해보자
            
            tmp=numsfunctionupward(depth+1, result)
            result[depth]=0

def numsfunctiondownward(depth, result):
    global k
    global inequalities
    global satifies

    if(depth>=(k+1)):
        #
        form=''
        print(''.join(result))

        if(''.join(result)=='888'):
            return

    else:
        for element in '9876543210':
            result[depth]=element
            tmp=numsfunctiondownward(depth+1, result)
            result[depth]=0

if __name__=="__main__":
    global k
    k=int(input())
    global inequalities
    inequalities=input().split()
    print(inequalities)

    depth=0
    result=[0]*(k+1)

    satifies=list()

    token_downup=0
    token_updown=0

    tmptmp=numsfunctionupward(depth, result,token_downup)
    # tmptmp=numsfunctiondownward(depth, result)
    # print(satifies)

    