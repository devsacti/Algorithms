## template
from math import gcd

if __name__=="__main__":
  N=int(input())
  
  position_1dvectors=[]
  for _ in range(N):
    position_1dvectors.append(int(input()))
    
  # print(position_1dvectors)
  
  distances=[]
  
  #distance 
  idx=0
  while(idx+1<N):
    start=position_1dvectors[idx]
    end=position_1dvectors[idx+1]
    distances.append(end-start)
    idx+=1
  
  # print(distances)
  #finding total gcd
  #gcd argument requires 2 arguments
  idx=1
  totalgcd=0
  len_distances=len(distances)
  while(idx<=(len_distances-1)):
    # print(totalgcd)
    if(idx==1):
      start=distances[idx-1]
      end=distances[idx]
      totalgcd=gcd(start,end)
      # print(totalgcd)
      idx+=1
    else:
      next=distances[idx]
      totalgcd=gcd(totalgcd,next)
      idx+=1
  
  # print(totalgcd)
  
  totalcnt_tree=1+(position_1dvectors[-1]-position_1dvectors[0])//totalgcd
  addtionaltree=totalcnt_tree-N
  print(addtionaltree)

