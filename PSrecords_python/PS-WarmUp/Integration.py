# ps record components
# 1.problem reference
# 2.core algorithm, language
# 3.time complexity
# 4. ps ; accuracy, utilizing&Integrating algorithm for simulation, implementation

# code Integration for coding test
## caution
### shellow copy

### index

## lib
#basic
import string
#ascii_lowercaseList=string.ascii_lowercase

import math
#math.sqrt
#math.gcd
#math.lcm

# max, min, abs
min(-5, 3, 0, 3, -5, key=abs)
max(nums, key=abs)

# sorting with priority and bisect
e2 = sorted(a, key = lambda person : (person[0],person[2], -person[1]))
## 다중 정렬은 어떻게 구현할까? 
## 내 예상
## (1, 4, 1)
## (2, 3, 3)
## (2, 2, 3)
## (4, 1, 4)

##  우선 각 인스턴스의 0번째값으로만 인덱스 정렬, 그 다음 

from bisect import bisect_left
from bisect import bisect_right

# caution bisect_left right can output 'out of index' cuz this purpose is 'insert'
# nums  [1, 1, 2, 2, 4, 4, 4, 7, 7, 10]

# if print(bisect_left(nums,4)) and print(bisect_right(nums,4))
# index  0  1  2  3  4  5  6  7  8   9
#                    |                 => result is 4
#                             |           => result is 7
# left means that " 3 canbe inserted at 4 "
# right means that " 3 canbe inserted at 7 "
# insert 기준이라 반드시 left의 경우 반환된 인덱스와 그 좌우를 출력해봐야함
# 가령, bisect_left(nums,3)이면 없다가 아니라, 똑같이 인덱스 4를 출력함 그리고 3이 좌우에 없는경우도 살펴야함

# so if 11 was given left and right result is 10 which is out of range

# 출처: https://programming119.tistory.com/196 [개발자 아저씨들 힘을모아]
## and remind parameter binary search by custom function

from itertools import product
from itertools import combinations
from itertools import permutations
# product cases, combinations cases, permutations cases
sample=[i for i in range(1,n+1)]
sample2=[char for char in string.ascii_lowercase]
print(sample)
print(sample2)

allcases=list(product(sample,sample2))
#or
totalcases=list(product(samplespace,repeat=3))
print(allcases)

combinations_cases=list(combinations(sample,r))
print(combinations_cases)
print(len(combinations_cases))

permutations_cases=list(permutations(sample,r))
print(permutations_cases)
print(len(permutations_cases))

# dfs
from collections import defaultdict
# bfs
from collections import deque
# dijstra : bfs + priority queue(heap)
import heapq
## heapq는 오름차순으로 주어진 값을 정렬하는 최소힙
heap=[1,2,3,4,5]
heapq.heapify(heap)
# or
pq=[]
for item in heap:
    heapq.heappush(pq,item)
## 별도의 우선순위 산출을 통해, 가령 -, (0,origin9),(1,origin3) 등으로 재정렬 가능
for item in heap:
    heapq.heappush(pq,(-item,item))

## 특성상 pq[0]은 최소값이다. 현재 트리의 root
## 하지만, 방금 뽑아낸 값과 그 다음 트리의 root를 비교 시에 적합
## 다중정렬에는 부적합

# input
# import sys
# input=sys.stdin.readline

## skill
# base
# if 문 복수 조건 시 그 안에도 순서가 있다. L4_03; seatNotRecursive
# 다음 예제에서 볼 수 있듯이 a['nokey']처럼 존재하지 않는 키(nokey)로 값을 가져오려고
# 할 경우 a['nokey']는 Key 오류를 발생시키고 a.get('nokey')는 None을 돌려준다는 차이가 있다. 어떤것을 사용할지는 여러분의 선택이다.



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

        # 아래 폴문에서 '현재노드'기준 주변 노드로의 최단거리를 갱신했다, 근데, 그 목표노드가 다른 노드에서도 접근가능하기에 이런 
        # 필터를 통해 부하를 줄인다.
        if(candShortest>shortest[now]): continue
        else:
            
            for adj in graph[now]:
                interval,next=adj
                cost=candShortest+interval
                if(cost<shortest[next]):
                    shortest[next]=cost
                    heapq.heappush(pq,(cost,next))