#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define COUNT 10


int graph[10][10]={
    {0,1,1,1,0,0,0,0,0,0},
    {1,0,0,1,1,0,1,0,0,0},
    {1,0,0,1,0,0,0,0,0,0},
    {1,1,1,0,0,1,0,0,0,0},
    {0,1,0,0,0,0,1,1,0,0},
    {0,0,0,1,0,0,0,0,0,0},
    {0,1,0,0,1,0,0,1,0,0},
    {0,0,0,0,1,0,1,0,0,0},
    {0,0,0,0,0,0,0,0,0,1},
    {0,0,0,0,0,0,0,0,1,0}
};

/*
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
*/
visiting_order_index=1;
bool visited[10]={false};
int pre[10]={0};
int post[10]={0};


//�迭 ����Ʈ
void print_array(int arr[])
{
    int i=0;
    for(i=0;i<10;i++)
    {
        printf("%d %d/ ",i,arr[i]);
    }
    printf("\n");
}

void printing_array(int arr[])
{
    int i=0;
    for(i=0;i<10;i++)
    {
        printf("Index is %d, value is %d/ ",i,arr[i]);
    }
    printf("\n");
}

void DFS_Core(int vertice_number)
{
	printf("%d ", vertice_number+1);
	visited[vertice_number]=true;

	pre[vertice_number]=visiting_order_index++;//1���� ��������.

	int index1_col;
    for(index1_col=0; index1_col<10; index1_col++)
    {
        if((graph[vertice_number][index1_col] != 0)&&(visited[index1_col]==0))
        {

            DFS_Core(index1_col);
            post[index1_col]=visiting_order_index++;
        }
    }

}
void DepthFirstSearch(int start_vertice_num)
{
    //���� �� �ʱ�ȭ����, DFS�� �ʱ�ȭ.
    int index0;
    for(index0=0;index0<10;index0++)
    {
        visited[index0]=0;
        pre[index0]=0;
        post[index0]=0;
    }
    for(index0=start_vertice_num; index0<10; index0++){
        if(visited[index0]==0)
        {
            DFS_Core(index0);
            if(post[index0]==0)
            {
                post[index0]=visiting_order_index++;
            }
        }
    }


    int index2=0;
    for(index2=0;index2<10;index2++)
    {
        printf("\n%d -> Node#%d's pre and post in picture ( %d, %d)/\n",index2, index2+1,pre[index2],post[index2]);
    }
    printf("\n");
}

int main()
{
    //�׷����� �迭��
    //DFS �˰��� wiht recursive
    //���� ���� 1, �湮���� ���.

    //printf("%d",visited[0]);

    //picture ����
    int start_vertice_num=1;

    //0���� ���ε��� �ر�.
    start_vertice_num=start_vertice_num-1;

    DepthFirstSearch(start_vertice_num);



    printf("Hello world!\n");
    return 0;
}
