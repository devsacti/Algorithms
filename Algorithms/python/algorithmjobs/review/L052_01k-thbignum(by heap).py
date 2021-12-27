import sys
import heapq

# 참고 링크 https://www.daleseo.com/python-heapq/

if __name__=="__main__":
    # K : Not computer INDEX 1~
    N,K = map(int, sys.stdin.readline().split())
    nums=list(map(int, sys.stdin.readline().split()))

    # 처음에 '앞으로' 힙으로 작동할 리스트로 정의
    heap=[]

    # heap 원소 추가 삭제, 루트값 조회
    # heapq.heappush(heap, 4)
    # heapq.heappush(heap, 1)
    # heapq.heappush(heap, 7)
    # heapq.heappush(heap, 3)
    # print(heap)
    # 출력 결과; [1, 3, 7, 4]
    # print(heapq.heappop(heap))
    # print(heap)
    # print(heap[0])

    # heap 초기화 2
    # heap = nums
    # heapq.heapify(heap)
    # print(heap)
    # [1, 3, 5, 4, 8, 7]

    # 한편, 파이썬에서는 최소 힙(우선순위==작은 값)만 지원하는데,
    # 인풋값을 음수화한다던지 별도의 연산(별개의 우선순위 와 값)을 통해 인풋값의 우선순위를 뒤집어서 힙에 넣으면 된다.
    # nums = [4, 1, 7, 3, 8, 5] -> nums = [-4, -1, -7, -3, -8, -5]
    # 가장 우선순위가 컸던 1은 제일 우선순위가 작아진다. -8 <-1 이므로
    # heapif결과
    # [1, 3, 5, 4, 8, 7] => [-8, -7, -5, -4, -3, -1]
    # 이를 응용해서 '변화된 우선순위'와 '본래 값'을 튜플로 저장해서 출력 시
    # 역전된 우선순위에 따라서 값을 출력하게 한다.

    # k 번째로 "큰 값" -> 최대 힙
    for num in nums:
      heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

    # print(heap)

    # while heap:
    #   print(heapq.heappop(heap)[1], end=' ')  # index 1
    # 10 8 7 5 4 3 3 2 2 1

    kth_max = None
    for _ in range(K):
        kth_max=heapq.heappop(heap)

    print(kth_max[1])