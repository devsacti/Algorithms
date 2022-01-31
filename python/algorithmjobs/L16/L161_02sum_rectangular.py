import sys

if __name__=="__main__":
    N,M,Q = map(int, sys.stdin.readline().split())

    matrix=[]
    for _ in range(N):
        row=list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

    subsum_matrix=[[0]*M for _ in range(N)]

    cmds=[]
    for _ in range(Q):
        cmds.append(list(map(int, sys.stdin.readline().split())))

    # print(*matrix, sep='\n')
    # print(cmds)

    # for cmd in cmds:
        