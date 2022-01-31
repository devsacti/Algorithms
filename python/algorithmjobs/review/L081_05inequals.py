import sys
input=sys.stdin.readline

# variables for backtracking
global n

def recursiveBruteforce(depth,result,limit):
    if(i>=limit):
        pass
    else:
        pass

if __name__=="__main__":
    n=int(input().rstrip())
    inequals=input().split()

    # cnt of spaces : 1+ n-1 +1
    # cnt of num : n
    # total 2n+1
    fomular=[' ']+list(' '.join(inequals))+[' ']
    print(fomular)    
