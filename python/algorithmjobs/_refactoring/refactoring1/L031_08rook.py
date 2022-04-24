## template
# 처음에는 룩의 위치에 따른 행과 열 탐색으로 풀었는데, 
# 이번에는 좀더 직관적인 로봇형태로

# 정리하자면, 로봇이 직관적이지만, 이 경우 
# 룩 위치에 따라 4방면 4번만, 경로에 1이 있나 없나, 그리고 그 사이에 3이 있나정도뿐이라
# 첫번째도 꽤 적합한듯, 범용성이 딸려도, 간단한 문제를 간단하게 푸는걸수도,
# 특히 파이썬은 transpose가 한결쉬워서 

import sys

def rook(position):
  global matrix
  global token_kingcatched

  # direction EWSN 0~3
  kinds_dir=4
  dr=[0,0,1,-1]
  dc=[1,-1,0,0]
  
  for d in range(kinds_dir):
      
    idx_r=position[0]
    idx_c=position[1]
    # print('init ',idx_r,idx_c)
    
    # magnitude of vector of rook is flexible
    # ->while(1) and relavant break
    while(1):
      candi_idx_r=idx_r+dr[d]
      candi_idx_c=idx_c+dc[d]
      # print('candi ', candi_idx_r,candi_idx_c, end='/')
      
      if(candi_idx_r<0 or candi_idx_r>(N-1) or candi_idx_c<0 or candi_idx_c>(M-1)):
        break
      
      if(matrix[candi_idx_r][candi_idx_c]=='3'):
        break

      if(matrix[candi_idx_r][candi_idx_c]=='1'):
        token_kingcatched=True
        break
      
      #after this line, there is no 'out of boundary','obstacle','king'
      # so move
      idx_r=candi_idx_r
      idx_c=candi_idx_c
      # print('result', idx_r,idx_c)
      
    if(token_kingcatched):
      break
      
if __name__=="__main__":
  N,M=8,8
  
  matrix=[]
  for _ in range(N):
    row=sys.stdin.readline().split()
    matrix.append(row)
    
  # print(*matrix,sep='\n')
  
  global token_kingcatched
  token_kingcatched=False
  
  positions=[]
  for idx_r in range(N):
    for idx_c in range(M):
      if(matrix[idx_r][idx_c]=='2'):
        positions.append( (idx_r,idx_c) )
        
  # print(positions)
  
  for position in positions:
    rook(position)
    
  if(token_kingcatched):
    print(1)
  else:
    print(0)
  
  