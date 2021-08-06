## template

seq=[]

def getArgs():
    n=9
    for i in range(n):
        seq.append(int(input()))
        
    return n, seq

def tempfunction(n, seq):
  #python don't need n argument
  
  #processing seq
    max=sorted(seq)[-1]
    idx_max=seq.index(max)+1
    print(max)
    print(idx_max)

n, seq=getArgs()
#print(n, seq)
tempfunction(n, seq)
