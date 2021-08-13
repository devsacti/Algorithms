import string

from itertools import product
from itertools import combinations
from itertools import permutations

n,r =map(int,input().split())

sample=[i for i in range(1,n+1)]
sample2=[char for char in string.ascii_lowercase]
print(sample)
print(sample2)

allcases=list(product(sample,sample2))
print(allcases)

comb=list(combinations(sample,r))
print(comb)
print(len(comb))

permute=list(permutations(sample,r))
print(permute)
print(len(permute))
