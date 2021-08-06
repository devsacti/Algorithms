import sys

def makefield(matrix,X,Y,R):
    global N
    
    for x in range(N):
        for y in range(N):
            dx=x-(X-1)
            dy=y-(Y-1)

            len_path=abs(dx)+abs(dy)

            if(len_path<=R):
                if(len_path==0):
                    matrix[x][y]='x'
                else:
                    matrix[x][y]=len_path
            else:
                continue

    return matrix

if __name__=='__main__':
    # 6 <= N <= 100
    global N
    N=int(sys.stdin.readline().strip())

    X,Y,R=map(int,sys.stdin.readline().split())

    matrix=[[0]*N for _ in range(N)]

    matrix=makefield(matrix,X,Y,R)

    for row in matrix:
        print(' '.join(map(str,row)))