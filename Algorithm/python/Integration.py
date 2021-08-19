# ps record components
# 1.problem reference
# 2.core algorithm, language
# 3.time complexity
# 4. ps ; accuracy, utilizing&Integrating algorithm for simulation, implementation

# code Integration for coding test

## lib
#basic
import string
#ascii_lowercaseList=string.ascii_lowercase

import math
#math.sqrt
#math.gcd
#math.lcm

from itertools import product
from itertools import combinations
from itertools import permutations

# dfs/bfs
from collections import defaultdict
from collections import deque
#dijkstra
import heapq

#input
# import sys
# input=sys.stdin.readline

## skill
# base
# if 문 복수 조건 시 그 안에도 순서가 있다. L4_03; seatNotRecursive
# 다음 예제에서 볼 수 있듯이 a['nokey']처럼 존재하지 않는 키(nokey)로 값을 가져오려고
# 할 경우 a['nokey']는 Key 오류를 발생시키고 a.get('nokey')는 None을 돌려준다는 차이가 있다. 어떤것을 사용할지는 여러분의 선택이다.

# sorting list 
e2 = sorted(a, key = lambda person : (person[0],person[2], -person[1]))
min(-5, 3, 0, 3, -5, key=abs)
max(nums, key=abs)

# product cases, combinations cases, permutations cases
sample=[i for i in range(1,n+1)]
sample2=[char for char in string.ascii_lowercase]
print(sample)
print(sample2)

allcases=list(product(sample,sample2))
print(allcases)

combinations_cases=list(combinations(sample,r))
print(combinations_cases)
print(len(combinations_cases))

permutations_cases=list(permutations(sample,r))
print(permutations_cases)
print(len(permutations_cases))

## algorithm templetes
#bruteforce
def judge(result,depth,inequals):
    window=result[depth-1]+inequals[depth]+result[depth]
    return eval(window)

def bruteforce(result,depth,limit, inequals):
  if(depth>=limit):
    print('arrive')
    # print(result)
  else:
    for numchar in '123456789':
      result[depth]=numchar
      print(' '*depth,end='')
      print('given',result)
      print(' '*depth,end='')
      print('depth',depth)

      if(depth==0):
        bruteforce(result[:],depth+1,limit, inequals)
      
      result[depth]='*'
      print(' '*depth,end='')
      print('remove',result)
      print(' '*depth,end='')
      print('depth',depth)
      print('--')
      
        
      # else:
      #   token=judge(result,depth,inequals)
      #   print(token)
      #   if(token):
      #     bruteforce(result[:],depth+1,limit, inequals)
      #   else:
      #     return

#dynamic programming
def dpMarble(nums):
    # init table and items of table
    length=len(nums)
    dptable=[0]*length
    minusdptable=[0]*length

    dptable[1]=1;dptable[2]=1
    CANDs=[nums[1]+nums[3],nums[1]+nums[2],nums[2]+nums[3]]
    dptable[3]=max(CANDs)

    for i in range(5,n+1):
        #sub problems
        tokens=[]
        # 철수가 주어진 n개에 대해 1개,2개,3개 선택시 남은 갯수가 패턴상
        # 승리패턴인지 패배패턴인지 판단가능
        if(dptable[i-1]==1): tokens.append(0)
        else: tokens.append(1)        

        if(dptable[i-2]==1): tokens.append(0)
        else: tokens.append(1)

        if(dptable[i-3]==1): tokens.append(0)
        else: tokens.append(1)

        CANDs=[dptable[i-1],dptable[i-2]+nums[i],dptable[i-3]+nums[i-1]+nums[i]]
        
        dptable[idx]=max(dptable[idx-1]*nums[idx],nums[idx])
        # expansion part of kadene
        if(abs(minusdptable[idx-1]*nums[idx])>abs(nums[idx])):
            minusdptable[idx]=minusdptable[idx-1]*nums[idx]
        else:
            minusdptable[idx]=nums[idx]

        dptable[idx]=max(minusdptable[idx-1]*nums[idx],nums[idx])


        dptable[i]=max(tokens)

    return dptable[n]

def dfs(graph,v,visited,*arg):
    visited[v]=1

    for adj in graph[v]:
        if(visited[adj]==0):
            dfs(graph,v,visited,*arg)
        else: continue

def bfs(graph,s,visited,*arg):
    visited[s]=1
    q=deque();q.append(s)
    
    while(q):
        now=q.popleft()

        for adj in graph[now]:
            if(visited[adj]==0):
                visited[adj]=1
                q.append(adj)
            else: continue

def dijkstra(graph,s,shortest,*arg):
    # visited 처럼, 해석하면 안됨, 이 문제는 visited는 논외이고,
    # 최단거리를 도출하기 위한 적절한 초기화과정으로 이해해야함, 아래 2 스텝을 이해하기 위해
    shortest[s]=0
    ## 시작점 관련해서는 출입문이 2개이고 0과 20이라고 하자
    ## 그리고 초기화는 20으로 되있어서 부득이 내가 0으로 기입한 상황
    pq=[];heapq.heappush(pq,(0,s))

    while(pq):
        # pop >> try moving to 'now' and check cand interval
        candShortest, now = heapq.heappop(pq)

        # '다음 노드'까지의 최단거리를 찾는과정
        # 1. 현재 노드까지의 거리가 최단거리인가
        # 2. 그렇다면, 현재 위치에서 다음 노드를 접근할때의 코스트가 최단거리인다.
        
        # 특히 , 시작점에 진입하는 경우, 아래 if가 다소 모호하다 왜냐하면 다른 진입경로가 없다고 생각하기 쉬우니
        # 그러니까 앞선 전제와같이 20과 0이 있고, 20으로 초기화 되어있을때, 아래와 같은 if를 사용하고

        # 시작점이 아닌 점부터는 러프한 틀, 그리고 추가 판단은 아래 if에서 한다고 이해하자
        if(candShortest>shortest[now]): continue
        else:
            
            for adj in graph[now]:
                cost=candShortest+adj[1]
                if(cost<shortest[adj[0]]):
                    shortest[adj[0]]=cost
                    heapq.heappush(pq,(cost,adj[0]))