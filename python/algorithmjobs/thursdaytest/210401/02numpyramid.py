## template
import sys

if __name__=="__main__":
  N,S = map(int,sys.stdin.readline().split())
  
  samplespace=[i for i in range(1,10)]

  s_idx=samplespace.index(S)
  
  equallimit=N*N
  cnt_sampling=1
  
  nums=[]
  while(cnt_sampling<=equallimit):
    nums.append(samplespace[s_idx%9])
    
    s_idx+=1
    cnt_sampling+=1
  
  # print(nums)
  
  matrix=[]
  s_idx_nums=0
  underend_idx_nums=0
  for i in range(N):
    interval=2*i+1
    underend_idx_nums=s_idx_nums+interval
    
    row=nums[s_idx_nums:underend_idx_nums]
    if(i%2==0):
      row=list(reversed(row))
    matrix.append(row)
    
    s_idx_nums=underend_idx_nums
  
  # print(matrix)
  
  for i in range(N):
    spaces=' '*((N-1)-i)
    print(spaces,end='')
    print(''.join(map(str,matrix[i])))