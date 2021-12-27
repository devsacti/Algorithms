## template
import pprint
def getArgs():
    #N, M = map(int,input().split())
    N=int(input())

    return N

def makeMatrix(N):
    two_d_matrix=[]
    element=1
    for i in range(N):
        row=[]
        for j in range(N):
            #print('-i j-',i,j)
            if(i>=1):
                if(j<=(N-1)-i):
                    #print(two_d_matrix[i-1][j+1])
                    row.append(two_d_matrix[i-1][j+1]+1)
                    print(row[j],end=' ')
                    #print(row)
                else:
                    continue
            else:
                element+=j
                row.append(element)
                print(row[j],end=' ')
                #print('i j',i,j)
                
        two_d_matrix.append(row)
        print()

    return two_d_matrix


if __name__=='__main__':
  N= getArgs()
  two_d_matrix=makeMatrix(N)

  #다양한 출력 방법
  #print(len(two_d_matrix),len(two_d_matrix[0]))
  #print(*two_d_matrix,sep='\n')

