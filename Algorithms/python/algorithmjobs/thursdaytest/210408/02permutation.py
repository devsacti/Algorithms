import sys
import string
import itertools

if __name__=="__main__":
    n,r = map(int, sys.stdin.readline().split())

    samplespace=string.ascii_lowercase[:n]

    result=list(itertools.permutations(samplespace,r))

    # print(result)

    for case in result:
        print(''.join(case))