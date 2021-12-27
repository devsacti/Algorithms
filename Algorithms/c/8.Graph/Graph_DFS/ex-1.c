#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define COUNT 8
/*
���� �˾Ҵµ�, c������ bool/boolean ���� ��� �̷��� ����;��Ѵٰ� �Ѵ�.
�ƴϸ� ���� 0 �� false, 1�� �� �� ���ڰ� true�� ���ֵȴٴ� ���� Ȱ���Ͽ�
visiting order index �ٷ� �ᵵ �ȴ�.
����, bool�� ������ %d�� ��� �� 1����.
*/

/*
��ü ����.
1. �׷����� ��������
  1.1.���� ����� �������� adjacent matrix &
  1.2.�� ��忡 ���ؼ� (visiting order index & visited array) &(pre&post)
2. DepthFirstSearch
3. DFS_core
*/

/*
1.1.
vertice & edge�� ���ÿ� �ڵ������� �����ϴ�
adjacent matrix�� ��������.

����� ������ 8���ϱ� 1���� ���ѹ�1�� edge�� ǥ��, �� n���� ���ѹ�n�� edge�� ����.

�ٵ�, ��ǻ�Ϳ����� 0��°�� ����� �� ���ϴϱ�,
�Ʒ�ó�� ���� ���� �ε����ߴٰ� ġ��.

node#0 is connected with #1,2,3 that means NODE 1 in picture
node#1 is connected with #0,3,4,6 that means NODE 2 in picture
node#2 is connedted with #0,3 that means NODE 3 in picture
...

*/
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
/*
1.2.
���� �湮���̴ϱ�, �湮�����ε����� 1�� �����ϰ�, ��� ���� �湮 ���� �ǹ��ϴ� 0���� �ʱ�ȭ.
�湮�Ҷ����� �湮�����ε����� 1 ������Ų �� pre�� ����.
�׸��� ������ Ÿ�ֿ̹� 1 ���� ���Ѽ� post�� ����.

����,
�� �湮�����ε��������� visited �迭�� n(n>=0)��°�� �����ؼ�
����� ���� ���#n�� �湮������ �ǹ��ϵ��� �Ҽ����� ������ �ߴµ�,
�׷��� ��ȸ?(����)�� ����� ���ϴϱ�. pre�� post�� ���� �� Ȯ�强�� �ִµ�.
*/
int visiting_order_index=1;
bool visited[8]={false};
int pre[8]={0};
int post[8]={0};

