## template

import sys

def reverser(unit):
  global matrix
  
  idx_r=unit-1
  # print(matrix[idx_r])
  for idx,val in enumerate(matrix[idx_r]):
    # print(val)
    if(val==0):
      # print('ck')
      matrix[idx_r][idx]=1
    else:
      matrix[idx_r][idx]=0
  # print(matrix[idx_r])
  
  matrix=list(map(list,zip(*matrix)))
  # print(*matrix,sep='\n')
  
  idx_c=unit-1
  for idx,val in enumerate(matrix[idx_c]):
    if( val == 0):
      matrix[idx_c][idx]=1
    else:
      matrix[idx_c][idx]=0
  
  # common
  if(matrix[idx_r][idx_c]==0):
    matrix[idx_r][idx_c]=1
  else:
    matrix[idx_r][idx_c]=0
    
  matrix=list(map(list,zip(*matrix)))
  

if __name__=="__main__":
  N=int(sys.stdin.readline().strip())
  matrix=[]
  
  for _ in range(10):
    row=list(map(int, sys.stdin.readline().split()))
    matrix.append(row)
    
  units=[i for i in range(1,N+1)]
  
  # 행단위 칼럼단위하고 공통영역 재반복
  # 로봇으로 좌표
  # 둘다 스텝은 같지만 구현에서 차이
  
  # 파이썬에서 행렬은 트랜스포스트 이용하자
  
  # (행,열,공통)단위
  
  for unit in units:
    reverser(unit)
  
  for row in matrix:
    print(' '.join(map(str,row)))
  