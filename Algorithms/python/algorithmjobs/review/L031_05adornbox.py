## template

import sys

# NO를 여집합으로 설정하는 게 느낌상 유리
# NO condtion
# 1, paper is short 5,4,3,2,1,0
# 2, at last, one color can be used maximum 2, but if after cut off more than 3
# and left total num of paper is less than 6? it is no
# 1~2->1.5 after cut off more than 2, and total num is under 6 is wrong
# 
# other no condition is not seen at now.


if __name__=="__main__":
  num_kinds=int(sys.stdin.readline().strip())
  colors=list(map(int,sys.stdin.readline().split()))
  
  # print(num_kinds,colors)
  
  #dict of colors
  dict_colors=dict()
  
  for color in colors:
    if color not in dict_colors.keys():
      dict_colors[color]=1
    else:
      dict_colors[color]+=1
      if(dict_colors[color]>2):
        dict_colors[color]=2
        
  #get all value of dict
  sum_preprocessedtotal=sum(dict_colors.values())
  # print(dict_colors, sum_preprocessedtotal)
  
  if(sum_preprocessedtotal<6):
    print('NO')
  else:
    print('YES')