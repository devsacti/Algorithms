## template
import sys

freq_num={}

cand_mode=[]
max_freq=-100

if __name__=="__main__":
  nums=[]
  
  for _ in range(10):
    num=int(sys.stdin.readline().strip())
    nums.append(num)
    
    if num not in freq_num.keys():
      freq_num[num]=1
    else:
      freq_num[num]+=1
  
  # print(freq_num)    
  max_val=max(freq_num.values())
  # print(max_val)
  cand_mode=[k for k,v in freq_num.items() if v ==max_val]
  
  # print(cand_mode)
    
  mean_nums=sum(nums)/len(nums)
  print(int(mean_nums))
  print(min(cand_mode))