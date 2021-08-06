## template
import sys
# lms 따라서 얼핏아는 라이브러리는 쓰지도 못하네, . 뒤에 설명이 안나와서
# import asci blabal 
import string
from collections import deque


if __name__=="__main__":
  std=list(sys.stdin.readline().strip())
  
  underlimit=len(std)
  print(std)
  
  samplespace=string.ascii_lowercase
  print(samplespace)
  print(len(samplespace))
  
  samples=samplespace[:underlimit]
  dq_samples=deque(samples)
  print(dq_samples)
  
  #int the stack
  calcul_stack=deque()
  
  # in relevant situation, when all samples are dequeued, std str is maded
  # with relavant cmds like push push pop pop blabla
  # but if there is some problem print impossible
  curidx=0
  cmds=[]
  token_possible=True
  
  while(dq_samples):
    calcul_stack.append(dq_samples.popleft())
    cmds.append('push')
    
    if(calcul_stack[-1]==std[curidx]):
      tmp=calcul_stack.pop()
      curidx+=1
      cmds.append('pop')
    else:
      

  
  # while(dq_samples):
  #   # push is all ways required -> No -> yes.....
  #   # 처음에 calcul_stack에 내용물 있냐 없냐로 우선 판단한 후 push했는데
  #   # 결국은 문제조건과 불합치한 나의 사견으로, 실제 문제 해결 과정에서
  #   # 예상치 못한 오류 발생, while 내 if else로 원래의 연속동작이 쪼개지면서
  #   # 마지막 cmd가 제대로 저장안됨.
  #   # !! 문제의 조건과 있는그대로에 충실하자.
    
  #   # 잘못된 흐름 파악은 잘했는데, 해결책은 잘못찾음
  #   #그냥 init을 해서 로직문제 해결
    
  #   # 애당초 큰그림을 우선 탑과 필요값을 비교해야하는데, 접근 잘못해서,
  #   # 완전 재 설계
  #   # while(dq_samples):-> 탑이랑 필요값 같을때가지 push해야지
  #   #at least 1 item in calcul_stack
    
  #   #init for convenient
  #   calcul_stack.append(dq_samples.popleft())
  #   print('init',calcul_stack)
  #   cmds.append('push')
  
  #   while(calcul_stack[-1]!=std[curidx]):
  #     calcul_stack.append(dq_samples.popleft())
  #     cmds.append('push')
  #     print('in while',calcul_stack)
      
  #   #위 while에 의해서 calcul_stack[-1]==std[curidx] 이면 멈춘다.
  #   # 그리고 샘플들이 입력값에서 파생되서 반드시 1개는 같게되있음
  #   if(len(calcul_stack)!=0):
  #     tmp=calcul_stack.pop()
  #     curidx+=1
  #     cmds.append('pop')
  #   print(cmds)
    
  #   # 근데 원하는 걸 찾았더니, 데크가 비어져있다면 불가능
  #   if(len(dq_samples)==0):
  #     token_possible=False
  #     print('impossible')
  #   else:
  #     #안비워져 있다면, 다시 while
  #     pass
    
    
    
    # if(calcul_stack[-1]==std[curidx]):
    #   tmp=calcul_stack.pop()
    #   curidx+=1
    #   cmds.append('pop')
    # else:
    #   calcul_stack.append(dq_samples.popleft())
    #   cmds.append('push')
      
    # # 중복이 없는 상황에서 현재필요한 std[curidx]가 탑에 없으면 실패임
    # if(std[curidx] != calcul_stack[-1]):
    #   print('impossible')
    #   token_possible=False
    #   break
    # else:
    #   tmp=calcul_stack.pop()
    #   curidx+=1
    #   cmds.append('pop')
    
  if(token_possible):
    for cmd in cmds:
      print(cmd)
        
  
        