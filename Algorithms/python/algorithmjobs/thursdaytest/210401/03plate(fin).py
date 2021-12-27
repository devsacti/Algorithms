## template
from collections import deque
import sys
import string

# 설계할때, 문제에서 제시된 절차를 그대로 따라가는 게 중요한데,
# 큰 그림, 기본적으로 중간과 마지막 상황에 대한 최소한의 상상은 해야한다

if __name__=="__main__":
  std_string=list(sys.stdin.readline().strip())
  
  underlimit=len(std_string)
  
  samplespaces=string.ascii_lowercase
  dq_samples=deque(samplespaces[:underlimit])
  # print(std_string,dq_samples)
  
  stack_calcul=list()
  # variable은 constant와 달리, 초기화는 물론, !! 갱신 위치도 고려해야
  top_stackcc=len(stack_calcul)-1
  top_element=''
  
  token_possible=True
  curidx_stdstring=0
  cmds=[]
  ## 추후 action의 원인이 되는 변수를 조건으로 잡으니까, 필요한 시행이 
  # 모두 완료되지 못하는 상황 발생, 애당초 구조적으로 부적절한 변수이므로
  # 이걸로 뻘짓하지 말고, 빠르게 간접 조건과 제한으로 전환해라
  # 확신이 있다면 1도 괜찮은데, 되도록 토큰으로 명확하게 표시하자
  # while(dq_samples):
  while(1):
    # 필요 문자와 현재 스택 상 값을 비교하기 위한 초기화들
    #standard
    std_chr=std_string[curidx_stdstring]
    
    #experiment val; val of top of stack
    # !! top variable 갱신 위치
    top_stackcc=len(stack_calcul)-1
    if(top_stackcc==-1):
      top_element='*'
    else:
      top_element=stack_calcul[-1]
      
    # exit 2; 중간상황
    # 앞선 과정으로 스택에 값들이 쌓임
    if(std_chr in stack_calcul and std_chr != top_element):
      token_possible=False
      break
    
    # 판단 부분
    if(std_chr==top_element):
      tmp=stack_calcul.pop()
      cmds.append('pop')
      curidx_stdstring+=1
    else:
      if(dq_samples):
        stack_calcul.append(dq_samples.popleft())
        cmds.append('push')
        
    # 판단부분의 pop을 고려한 exit 1; 마지막 상황
    # pop 한걸 받았더니, 원하는 문자열이 만들어졌다는 상황
    if(curidx_stdstring>=underlimit):
      token_possible=True
      break
    
  if(token_possible):
    for cmd in cmds:
      print(cmd)
  else:
    print('impossible')
    
    
    