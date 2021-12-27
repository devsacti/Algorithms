'''
thursday test.pyramid is reflected
'''

## template
if __name__=="__main__":
  N,S =map(int, input().split())
  
  #utilize queue
  queue=[i for i in range(1,10)]
  
  nums=[]
  idx_start=queue.index(S)
  
  limit=N*N
  while(limit>0):
    nums.append(queue[(idx_start%len(queue))])
    idx_start+=1
    limit-=1
  
  # print(nums)
  
  matrix=[]
  sidx_section=0
  eidx_section=0
  for i in range(N):
    len_row=2*i+1
    eidx_section=sidx_section+len_row
    row=nums[sidx_section:eidx_section]
    if(i%2==0):
      row=reversed(row)
    matrix.append(row)
    sidx_section=eidx_section
  
  # print(*matrix,sep='\n')
  for i in range(N):
    spaces=' '*((N-1)-i)
    print(spaces, end='')
    print(''.join(map(str,matrix[i])))
    
  