## template
from collections import deque

if __name__=="__main__":
  N,S= map(int, input().split())
  
  cnt_nums=N*N
  #제거될 10까지 생각해서 숫자들 출력
  #총 갯수, N*N+N*N//10 가 아니었음
  #눈에 보이는 N*N
  #안보이는 (N*N-짜투리)//9 가 숨겨진 10의 갯수가 아님, 마지막이 1~8이어도 10가짐
  #눈에 보이는 N*N개의 숫자에서 1의 갯수가 숨겨진 10의 갯수, 1이면 10을 거친것 무조건
  #복잡하게 계산하면 N*N을 9씩 묶었을때 몫의 갯수와 앞 짜투리 뺀 N*N을 %9했을 때 나머지가 있냐 없냐로 
  # 숨겨진 10을 포함한 전체 length를 구할 수 있겠는데, 그짓할바엔 그냥 눈에 보인느대로 할걸
  # 일단 발견한 규칙성 활용
  
  # def rest(), 그냥 if로 떼우자
  plusalpha=0
  if(( N*N-(9-(S-1)) )%9==0):
    plusalpha=0
  else:
    plusalpha+=1
    
  nums=[num for num in range(S, (S+N*N)+( ( N*N-(9-(S-1)) )//9 )+plusalpha  ) if num%10!=0]
  # print(nums, len(nums))
  
  nums=list(map(lambda x:x%10, nums))
  # print(nums, len(nums))
  
  dq_nums=deque(nums)
  matrix=[]
  
  cnt_poplefts=[2*i-1 for i in range(1,N+1)]
  # print(cnt_poplefts)
  
  for cnt in cnt_poplefts:
    token_reverse=0
    if(((cnt+1)//2)%2==1):
      token_reverse=1
      
    row=[]
    while(cnt>0):
      row.append(dq_nums.popleft())
      cnt-=1
    # print(dq_nums)
    
    if(token_reverse):
      row=list(reversed(row))
    # print(row)
    
    matrix.append(row)
    # print(*matrix, sep='\n')
  
  # print(*matrix, sep='\n')
  
  for i in range(N):
    space=' '*((N-1)-i)
    print(space,end='')
    print(''.join(map(str,matrix[i])))
    
    
    