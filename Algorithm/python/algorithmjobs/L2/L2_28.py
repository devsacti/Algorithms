'''
## template
import numpy as np

def getArgs():
    #N : total level of pyramid , S : startnumber
    N, M = map(int,input().split())

    return N,M

def makeMatrix(N,M):
  arr=np.arange(1,N*M+1)
  arr=arr.reshape((N,M))

  print(arr)
    
if __name__=='__main__':
  N,M = getArgs()
  makeMatrix(N,M)
'''

'''
list comprehension

two_d_list = [[0 for _ in range(10)] for _ in range(5)]
'''
## template

def getArgs():
    #N : total level of pyramid , S : startnumber
    N, M = map(int,input().split())

    return N,M

def makeMatrix(N,M):
    two_d_matrix=[]
    element=1
    for i in range(N):
        row=[]
        for j in range(M):
            #리스트와 array는 다른 용법
            #matrix[i][j]=element
            #이건 특히 C 용법으로 기억
            row.append(element)
            print(row[j],end=' ')
            element+=1
        two_d_matrix.append(row)
        print()

    return two_d_matrix


if __name__=='__main__':
  N,M= getArgs()
  two_d_matrix=makeMatrix(N,M)
  #print(len(two_d_matrix),len(two_d_matrix[0]))
  