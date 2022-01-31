if __name__=='__main__':
    N,k = map(int, input().split())
    temp=list(map(int, input().split()))

    temp=sorted(temp,reverse=True)

    print(temp[k-1])