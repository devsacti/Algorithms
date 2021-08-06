from itertools import combinations
from itertools import permutations

from string import ascii_lowercase

# 놀랍게도 4일만에 개념논리적으론 
# 조합_4개중 2개 순서상관없이 뽑는것_과
# 순열_순서 구분해서 배치하는것_의 융합문제인 것을 발견

# 다만, 출력결과가 개념적인 4C2 x 2! 를 순으로 출력한게 아니라,
# 즉, [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
# 에서 각 요소에대해서 2!한 게 아니라 
# 재귀구조에 따른 순서로 출력
# ab ac ad ba bc bd ca cb cd da db dc

#--------------
# 아마도 ?개 중 2개일때는 
# sorted_total=sorted(total,key=lambda x: ord(x[0]))
# 가 먹히는데 그 이상부터는 순서가 잘못되는듯
# 결국 재귀구현해야

if __name__=="__main__":
    n, r = map(int, input().split())

    #alphabets='abcdefghijklmnopqrstu'

    alphabets=list(ascii_lowercase)
    candidates=alphabets[:(n-1)+1]

    result_combi=list(combinations(candidates,r))
    # print(result_combi)

    tmp=[list(x) for x in permutations(('a', 'b'))]
    # print(tmp)

    total=[]

    for element in result_combi:
        permuted=[list(x) for x in permutations(element)]
        total.extend(permuted)
    
    # print(total)
    sorted_total=sorted(total,key=lambda x: ord(x[0]))
    # print(sorted_total)

    for element in sorted_total:
        print(''.join(element))
