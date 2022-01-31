if __name__=='__main__':
    n, q =map(int, input().split())

    seq=set(map(int, input().split()))

    quests=list(map(int, input().split()))

    # print(seq, quests)

    for quest in quests:
        if(quest in seq):
            print('YES')
        else:
            print('NO')