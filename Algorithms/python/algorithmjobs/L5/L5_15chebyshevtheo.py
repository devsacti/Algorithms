'''
time limit을 해결하는 방법
1. 루트씌우기
2. 에라토스테네스의 체; 결국은 이미 확인한 소수나 구간에 대한 소수의 갯수의 경우
기존 확인이나 값을 활용하면 끝
->
'''
import math

ex_primes=set()

def judgeprime(element):
    limit_area=int(math.sqrt(element))
    token_prime=1

    for i in range(2, limit_area+1):
        if(element%i==0):
            token_prime=0
            break

    if(token_prime==1):
        ex_primes.add(element)
        return 1
    else:
        return 0

def findprimes(n):

    domain=[i for i in range(n+1,2*n+1)]
    cnt_prime=0

    for element in domain:
        cnt_prime+=judgeprime(element)
        '''
        이렇게 하면 결국 제곱근 까지만 확인하는 요령은 1순위로 적용하는건데
        결국 시간줄이기에 부족했음.
        if(element in ex_primes):
            cnt_prime+=1
        else:
            cnt_prime+=judgeprime(element)
        '''

    print(cnt_prime)

if __name__=='__main__':
    token=1
    ns=[]

    while(token != 0 ):
        element=int(input())
        if(element==0):
            break
        else:
            ns.append(element)

    # print(ns)

    # 아래 부분을 에라토스테네스가 대체 및 최소화
    # for n in ns:
    #     findprimes(n)

    
    #에라토스테네스의 체 활용하기; 가장 n을 통해 미리 소수를 확인하면
    # 1000 1001 1002의 n들이 들어올때 훨씬 빠름, 1 10 100은 여전해도
    max_n=max(ns)
    
    domain=[i for i in range(2,2*max_n+1)]
    # print(domain)

    cnt_prime=0
    
    for element in domain:
        cnt_prime+=judgeprime(element)

    # print(ex_primes)
    candidates_primes=sorted(list(ex_primes))
    # print(candidates_primes)

    for n in ns:
        min_domain=n+1
        max_domain=2*n

        min_idx=0
        max_idx=len(candidates_primes)-1

        for idx,element in enumerate(candidates_primes):
            if(min_domain<=element):
                min_idx=idx
                break

        for idx,element in enumerate(candidates_primes):
            # print(idx, element)
            if(max_domain<element):
                max_idx=idx-1
                break

            if(max_domain==element):
                max_idx=idx
                break

        # print(min_idx, max_idx)
        print(max_idx-(min_idx-1))