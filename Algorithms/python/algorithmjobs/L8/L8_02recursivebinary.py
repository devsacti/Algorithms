def recursice_binary(depth,n,k,result):
    if(depth>=n):
        print(result)
    else:
        #
        for num in range(1,-1,-1):
            if(result.count(1)<k):
                result[depth]=num
                recursice_binary(depth+1,n,k,result)
                result[depth]=0
            else:
                pass

def test_recursice_binary(depth,n,k,result):
    print('#',depth,n,k,result)

    if(depth>=n):
        print('#onif',depth,end=' ')
        print(result)
    else:
        #
        for num in range(1,-1,-1):
            result[depth]=num
            test_recursice_binary(depth+1,n,k,result)
            result[depth]=-1

def test2_recursice_binary(depth,n,k,result):
    print('#',depth,n,k,result)
    
    if(depth>=n):
        if(sum(result)==k):
            print(''.join(map(str,result)))
    else:
        #
        for num in range(1,-1,-1):
            result[depth]=num
            test2_recursice_binary(depth+1,n,k,result)
            result[depth]=0

def test3_recursice_binary(depth,n,k,result):
    # print('#',depth,n,k,result)
    
    if(depth>=n):
        if(sum(result)==k):
            print(''.join(map(str,result)))
    else:
        if(sum(result)==k):
            print(''.join(map(str,result)))
        else:
            for num in range(1,-1,-1):
                result[depth]=num
                test3_recursice_binary(depth+1,n,k,result)
                result[depth]=0

if __name__=="__main__":
    n,k= map(int, input().split())

    depth=0
    result=[0]*n

    # print([i for i in range(1,-1,-1)])
    # recursice_binary(depth, n,k,result)
    # print('------')
    test_recursice_binary(depth, n,k,result)
    # test2_recursice_binary(depth, n,k,result)
    # test3_recursice_binary(depth, n,k,result)


