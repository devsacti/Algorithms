## template
import sys

def check_adjacent(matrix, ci_r,ci_c):
  global r,c
  cnt_mine=0
  
  if(matrix[ci_r][ci_c]==1):
    print('game over')
  else:
      kinds_dir=8
      dr=[0,0,1,-1,1,1,-1,-1]
      dc=[1,-1,0,0,1,-1,1,-1]
      
      for d in range(kinds_dir):
        cand_cir=ci_r+dr[d]
        cand_cic=ci_c+dc[d]
        
        if(cand_cir<0 or cand_cir>=r or cand_cic<0 or cand_cic>=c):
          continue
        
        if(matrix[cand_cir][cand_cic]==1):
          cnt_mine+=1
      
      
      print(cnt_mine)
      
if __name__=="__main__":
  
  r,c =map(int, sys.stdin.readline().split())
  
  ri_r,ri_c=map(int, sys.stdin.readline().split())
  ci_r,ci_c= ri_r-1, ri_c-1
  
  matrix=[]
  for _ in range(r):
    row=list(map(int, sys.stdin.readline().split()))
    matrix.append(row)
    
  check_adjacent(matrix, ci_r,ci_c)