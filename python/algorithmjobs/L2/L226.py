# template
# from collections import deque
# seqs=deque()
seqs = list()

def getArgs():
    n = int(input())
    for i in range(n):
        seqs.append(list(map(int, input().split())))

    return seqs


def checkcntsame(seq):
    cnt_same = 0
    std = seq[0]
    maxval = seq[0]

    for element in seq:
        if (std == element):
            cnt_same += 1
        else:
            std = element
            if(cnt_same==1):
                cnt_same = 0

            if (std > maxval):
                maxval = std

    return cnt_same, maxval


def calculateprize(cnt_same, std):
    prize=0

    if (cnt_same == 3):
        prize = 10000 + std * 1000
    elif (cnt_same == 2):
        prize = 1000 + std * 100
    elif (cnt_same == 1):
        prize = std * 100
    else:
        pass

    #print('prize', prize)

    return prize

def FindMaxPrize(seqs):
    prizelist = []

    for seq in seqs:
        cnt_same, std = checkcntsame(seq)
        prizelist.append(calculateprize(cnt_same, std))
        #print('prizelist', prizelist)

    prizelist.sort()
    maxprize = prizelist[-1]

    print(maxprize)


seqs = getArgs()
# print(seqs)
FindMaxPrize(seqs)

