'''
step1 input, flags;ex 1~42

!graph
step2
step2.1 searchnext

step2.2 best place and move

    #idx_r, idx_y 대용
    max_x, max_y=(R-1),(C-1)
    x, y = current

    #checking
    matrix[x][y]=flag
    flag+=1
    
    #searchnext, search할때 패턴따라가야 큐 정렬과정이 없거나 편함
    candidateplace=deque()

    #searchnext changer tokens
    # searchchangertoken_x=[i for i in range(R,int(R/2),-1)]
    # searchchangertoken_y=[j for j in range(0,int(C/2))]
    # tokens=list(zip(searchchangertoken_x,searchchangertoken_y))

    dx=[1,0,-1,0]
    dy=[0,-1,0,1]

    for i in range(len(dx)):
        nx=x+dx[i]
        ny=y+dy[i]

        if(ny>max_y or ny<0 or nx>max_x or nx<0):
            continue

        if(matrix[nx][ny]!=0):
            continue

        candidateplace.append([nx,ny])
    
    if(len(candidateplace)==0):
        candidateplace.append([-1,-1])
    
step2.3 again until no place

?greedy, 근데 커브길에서 조건을 모르겠음
->행렬좌측아래부터 오른쪽위 +1씩인줄알았는데 특정 구간동안 탐색 순서가 바뀌어야
->우하좌상 시 탐색 순서 변환 구간보다 상우하좌 탐색 순서 변환 필요구간이 더 쉽다, 일종의 치환
->아에 초기 매트릭스에 일단 ifelse 2중 꼴로 변환구간 표시하면 될듯함, 근데 어렵

->그래서 반시계방향 90도 아이디어로 접목
    #매트릭스 반시계로 90도
    matrix=list(zip(*matrix))
    matrix=[list(row) for row in reversed(matrix)]
->결국 시작점 카운트에서 같은 본질적 문제 종착; 어디서부터 전환인가

step2
step2.1 fill the map
step2.2 find the k

'''
from collections import deque


def walker(matrix, current, flag,K):
    # print(*matrix,sep='\n')
    # print()

    #break of recursive;기저 조건
    if(current==[-1,-1]):
        return

    R=len(matrix)
    C=len(matrix[0])

    #idx_r, idx_y 대용
    max_x, max_y=(R-1),(C-1)
    x, y = current
    
    #searchnext, search할때 패턴따라가야 큐 정렬과정이 없거나 편함
    candidateplace=deque()

    if(matrix[x][y]==-1):
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]
    else:
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]

    for i in range(len(dx)):
        nx=x+dx[i]
        ny=y+dy[i]

        if(ny>max_y or ny<0 or nx>max_x or nx<0):
            continue

        if(matrix[nx][ny]>0):
            continue

        if(matrix[nx][ny]==-1):
            candidateplace.append([nx,ny])
            #print(candidateplace)

        candidateplace.append([nx,ny])
    
    if(len(candidateplace)==0):
        candidateplace.append([-1,-1])

    #checking
    matrix[x][y]=flag
    if(flag==K):
        print(x+1,y+1)

    flag+=1

    #move
    walker(matrix, candidateplace.popleft(),flag,K)


if __name__=='__main__':
    R,C =map(int, input().split())
    K=int(input())

    flags=[i for i in range(R*C,0,-1)]

    seat_matrix=[[0]*C for i in range(R)]
    #print(*seat_matrix,sep='\n')

    startidx=0
    endidx=(C-1)

    for n, row in enumerate(seat_matrix,1):
        
        if(n>int(R/2) or endidx-startidx<1):
            break

        for idx in range(startidx,endidx+1):
            row[idx]=-1
        
        # for i,element in enumerate(row):
        #     if(i>=startidx and i<=endidx ):
        #         element=1        
        startidx+=1
        endidx-=1

    seat_matrix=list(reversed(seat_matrix))
    # print('--')
    # print(*seat_matrix,sep='\n')

    startidx=0
    endidx=(C-1)

    for n, row in enumerate(seat_matrix,1):
        
        if(n>int(R/2) or endidx-startidx<1):
            break

        for idx in range(startidx,endidx+1):
            row[idx]=-1
        
        # for i,element in enumerate(row):
        #     if(i>=startidx and i<=endidx ):
        #         element=1        
        startidx+=1
        endidx-=1
    
    print('--')
    print(*seat_matrix,sep='\n')

    seat_matrix=list(reversed(seat_matrix))

    # print('--')
    # print(*seat_matrix,sep='\n')

    walker(seat_matrix,[0,0],1,K)

