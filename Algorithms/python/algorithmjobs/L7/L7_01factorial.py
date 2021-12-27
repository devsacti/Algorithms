def factorial(N):
    if(N==1):
        return 1

    val_factorial=N*factorial(N-1)

    return val_factorial


if __name__=='__main__':
    N=int(input())

    result=factorial(N)

    print(result)