from string import ascii_lowercase
import copy

def permute(depth, candidates,n,r, result):
    if(depth>=r):
        print(''.join(result))
    else:
        for idx in range(n):
            if(candidates[idx] not in result):
                result[depth]=candidates[idx]
                permute(depth+1,candidates,n,r,result)
                result[depth]=0
            else:
                pass

if __name__=='__main__':
    n, r = map(int, input().split())

    #alphabets='abcdefghijklmnopqrstu'
    alphabets=list(ascii_lowercase)
    # print(alphabets)

    candidates=alphabets[:(n-1)+1]

    '''step2 이해단계'''

    # permutation=[[i,j] for i in candidates for j in candidates if j!=i]
    # print(permutation)
    # 이중 폴문을 위와같이 축약->3중, 4중이 되는 구조를 상상해야, 즉 재귀단계마다 폴문이 있어야하지 않을까

    # for element in permutation:
    #     print(''.join(element))
    
    depth=0
    result=[0]*r

    permute(depth, candidates,n,r,result)