## template
import math

def getinput():
    input01=int(input())
    return input01

def tempfunction(k):
  for i in range(k):
    for j in range(2*k-1):
      if(i>=abs( math.floor((2*k-1)/2)-j) ):
        print('*',end='')
      else:
        print(' ',end='')

    print()

k=getinput()
tempfunction(k)
