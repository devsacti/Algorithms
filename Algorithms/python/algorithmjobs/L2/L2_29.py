#template

def getArgs():
    N, M = map(int,input().split())

    rows=[]

    for i in range(N):
        row=list(map(int,input().split()))
        rows.append(row)

    r,c= map(int,input().split())

    return N,M, r,c, rows

if __name__=='__main__':
  N,M, r,c, rows= getArgs()
  #two_d_matrix=makeMatrix(N,M)
  #print(len(two_d_matrix),len(two_d_matrix[0]))
  print(rows[r][c])