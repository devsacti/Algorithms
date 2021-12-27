if __name__=='__main__':
    R,C =map(int, input().split())
    K=int(input())

    flags=[i for i in range(R*C,0,-1)]

    seat_matrix=[[0]*C for i in range(R)]

    # print(*seat_matrix,sep='\n')
    # print()

    directions=[[0,1],[1,0],[0,-1],[-1,0]]
    idx_directions=0

    max_x, max_y=(R-1),(C-1)
    nx, ny=0,0
    flag=flags.pop()

    while flag <= R*C:
        if(K>R*C):
            print(0)
            break

        seat_matrix[nx][ny]=flag
        if(flag==K):
            print(nx+1,ny+1)
            break

        dx=directions[idx_directions][0]
        dy=directions[idx_directions][1]

        for i in range(1):
            temp_nx=nx+dx
            temp_ny=ny+dy

            if(temp_ny>max_y or temp_ny<0 or temp_nx>max_x or temp_nx<0 or seat_matrix[temp_nx][temp_ny]>0):
                idx_directions+=1
                if(idx_directions==4):
                    idx_directions=0
            
            else:
                nx,ny=temp_nx,temp_ny
                flag=flags.pop()
            
            # print(*seat_matrix,sep='\n')
            # print()
