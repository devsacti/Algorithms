import sys

# int 1, str '1' 모두 출력되면 1이더라....
# 적절한 초기화 위치와 기본문법인 자료형....
# 파이썬 하면 변수에 대한 감각이 무뎌지는데, 그냥 C 편한상태로 생각하자

def makeallcases(depth,case,limit):
  global allcases
  # print(depth,case)
  if(depth>=limit):
    # print('ck')
    # fucking shellow copy, cuz to case=[depth]=0 when at the last all case is become [0,0,0]
    # so should slice or deepcopy
    # allcases.append(case[]) is worthless
    allcases.append(case[:])
    # print(len(allcases),end=' ')
    return
  else:
    for num in range(1,10):
      if(num not in case):
        case[depth]=num
        makeallcases(depth+1,case,limit)
        case[depth]=0
      else:
        continue


if __name__=="__main__":
  N=int(sys.stdin.readline().strip())
  
  answers=[]
  for _ in range(N):
    answer=sys.stdin.readline().split()
    answers.append(answer)
    
  # print(answers)
  
  global allcases
  allcases=[]
  
  depth=0
  case=[0]*3
  limit=3
  makeallcases(depth,case,limit)
  
  # print(len(allcases))
  
  satisfyingcases=[]
  for case in allcases:
    #token per case
    token_allpass=True
    # print(case)
    
    #init strike, ball per case, NO!!! per answer!!
    # cnt_strike=0
    # cnt_ball=0
    
    for answer in answers:
      #init strike, ball per case, NO!!! per answer!!
      cnt_strike=0
      cnt_ball=0
      
      std_trial=list(map(int,answer[0]))
      std_strike=int(answer[1])
      std_ball=int(answer[2])
      # print(std_trial,std_strike,std_ball,end='/')
      
      for idx_std, val_std in enumerate(std_trial):
        for idx_case, val_case in enumerate(case):
          if(val_std==val_case):
            #at least ball or strike
            if(idx_std==idx_case):
              cnt_strike+=1
            else:
              cnt_ball+=1
          else:
            pass
          
      # print(case, cnt_strike,cnt_ball)
      
      # checking one answer
      if(cnt_strike==std_strike and cnt_ball==std_ball):
        #maintain
        # print(case)
        token_allpass=True
      else:
        token_allpass=False
        break
    
    #after checking answers per case ex) 4times
    if(token_allpass):
      satisfyingcases.append(case)
  
  print(len(satisfyingcases))