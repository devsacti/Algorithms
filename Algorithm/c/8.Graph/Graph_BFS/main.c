#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define QSize 10

int graph[8][8]={
    {0,1,1,1,0,0,0,0},
    {1,0,0,1,1,0,1,0},
    {1,0,0,1,0,0,0,0},
    {1,1,1,0,0,1,0,0},
    {0,1,0,0,0,0,1,1},
    {0,0,0,1,0,0,0,0},
    {0,1,0,0,1,0,0,1},
    {0,0,0,0,1,0,1,0}
};

int visiting_order_index=0;
bool visited[8]={false};

int Queue[QSize];
int first= 0;
int last=0;


int isFull()
{
    return ((first == 0 && (last == QSize - 1)) || (first == last + 1));
}

int isEmpty()
{ // first와 last가 같은 경우 큐는 empty
	return (first == last);
}

int enqueue(int v)
{
    if(!isFull())
    {
        last = (last+1)% QSize;
        Queue[last] = v;
    }
    else return -1;
    return v;
}

int dequeue()
{
    int v;
    if(!isEmpty())
    {
        v = Queue[first];
        first = (first+1)% QSize;
    }
    else return -1;
    return v;
}

void printing_array(int arr[])
{
    int i=0;
    for(i=0;i<8;i++)
    {
        printf("(index,value) (%d,%d) ",i,arr[i]);
    }
    printf("\n");
}

void BreadthFirstSearch(int start_vertice_num)
{

    //선언 시 초기화말고도, BFS상 초기화.
    int index0;
    for(index0=0;index0<8;index0++)
    {
        visited[index0]=false;
    }
    first=last=0;

    // 단절된 곳이 있는 것을 염두한 코딩, DFS와 동일
    for(index0=start_vertice_num; index0<8; index0++)
    {
        if(visited[index0]==0)
        {
            //입력받은 벌틱스에 대해서 방문한거니까,true 할당.
            visited[index0]=true;
            //방문순 출력, 별도 저장 안함.
            printf("%d -> node#%d in picture is visited\n", index0,index0+1);

            int v,w;
            v=enqueue(index0);

            while(!isEmpty)
            {
                w=dequeue();
                printf("check %d ",w);

                int index1_col;
                for(index1_col=0;index1_col<8;index1_col++)
                {
                    if((graph[index0][index1_col] != 0)&&(visited[index1_col]==0))
                    {
                        visited[index1_col]=true;
                        enqueue(index1_col);
                    }
                }
            }
        }
    }
}

int main()
{
    //picture 기준
    int start_vertice_num=1;

    //0부터 재인덱싱 해기.
    start_vertice_num=start_vertice_num-1;

    BreadthFirstSearch(start_vertice_num);

    printf("\nHello world!\n");
    return 0;
}
