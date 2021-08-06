if __name__=='__main__':
    N=int(input())
    seq=list(map(int, input().split()))
    sorted_seq=sorted(seq)

    print(' '.join(map(str,sorted_seq)))