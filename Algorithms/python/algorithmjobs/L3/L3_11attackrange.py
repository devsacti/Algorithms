'''
1. dfs/bfs
step1 input

step2 recursive 4way round
step2.1 stop condition : range of map, condition limit of R, visited, deque
step2.2 value of current position = value of past position+1

step3 change start position to 'x'

? 끝이 명확하게 있으니 dfs?
bfs 기본은 최단거리, 현재위치 1칸식 모든 지점, 대표적으로 미로찾기
dfs 지나온 길에 대한 정보가 중첩적(재귀적)으로 필요할때, 재귀적 구조 상 데이터 커지면 런타임에러뜸


?!dfs/bfs 아니면 어떻게 풀지
2. R이 고정이라 경로라는 걸 생각안하고 그냥 그리디하게
-> 좌우하상, 대각선은 그렇다 치는데, 나머지는 어떻게 갱신?
-> 기준점과 주변 점 사이의 dx+dy로 좌표값 갱신가능해보임.

?의도한 바가 따로 있을까?
왼쪽 출력 기준으로 위아래 이동하면 대각선도 아니고 직선도 아닌 애들 해결가능
경계 처리를 위해 배열의 길이 유념

?적용가능한 알고리즘이 끝날때까지 1개이면 상관없지만 쉬운 길이 나오면?
다양한 문제방법은 복잡한 문제에 대해 최적화되면서 축약됨,
일단 지금은 연습

'''
def makefield(matrix,X,Y,R):

    N=len(matrix)

    for x in range(N):
        for y in range(N):
            dx=x-(X-1)
            dy=y-(Y-1)

            len_path=abs(dx)+abs(dy)

            if(len_path<=R):
                if(len_path==0):
                    matrix[x][y]='x'
                else:
                    matrix[x][y]=len_path
            else:
                continue

    return matrix




if __name__=='__main__':

    # 6 <= N <= 100
    N=int(input())

    X,Y,R=map(int,input().split())

    matrix=[[0]*N for _ in range(N)]

    matrix=makefield(matrix,X,Y,R)

    for row in matrix:
        print(' '.join(map(str,row)))

