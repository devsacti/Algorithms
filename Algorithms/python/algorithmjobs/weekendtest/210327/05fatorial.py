## template
def factorial(N):
    if(N==1):
        return 1
    else:
        total=N*factorial(N-1)
    
    return total
    
if __name__=="__main__":
  N=int(input())
  
  result=factorial(N)
  print(result)
  
  