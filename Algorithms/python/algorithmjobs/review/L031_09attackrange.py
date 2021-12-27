## 처음에는 모든 좌표를 방문해서 기준좌표와의 가로세로 길이가 R안에 들어가나를 판단해서품,
# 이것저것 따져보면 이것도 나름 최적화인데
# 이번에는 범용성을 생각해서 로봇형태로+재귀인데 너무 어렵다 익숙해지긴 해야..
import sys

def checkerRange(depth_search,idx_r,idx_c,R):
  global matrix
  global std_r,std_c
  global N
  
  if(depth_search>R):
    return
  
  else:
    # print('curidxs',idx_r,idx_c, end='/')
    
    #flag init
    # print('depth ',depth_search,end='/')
    flag=depth_search
    if(depth_search==0):
      flag='x'
    else:
      flag=depth_search
      
    matrix[idx_r][idx_c]=flag
    visited_matrix[idx_r][idx_c]=1
    # print('curval',matrix[idx_r][idx_c])
    # print(*matrix, sep='\n')
    
    #direction EWSN 0 3 and magnitude 1
    kinds_direction=4
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    
    for d in range(kinds_direction):
      cand_idx_r=idx_r+dr[d]
      cand_idx_c=idx_c+dc[d]
      
      # print('cand',cand_idx_r,cand_idx_c)
      
      if(cand_idx_r<0 or cand_idx_r>(N-1) or cand_idx_c<0 or cand_idx_c>(N-1)):
        continue
      
      #visited, val is not 0->다른 경로와 중첩되는 구간에서 logic fellow 발생
      #       [0, 0, 0, 0, 0, 0, 0, 0]
      #       [0, 0, 0, 3, 0, 3, 0, 0]
      #       [0, 0, 3, 2, 3, 2, 3, 0]
      #       [0, 3, 2, 1, 'x', 1, 2, 3]
      #       [0, 0, 3, 2, 3, 2, 3, 0]
      #       [0, 0, 0, 3, 0, 3, 0, 0]
      #       [0, 0, 0, 0, 0, 0, 0, 0]
      #       [0, 0, 0, 0, 0, 0, 0, 0]
      # 좌우에서 방문해서 남긴 flag로 인해 남북이 제한됨, 현재로썬 플래그값이 있어도 갈곳은 가야하는데...
      # 직관적으론 이전 방문 좌표 모두를 저장해야...
      # 좀 투박하지만 문제가 되는 direction을 조건으로 not continue하게 해보자
      # 남북의 경우 not continue 할 경우, 길은 뚫리는데 갱신되면 안되는 북이나 남의 문제발생
      # 일단 전통적인 visited를 선언하자
      # 근데 어쨌거나 다른 노드에서 접근했다 안했다로는 똑같은 문제 발생...당연하게도..
      # 방문했다 equal flag니까...
      # depth를 통해서 길을 뚫어보자, 되긴 되는데 거시기 하네
      
      # 안됨, dfs 구조상 좌우 어디론 가 먼쩌 프랙탈 처럼 뻗어나가면서 형태가 이상하고
      # flag값이 작으면 갱신가능으로 해서 어찌 값은 조정가능해보이는데...
      
      if(depth_search==0):
        pass
      else:
        if(matrix[cand_idx_r][cand_idx_c] != 0):
          continue
      
      # print('cur, cand',idx_r,idx_c,'/',cand_idx_r,cand_idx_c)
      checkerRange(depth_search+1,cand_idx_r,cand_idx_c,R)
  

if __name__=="__main__":
  N=int(sys.stdin.readline().strip())
  
  X,Y,R=map(int,sys.stdin.readline().split())

  global std_r,std_c
  std_r=X-1
  std_c=Y-1
  
  # print(N,X,Y,R)
  global matrix, visited_matrix
  matrix=[[0]*N for _ in range(N)]
  visited_matrix=[[0]*N for _ in range(N)]
  
  # print(*matrix, sep='\n')
  
  depth_search=0
  idx_r=X-1
  idx_c=Y-1
  checkerRange(depth_search,idx_r,idx_c,R)
  # print(*matrix, sep='\n')
  
  for row in matrix:
    print(' '.join(map(str,row)))