if __name__=='__main__':
    n=int(input())

    binarys=[]

    while(n>=1):
        binarys.append(n%2)
        n=n//2
    
    binarys.reverse()

    for element in binarys:
        print(element, end='')