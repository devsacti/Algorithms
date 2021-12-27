if __name__=='__main__':
    N=int(input())

    seq1=set(map(int, input().split()))

    M=int(input())

    seq2=list(map(int, input().split()))

    for quest in seq2:
        if quest in seq1:
            print('1')
        else:
            print('0')