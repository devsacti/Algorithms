'''

'''
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

def numsfunctionupward(depth, result):
    global k
    global inequalities
    global satifies

    if(depth>=(k+1)):
        #
        form=''
        print(result)
        form, token_rec=judge(result,inequalities)
        satifies.append(form)
        if(token_rec):
            exit(0)

    else:
        for element in '0123456789':
            result[depth]=element
            numsfunctionupward(depth+1, result)
            result[depth]=0

def numsfunctiondownward(depth, result):
    global k
    global inequalities
    global satifies

    if(depth>=(k+1)):
        #
        print(result)

    else:
        for element in '9876543210':
            result[depth]=element
            numsfunction(depth+1, result)
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

    numsfunctionupward(depth, result)
    # numsfunctiondownward(depth, result)
    print(satifies)

    