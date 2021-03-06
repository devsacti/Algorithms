# 하나의 탑에서 발사된 레이저 신호는
# 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다.
 
# 예를 들어 
# 높이가 6, 9, 5, 7, 4인 다섯 개의 탑이 수평 직선에 일렬로 서 있고,
# 모든 탑에서는 주어진 탑 순서의 반대 방향(왼쪽 방향)으로
# 동시에 레이저 신호를 발사한다고 하자.
# 
# 그러면, 
# 높이가 4인 5 번째 탑의 신호는 높이가 7인 네 번째 탑이 수신을 하고,
# 높이가 7인 4 번째 탑의 신호는 높이가 9인 두 번째 탑이,
# 높이가 5인 3 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신을 한다.
# 높이가 9인 2 번째 탑과 
# 높이가 6인 첫 번째 탑이 보낸 레이저 신호는 어떤 탑에서도 수신을 하지 못한다.
#
# 탑들의 개수 N과 탑들의 높이가 주어질 때,
# 각각의 탑에서 발사한 레이저 신호를 어느 탑_의 1부터시작하는 서수_에서 수신하는지를 알아내는 프로그램
#
# 느낌상, 일반적인 방법_리버스하고 팝하고 뭐 이것저것_으로 풀면 바로 타임리밋걸리게 되는문제라
# 어떻게든 스택을 써야할것으로 보임
# 역순과 관련있는듯
# ->일단 뒤에서부터 push해보니까 원리가 보인다 
# ->아쉽게도 calcul stack상에서 조건충족하는 쌍으로 빼면 해결될줄 알았는데
# 그 쌍에서 또 윗을 뒤에서 써야함, 다른 접근 필요

# 파이썬의 강점을 쓰자면, calcul stack을 deque로 선언해서 충족하는 아래
# 탑을 그때마다 dequeue해서 풀리기도 함.
# ->이것도 중간층 해결이 다소 복잡

# 이것저것 스택을 통한 연산이나 변환이 다 애매한데,
# 설마 여기서 스택의 역할이 겨우 reversed인가
# 근데 그러면 그냥 index를 역순으로 접근해도 풀릴텐데

# 다시 스택을 통한 연산에 집중, 기준을 toplist앞쪽에서 방금뺀 item을
# 기준으로 calculstack에 있는걸 비우니까_쓸모없는걸 비우니까_
# 라인 28의 문제가 생각보다 쉽게 해결된다더라

import sys
from collections import deque

if __name__=="__main__":
    N = int(sys.stdin.readline().strip())
    top_list = list(map(int, sys.stdin.readline().split()))

    calcul_stack = []
    answer = []

    for i in range(N):
        # 일단 stack에 뭔가 있어서 비교해볼만함
        while calcul_stack:
            # 스택에 깔려있는 탑의 높이가 더 높아서 수신가능,
            # 어쩌면 추후에도 사용가능할지 모르니, 냅두고
            # 1부터 시작하는 서수니까 +1
            if calcul_stack[-1][1] > top_list[i]:  
                answer.append(calcul_stack[-1][0] + 1)
                break
            else:
                #현재 top의 높이 기준 무쓸모 탑은
                # 최소한 현재 top이 그 수신역할을 꾀차기 때문에
                # 어떤 경우도 무쓸모
                calcul_stack.pop()
        # 스택이 초기화되거나 쓸모없는게 pop되다가 빈 경우,
        # 레이저를 수신할 탑이 없다.
        if not calcul_stack:  
            answer.append(0)
        calcul_stack.append([i, top_list[i]])

    print(" ".join(map(str, answer)))

