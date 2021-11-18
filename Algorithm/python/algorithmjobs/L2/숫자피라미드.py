# template
from collections import deque

def getArgs():
    #N : total level of pyramid , S : startnumber
    N, S = map(int,input().split())
    '''
    for i in range(n):
        seqs.append(list(map(int, input().split())))
    '''

    return N,S

def makeval_level(N):
    Lens_levels=deque([2*domain+1 for domain in range(N)])
    sum_lens=sum(Lens_levels)

    return Lens_levels, sum_lens

def makeElement(S, sum_len):
    #given pattern
    pattern=[i for i in range(1,10)]
    idx_start=pattern.index(S)
    #print(pattern[idx_start],pattern)

    elements=deque()

    for i in range(sum_len):
        elements.append(pattern[(idx_start%9)])
        idx_start=idx_start+1

    return elements

def makelevel(N,levelnum, Lens_levels, elements):
    Lenlevel=Lens_levels.popleft()
    #print('Len_level', Lenlevel)

    leveldq=deque()

    if(levelnum%2!=0):
        for i in range(Lenlevel):
            leveldq.appendleft(elements.popleft())
        for i in range(N-levelnum):
            leveldq.appendleft(' ')
    else:
        for i in range(N-levelnum):
            leveldq.append(' ')
        for i in range(Lenlevel):
            leveldq.append(elements.popleft())
    
    #print(leveldq)
    #print(elements)

    return leveldq



def makePyraid(N,Lens_levels,elements):
    leveldq=deque()
    leveldqs=deque()

    for idx_level in range(N):
        levelnum=idx_level+1
        
        leveldq=makelevel(N,levelnum,Lens_levels,elements)

        leveldqs.append(leveldq)

    #print(leveldqs)

    return leveldqs

def makeResult(leveldqs):
    for i in range(len(leveldqs)):
        level=leveldqs.popleft()
        for i in level:
            print(i,end='')
        print()

if __name__=='__main__':
    N,S = getArgs()
    #print(N,S)
    # 5 3

    Lens_levels, sum_lens=makeval_level(N)
    #print(Lens_levels)
    #[1,3,5,7,9]

    elements=makeElement(S,sum_lens)
    print(elements)
    # [1,2,3,4~9,1]

    leveldqs=makePyraid(N,Lens_levels,elements)
    makeResult(leveldqs)





