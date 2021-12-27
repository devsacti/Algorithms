from collections import deque
'''파이썬에는 heapq로 heap이 제공된다고 한다. 쩐다'''

# list의 0번째는 안쓰는 형태
# cursor of next place where element is empty(cursor_next)는 그래서 1부터 시작이다.

# 개괄
# 트리에 insert, remove할 함수 2개
        
class PriorityQueue:
    MAX=10
    Tree=[0]*MAX
    lencursor_next=1

    def push( self,child ):
        # elaborately, insert of heap
        self.Tree[self.lencursor_next]=child
        self.lencursor_next+=1

        idx_child=self.lencursor_next-1
        # 새로 들어온 값의 인덱스와 그 부모 인덱스 사이에는
        # left child index의 /2 그리고 right child index에서 -1하고 /2
        # 종합하면, //2

        # 그리고 이러한 시행이 1번이 아니라, 새로 바뀐자리에서 또 부모랑 비교하다가
        # 루트까지 가나 안가나 확인해야
        while(idx_child >1):
            idx_parent= idx_child//2
            # again, 현재는 작은 값이 위로가게 설계된 상황
            if (self.Tree[idx_child] < self.Tree[idx_parent]):
                tmp=self.Tree[idx_child]
                self.Tree[idx_child]=self.Tree[idx_parent]
                self.Tree[idx_parent]=tmp
            else:
                break

            idx_child=idx_parent

    def pop( self):
        # elaborately, remove of heap
        # 이 때, 루트의 값을 빼고, root의 child들을 비교하면서 빈 공간을 
        # 채워가는 방식을 생각할 수 도 있지만,그렇게 아래서 위를 채우는 과정의
        # 복잡성보다 
        # 그냥 맨마지막 값을 일단 맨위로 올린뒤, 비교해서 위에서 아래로 다시 
        # 정렬하는 복잡성이 더 낮아서 후자로 구현되는듯하다.
        
        # 우선 탑값을 따로 빼놓는다.
        val_pop=self.Tree[1]
        # 탑과 마지막 값 교환
        self.Tree[1]=self.Tree[self.lencursor_next-1]
        self.Tree[self.lencursor_next-1]=0
        self.lencursor_next=self.lencursor_next-1

        idx_parent=1
        while(1):
            # 자식들 비교해서 가야할 왼쪽 오른쪽 판단
            # left는 index of parent *2, right는 (index of parent)*2+1
            # 한편, 같은경우 나는 그냥 right로 넘김

            # 별개로 만약 왼쪽 오른쪽 중 1개 가없다면, 더불어 초기화가 0이라면
            # 초기화값인데, 없음을 상징하는 0인데 우선순위가 높다고 판단 오류
            # 1. 그냥 초기화를 99999로 하거나, 세련되게는 좌우확인

            # 좌우확인할때, 있는그대로 값을 참조해서 초기값이면 없다고 할수있는데,
            # 더 요령있게하면 lencursor_next empty의 범위를 활용한다.
            
            idx_destiny=-1

            l_idx_child=idx_parent*2
            r_idx_child=idx_parent*2+1
            
            # 좌우 모두 없는 경우; 한쪽만 있는경우;양쪽있는경우
            # 근데 여기서 완전이진트리라는 전제에 의해, 한쪽만 있는 경우는 left에 존재하는 경우만 존재
            if(self.lencursor_next <= l_idx_child):
                break
            elif(1 <= l_idx_child and l_idx_child < self.lencursor_next and self.lencursor_next<=r_idx_child):
                idx_destiny=l_idx_child
            else:
                if( self.Tree[l_idx_child] < self.Tree[r_idx_child] ):
                    idx_destiny=l_idx_child
                elif( self.Tree[l_idx_child] >= self.Tree[r_idx_child] ):
                    idx_destiny=r_idx_child
            
            if( self.Tree[idx_parent] > self.Tree[idx_destiny]):
                tmp=self.Tree[idx_destiny]
                self.Tree[idx_destiny]=self.Tree[idx_parent]
                self.Tree[idx_parent]=tmp
                
                idx_parent=idx_destiny
            else:
                break

        return val_pop

    def top(self):
        # 아래와같은 꼴은 알수없는 None을 출력하게 해서 안함
        # 아 내 의도는 알겠지만, main의 프린트까지
        #  print(print(self.Tree[1)) 로 프린트가 2번되서 바깥 print가 None
        # print(self.Tree[1])
        return self.Tree[1]

if __name__=="__main__":
    myPQ=PriorityQueue()

    myPQ.push(3)
    myPQ.push(5)
    myPQ.push(88)

    print('ck1')
    print(myPQ.Tree)
    print('ck2')
    print(myPQ.top())
    print('ck3')
    print(myPQ.Tree)
    print('ck4')
    poped_val=myPQ.pop();print(poped_val)
    print(myPQ.Tree)
    print('ck5')
  