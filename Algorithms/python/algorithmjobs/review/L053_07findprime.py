import sys 
import math

def findprime(num):
    global cnt

    equallimit=round(math.sqrt(num))

    token_prime=True
    # exclude 1
    for denominator in range(2,equallimit+1):
        if(num%denominator == 0):
            token_prime=False
            break
    
    if(token_prime):
        # print(num)
        cnt+=1

if __name__=="__main__":
    N = int(sys.stdin.readline().strip())
    global cnt
    cnt=0

    nums=[]
    for _ in range(N):
        nums.append(int(sys.stdin.readline().strip()))

    for num in nums:
        if(num != 1): findprime(num)
    print(cnt)
