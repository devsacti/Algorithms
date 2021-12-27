import math

if __name__=='__main__':
    N=int(input())

    cnt_prime=0

    nums=[]
    for i in range(N):
        nums.append(int(input()))

    if (1 in nums):
        nums.remove(1)

    primes=[]
    for num in nums:
        limit=int(math.sqrt(num))
        #limit에 +1하면 틀렸는데 이유를 모르겠다.
        cnt_pass=0

        for element in range(2,limit+1):
            if(num%element==0):
                continue
            else:
                cnt_pass+=1
        
        if(cnt_pass==len(range(2,limit+1))):
            primes.append(num)

    # print(primes)
    print(len(primes))

