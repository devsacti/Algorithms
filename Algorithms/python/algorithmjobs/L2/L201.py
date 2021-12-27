## template

def getArgs():
    n=int(input())
    seq=list(map(int,input().split()))
    #**multi arugment search
    return n, seq

def tempfunction(n, seq):
  #python don't need n argument
  
  #processing seq
    seq.reverse()
    for item in seq:
        print(item, end=' ')

n, seq=getArgs()
#print(n, seq)
tempfunction(n, seq)
