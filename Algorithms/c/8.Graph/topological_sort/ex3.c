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
�� �޸�, �׷��� ����� ��Ī��ķ� ������ ������ �ܹ��� �׷���.
��׶��忡 �ִ� �ܹ��� �׷����� �������� �׷Ƚ��ϴ�.
*/
int graph[8][8]={
    {0,0,1,0,0,0,0,0},//3���� ����.
    {1,0,0,0,1,0,0,0},//1�� 5�� ����.
    {0,0,0,1,0,0,1,0},//4�� 7�� ����.
    {0,0,0,0,0,0,0,0},//
    {0,0,0,1,0,1,0,0},//4�� 6���� ����.
    {0,0,0,0,0,0,0,1},//8�� ����.
    {0,0,0,0,0,0,0,0},//
    {0,0,0,0,0,0,1,0}//7�ΰ���.
};

int visiting_order_index=1;
bool visited[8]={false};
int pre[8]={0};
int post[8]={0};


//�迭 ����Ʈ
void print_array(int arr[])
{
    int i=0;
    for(i=0;i<8;i++)
    {
        printf("%d %d/ ",i,arr[i]);
    }
    printf("\n");
}

//���İ� ���� �迭���� �񱳸� ���� �ε���(��� �ѹ�)���.
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
            //���� ���� �ڷ� ������. ��, Ŭ ���� ���̴�.
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

	//�Է¹��� ��ƽ���� ���ؼ� �湮�ѰŴϱ�,true �Ҵ�.
	printf("%d ", vertice_number+1);
	visited[vertice_number]=true;

	pre[vertice_number]=visiting_order_index++;//0���� ��������.

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

    //���� �� �ʱ�ȭ����, DFS�� �ʱ�ȭ.
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
    DFS�� ���� ����� post������ ������������ ���Ͽ� ����.
    �׸��� �̸� �������� ��带 ��� �Ǵ� ����.
    */

    int index2=0;
    for(index2=0;index2<8;index2++)
    {
        printf("\n%d -> Node#%d in picture ( %d, %d)/\n",index2, index2+1,pre[index2],post[index2]);
    }
    printf("\n");

    //pre ���� ���������� ����غ���.
    int* sorted_post;
    sorted_post=bubbleinsertion(post);

    printf("���� ���ļ���(post ū ��) : ");
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
    //�׷����� �迭��
    //DFS �˰��� wiht recursive
    //���� ���� 2, �湮���� ���.

    //printf("%d",visited[0]);

    //picture ���� ��� �ѹ� 1���� �����Ѵٰ� ����.
    int start_vertice_num=1;
    post[0]=8;

    //0���� ���ε��� �ر�.
    start_vertice_num=start_vertice_num-1;

    DepthFirstSearch(start_vertice_num);



    printf("Hello world!\n");
    return 0;
}