/*
�ε��� ����. �� ��û�̴ϱ�.�����ϰ�.

index0_vertice_row is for void DepthFirstSearch()
index1 is for void DFS_Core(int vertice_number)
*/



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
int* bubbleinsertion(int pre_data[])
{
    //print_array(pre_data);

    int i,j, temp;

    static int bubbled_array[COUNT];

    for(i=0;i<COUNT;i++)
    {
        bubbled_array[i]=pre_data[i];
    }

    for (i = 0; i < COUNT - 1; i++)
    {
        for (j = 0; j < COUNT - 1 - i; j++)
        {
            if (bubbled_array[j] > bubbled_array[j + 1])
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
    /*
	visited[v] = true;	// ����� �湮���� ���
	pre[v] = i++;
	for all vertices u adjacent to v   // G[v][u] == 1 �� ��� �������ִ�.
		if visited[u] == 0	// ó�� �湮�� ����� ���
			DFS(u);
	post[u]= i++;
	*/

	//�Է¹��� ��ƽ���� ���ؼ� �湮�ѰŴϱ�,true �Ҵ�.
	printf("%d ", vertice_number+1);
	visited[vertice_number]=true;

	pre[vertice_number]=visiting_order_index++;//1���� ��������.

	int index1_col;
    for(index1_col=0; index1_col<8; index1_col++)
    {
        /*
        ��������, DFS_Core�� ��� �������� ���湮�� �ƴ϶�, �־��� ���� ���� ��θ� ã�� ����
        ��������. �׷��� ������  �Ʒ� if���� �ప�� �����ϴ� ���̰�
        DepthFirstsearch�� ������ �κ��� �����ؼ� �ִ� ���̴�.
        ��, �̰��� ��� DepthFirstsearch�� ù 0 ���� 1,2,3,4 ����� �ƹ� �ǹ̰� ����.

        (graph[vertice_number][index1] != 0) means that it processes only adjacent node
        �ప�� �Է¹��� vertice number�� ��Ʈ���� �󿡼� �ະ�� ó��.
        (visited[index1]==0) means that it processes only unvisited node
        ����, for���� ���� ���ѹ������� �湮 ��带 �����ϴ� ����̴�.
        */
        if((graph[vertice_number][index1_col] != 0)&&(visited[index1_col]==0))
        {
            //���� �ȿ� ���Դٴ� ���� ��������̸�, �������� �湮�� �� ���� ���ٴ� ���̴�.
            //�Ʒ� �࿡�� ���湮 ó���� ����ȴ�.
            DFS_Core(index1_col);
            //�����Ҷ����� ���ƿ;��� �Ÿ��� ���ϱ�,
            post[index1_col]=visiting_order_index++;
            //printf("%d ", post[index1]);

        }
    }
}
void DepthFirstSearch(int start_vertice_num)
{
    /*
    for all vertices v
		num[v] = 0; // num�� visited
	i = 0;
	while there is a vertex v such that num(v) is 0
		DFS(v)

    pre���� ���� ��� ������ �� ����� ��ȣ�� ����Ѵ�.
    */

    //���� �� �ʱ�ȭ����, DFS�� �ʱ�ȭ.
    int index0;
    for(index0=0;index0<8;index0++)
    {
        visited[index0]=0;
        pre[index0]=0;
        post[index0]=0;
    }
    //PDF���, ��ƽ������ �湮������ üũ�ϰ�, �̹湮������ DFS ȣ��


    //�����,�̷��� for�������� �湮������ üũ�� visited�迭�� ���� ��ΰ� N�� ������ ����.
    //��Ʈ���� �󿡼� �ະ�� �����ϰԵ�. �Ʒ� for����.
    for(index0=start_vertice_num; index0<8; index0++){
        if(visited[index0]==0)
            DFS_Core(index0);
    }

    /*
    pre�� ���� ������� ����ϸ� �װ� �湮������ �ȴٰ� �Ѵ�.
    �׷��� �ִ��� post�� �߷��ϴµ� ������ �ʰ�, ���� �뵵 �ΰ� �ʹ�.
    �Ƹ��� ��ȸ ��ο��� ���� ���� ������? �ǵ��ư��� �浵 �����ϴϱ�.
    �׸��� ������ pre�� ������ ���� post�� �ʿ��Ѱ�����.
    */

    int index2=0;
    for(index2=0;index2<8;index2++)
    {
        printf("\n%d -> Node#%d in picture ( %d, %d)/\n",index2, index2+1,pre[index2],post[index2]);
    }
    printf("\n");

    //pre ���� ���������� ����غ���.
    int* sorted_pre;
    sorted_pre=bubbleinsertion(pre);

    printf("�湮����(pre������) : ");
    int index3=0;
    for(index2=0;index2<8;index2++)
    {
        //printf("%d ",sorted_pre[index2]);
        for(index3=0;index3<8;index3++)
        {
            if(sorted_pre[index2]==pre[index3])
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
    //���� ���� 1, �湮���� ���.

    //printf("%d",visited[0]);
    printf("pre�� ���翡 1���ͱ淡 1�� �����Ͽ����ϴ�.\n");

    //picture ����
    int start_vertice_num=1;

    //0���� ���ε��� �ر�.
    start_vertice_num=start_vertice_num-1;

    DepthFirstSearch(start_vertice_num);



    printf("Hello world!\n");
    return 0;
}
