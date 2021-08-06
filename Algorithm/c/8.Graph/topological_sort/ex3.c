#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define COUNT 8
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
와 달리, 그래프 행렬을 대칭행렬로 만들지 않으면 단방향 그래프.
백그라운드에 있는 단방향 그래프를 바탕으로 그렸습니다.
*/
int graph[8][8]={
    {0,0,1,0,0,0,0,0},//3으로 간다.
    {1,0,0,0,1,0,0,0},//1과 5로 간다.
    {0,0,0,1,0,0,1,0},//4와 7로 간다.
    {0,0,0,0,0,0,0,0},//
    {0,0,0,1,0,1,0,0},//4와 6으로 간다.
    {0,0,0,0,0,0,0,1},//8로 간다.
    {0,0,0,0,0,0,0,0},//
    {0,0,0,0,0,0,1,0}//7로간다.
};

int visiting_order_index=1;
bool visited[8]={false};
int pre[8]={0};
int post[8]={0};


//배열 프린트
void print_array(int arr[])
{
    int i=0;
    for(i=0;i<8;i++)
    {
        printf("%d %d/ ",i,arr[i]);
    }
    printf("\n");
}

//정렬과 기존 배열과의 비교를 통한 인덱스(노드 넘버)출력.
int* bubbleinsertion(int post_data[])
{
    //print_array(post_data);

    int i,j, temp;

    static int bubbled_array[COUNT];

    for(i=0;i<COUNT;i++)
    {
        bubbled_array[i]=post_data[i];
    }

    for (i = 0; i < COUNT - 1; i++)
    {
        for (j = 0; j < COUNT - 1 - i; j++)
        {
            //작을 수록 뒤로 보낸다. 즉, 클 수록 앞이다.
            if (bubbled_array[j] < bubbled_array[j + 1])
            {
                temp        = bubbled_array[j];
                bubbled_array[j]     = bubbled_array[j + 1];
                bubbled_array[j + 1] = temp;
            }
        }
    }

    //print_array(bubbled_array);
    return bubbled_array;
}

void printing_array(int arr[])
{
    int i=0;
    for(i=0;i<8;i++)
    {
        printf("Index is %d, value is %d/ ",i,arr[i]);
    }
    printf("\n");
}

void DFS_Core(int vertice_number)
{

	//입력받은 벌틱스에 대해서 방문한거니까,true 할당.
	printf("%d ", vertice_number+1);
	visited[vertice_number]=true;

	pre[vertice_number]=visiting_order_index++;//0부터 시작하자.

	int index1_col;
    for(index1_col=0; index1_col<8; index1_col++)
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

    //선언 시 초기화말고도, DFS상 초기화.
    int index0;
    for(index0=0;index0<8;index0++)
    {
        visited[index0]=0;
        pre[index0]=0;
        post[index0]=0;
    }

    for(index0=start_vertice_num; index0<8; index0++){
        if(visited[index0]==0)
            DFS_Core(index0);
    }

    /*
    DFS를 통해 산출된 post값들을 내림차순으로 구하여 저장.
    그리고 이를 바탕으로 노드를 출력 또는 저장.
    */

    int index2=0;
    for(index2=0;index2<8;index2++)
    {
        printf("\n%d -> Node#%d in picture ( %d, %d)/\n",index2, index2+1,pre[index2],post[index2]);
    }
    printf("\n");

    //pre 값이 작은순으로 출력해보자.
    int* sorted_post;
    sorted_post=bubbleinsertion(post);

    printf("위상 정렬순서(post 큰 순) : ");
    int index3=0;
    for(index2=0;index2<8;index2++)
    {
        for(index3=0;index3<8;index3++)
        {
            if(sorted_post[index2]==post[index3])
            {
                printf("%d ", index3+1);
            }
        }

    }
    printf("\n");
}

int main()
{
    //그래프를 배열로
    //DFS 알고리즘 wiht recursive
    //시작 노드는 2, 방문순서 출력.

    //printf("%d",visited[0]);

    //picture 기준 노드 넘버 1에서 시작한다고 하자.
    int start_vertice_num=1;
    post[0]=8;

    //0부터 재인덱싱 해기.
    start_vertice_num=start_vertice_num-1;

    DepthFirstSearch(start_vertice_num);



    printf("Hello world!\n");
    return 0;
}
