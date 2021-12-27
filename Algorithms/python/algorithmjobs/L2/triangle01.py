## template

def getinput():
    input01=int(input())
    return input01

def tempfunction(arg):
  for i in range(arg):
    for j in range(arg):
      if(j<=i):
        print('*',end='')
    print()

arg=getinput()
tempfunction(arg)
