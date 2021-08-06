## template
'''
!!초기화 위치문제로 거의 30분 아웃, 특히나 print도 불편해서
설계는 손을 좀 써라 시바새키야

pass와 continue가 느낌상 유사하지만
각각은 if else, for문 내로 한정하자

피할 수 없는 시간복잡도
1)sort excluded
(9*8*7)*N=>O((9*8*7)*N)

2)sort included,
NlogN+{best 1 worst (9*8*7)*N} => O(N(logN+1))~O(N(logN+(9*8*7)*N)
; N이 충분히 작고 best면
(9*8*7)*N 과 N(logN+1)
즉, (9*8*7) 과 (logN+1)) 비교
웬만하면 로그값이 504보다 작아서 괜춘인데,

지금보니까 worst시 너무 후짐,

하지만 1~100이 N범위 해볼만
정렬

+
근데, 볼이랑 스스트라이크 자릿수별로 비교할때 *3*3추가임,
뭐 정렬이나 안하나 '공통'인 부분이니까 쫄지말자

O((9*8*7)*N)*3*3
과
O(N(logN+1))~O(N(logN+(9*8*7)*N)*3*3

+부하를 줄이기 위해 
        for idx_std, val_std in enumerate(std_case):
              for idx_case, val_case in enumerate(case):
            # print(idx_std,val_std,idx_case,val_case, end='/')
            if(int(val_std)==val_case):
              if(idx_std==idx_case):
                cnt_strike+=1
              else:
                cnt_ball+=1
한 부분 굿
'''

def allcasecheckNcalculcnt(sorted_q):
  samplepace=[i for i in range(1,10)]
  allcase=[(i,j,k) for i in samplepace for j in samplepace if j!=i for k in samplepace if (k!=j and k!=i)]
  # allcase=[(3,2,4)]
  satifyingcase=[]
  
  #3strike 충족하는 경우의 수는 1개뿐
  if(sorted_q[0][1]==3):
    print(1)
  else:
    
    #9*8*7 part
    for case in allcase:

      #in progress if meet wrong, goto next
      token_satisfied=1
      
      # print(case, end=' ')
      
      #N part, so total (9*8*7)*N
      for question in sorted_q:
        cnt_strike=0
        cnt_ball=0
        
        std_case=str(question[0])
        # print(std_case,end=' ')
        std_strike=question[1]
        std_ball=question[2]
        
        #3자리 비교; so total (9*8*7)*N*3*3 
        #본능적으로 3 for 극혐인데, 계산된 부분
        for idx_std, val_std in enumerate(std_case):
          for idx_case, val_case in enumerate(case):
            # print(idx_std,val_std,idx_case,val_case, end='/')
            if(int(val_std)==val_case):
              if(idx_std==idx_case):
                cnt_strike+=1
              else:
                cnt_ball+=1
        
        # print(cnt_strike,cnt_ball,end='/') 
        if(std_strike==cnt_strike and std_ball==cnt_ball):
          #retain the token
          pass
        else:
          token_satisfied=0
          
        # print(token_satisfied)
        if(token_satisfied==0):
          #breaking for question in sorted_q and get back to for case
          break
      
      #question for문 다 돌아도 token이 1이면 append
      if(token_satisfied):
        satifyingcase.append(case)
    
    # print(satifyingcase,len(satifyingcase))
    print(len(satifyingcase))

if __name__=="__main__":
  N=int(input())
  
  questions=[]
  for _ in range(N):
    questions.append(list(map(int,input().split())))
    
  # print(*questions,sep='\n')
  
  #이 경우, 중간에 3스트라이크라고 멈출 일은 없음,
  #결과적 완전탐색꼴로 짜되, 약간 부하를 줄이게
  # 스트라이크 순으로 정렬해서 3이면 바로 스탑
  
  sorted_q=sorted(questions,key=lambda x:x[1],reverse=True)
  # print(*sorted_q,sep='\n')
  
  #all case check and calcul cnt
  
  allcasecheckNcalculcnt(sorted_q)