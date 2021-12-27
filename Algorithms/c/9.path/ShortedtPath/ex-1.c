#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//graph�� vertex �����ľ��� ��������.
#define NUM_VERTEX 8
#define MAX 9999
//vertex�� ���������̶�� ��������
//����,�׸��� �ε��̰� �����ϸ� ������ ¥�� ���� 1ĭ�߰�.
int dist[NUM_VERTEX+1];
int prev[NUM_VERTEX+1];
int visited[NUM_VERTEX+1];
/*
�־��� vertex�� ������ Ȯ���ϰ�, �̸� �������� ���� ����.

��, picture���� ���1 �� ��ǻ�ʹ� 0���Ͷ�, �򰥸���.
�׷��� ���� ���̴´�� �ڵ��� �� �ְ�
adjacent matrix�� ��� �������� ȣ���Ҽ��ְ�
�Ϻη� 2���� �迭�� ũ�⸦ ���μ��� 1�� �ø���
0��°�� ����д�.
+�򰥸��ϱ� ������ space 3ĭ��, ������ �𸣰ڰ� tap�ص� 2ĭ�ۿ� �ȶ����.

����, ���� 0�� �ƴϰ�, MAX�� �ƴϸ� ���� �������� �ǹ��ϴ±���.
*/

int graph[NUM_VERTEX+1][NUM_VERTEX+1]={
    {0,  0,  0,  0,  0,  0,  0,  0,  0},
    {0,  0,  6,  3,  2,MAX,MAX,MAX,MAX},
    {0,  6,  0,MAX,  2,  3,MAX,  2,MAX},
    {0,  3,MAX,  0,  1,MAX,  7,MAX,MAX},
    {0,  2,  2,  1,  0,MAX,  4,  3,MAX},
    {0,MAX,  3,MAX,MAX,  0,MAX,  7,  9},
    {0,MAX,MAX,  7,  4,MAX,  0,MAX,MAX},
    {0,MAX,  2,MAX,  3,  7,MAX,  0,  4},
    {0,MAX,MAX,MAX,MAX,  9,MAX,  4,  0}
};

//���������� �Ϲ����� graph ����

//�Ʒ��� ����� queue�� heap
//����ġ ���ߴµ�, �굵 +1���ְ� �ڵ� �� ��������� �� dist�� prev�� ��������.
int h[NUM_VERTEX+1];
int h_index_size = (-1+1);
/*
stack���� top�̶� ���� �����ε�.
�������,
0��°���� ������ ��ǻ�� Ư����
h_index_size�� 0�̸� �迭�� 1�� �ִٴ� �ǹ� ����.

�ٵ� ���� 0��° �Ⱦ��� 1��°���� ���Ŷ�
heap index size�� ��������� 0���� ����.
*/

//bubbleup, argument 'index_NextofLast'�� ������ ������ +1�Ǳ� ������
//������ �迭 ���� �����ڸ��� ��������.
void bubbleup(int h[], int key, int index_NextofLast)
{
    h[index_NextofLast] = key; // �ϴ�, �迭�� ���������ٰ� key�� ��ġ

    //�Ǹ����� �迭������ ���� �ڸ����� �����Ͽ� parent index�� �����ϱ� ���� ��������.
    //�״�� �ᵵ ������ ���� �򰥸�.
    int index_child=index_NextofLast;
    // p is parent's index, ���� ���� ���� ������ ��ġ�� ã�� ���ؼ� ������ ��.
    int p = ceil(index_child/2);
    int temp;
    //Ű������ �θ� ũ�� Ű���� ���� �÷����ϴϱ� �Ʒ�ó�� �ε�ȣ,
    // ���� �ִ��� heap array�� �ε����� 0, �� �迭 ���̰� 1�̸� �н�.
    while(index_child != (0+1) && h[p] > key)
    {
        temp = h[index_child];// ���� ����
        h[index_child] = h[p];// �θ��� Ű���� ��� ���� �ְ�
        h[p] = temp;// ������ Ű���� �θ� �ڸ��� �ֱ�.

        /*
        ��������� �θ��̴� ����� �ε�����
        child index�� �ο��Ѵ�.
        �� �θ��� �θ� �ε����� ������ �� �ְ� �ȴ�.
        */
        index_child = p;
        //�׸��� �Ʒ����� �θ��带 ����Ű�� ������ �����͸� level�� ���� �÷��� ��������� ����.
        p = ceil(index_child/2);
    }
}
//insert, key comes from input array S by 'for��'
void insert(int h[], int key)
{
    bubbleup(h, key, h_index_size);
}

//'i'�� �θ��� �ε������ ������ ��
//����, ������ �ڽ� �߿��� minimum_child's index�� ã��.
int minimum_child(int h[], int i)
{
    /*
    2i+1�� h index size ���� ũ�ٴ� �� �ڽ��� �ε����� ���� ũ�⸦ �Ѿ�ٴ� �ǹ�.
    �� ��� ���ʿ� ��尡 1���ų�, shiftdown�� �Ϸ�Ȱ�.

    ��尡 1���� ���, ������� �θ� �ε����� �ڱ��ڽ��� 0�ε�
    ���� ��� 1�� ���������� �����Ͽ����� +1
    ����, level 2 �̻󿡼� �ڽ��� ���� ���

    �ٵ� �����Ѱ�, 1���� �����̸� ���� ���ϵ尡 ¦���̴�.
    �̷� �� �����ϸ� �׳� 0��°���� �Ҳ� ������ ��ư
    ���� ���ϵ�� 2i

    �ٵ�,h[9]�� ����ǰų� ���ǵ��� ��������, c=9�̰� h[c]�� 0���� ���ֵǾ� �����߻�.
    �Ʒ� if�� �ǹ̴� ���� ���ϵ带 ��Ī�ߴµ�,
    �����غ��� �������� �ʰ��Ǵ� ��Ȳ�� �߰�
    */
    if(2*i+1-1 > h_index_size || 2*i+2-1 > h_index_size)
        return (0+1);
    else//���� �ڽİ� ������ �ڽ� �� ���� ���� �ε����� ������.
    {
        if(h[2*i+1-1] < h[2*i+2-1])
        {
            return 2*i+1-1;
        }
        else
        {
            return 2*i+2-1;
        }
    }
}
//shift down for min heap, makeheap�� �ʿ������� deletemin�� �ݵ�� �ʿ��� �Լ��ε�.
//key_h�� h�� ���ҵ�� ���ڸ��� ã�� �� �̴�.
void shiftdown(int h[], int key_h, int index_p)
{
    //printf("%d--",index_p);
    //printf("%4d--",key_h);

    int c = minimum_child(h, index_p);
    //printf("%d--",c);
    int temp;
    h[index_p] = key_h;
    //printf("%d\n", h[index_p]);
    //������ ������
    //h[9]�� ����ǰų� ���ǵ��� ��������, c=9�̰� h[c]�� 0���� ���ֵǾ� �����߻�.
    //�Ʒ� while���� && c<9�ʵ� �ǳ� ���� �� minimum_child �Լ� ����.
    while(c != (0+1) && h[c] < key_h)
    {
        temp = h[index_p];
        h[index_p] = h[c];
        h[c] = temp;
        //printf("%d++\n", h[c]);
        index_p = c;
        c = minimum_child(h, index_p);
    }
}

//make heap
void makeheap(int S[], int h[], int len_S)
{
    int i;
    for(i=(0+1); i<len_S; i++)
    {
        h_index_size++;// ���� heap array�� 1ĭ Ȯ���Ѵٴ� ����, for insert.
        //printf("%d\n", h_index_size);
        insert(h, S[i]);
        //insert �ȿ� bubbleup�� ������ h index size ������Ų�Ŵ�, �� ���ظ� ���� ����
        //insert(h, S[i], h_index_size);
    }
/*
    printf("heap array before shiftdown in makeheap\n");
    for(i=(0+1);i<NUM_VERTEX+1;i++)
    {
        printf("%d ",h[i]);
    }
    printf("\n\n");
*/
    for(i=(0+1); i<len_S; i++)
        shiftdown(h, h[i], i);
}

//deletemin
int deleteMin(int h[])
{
    int x;
    if(h_index_size == (-1+1))
        return -1000;
    else
    {
        x = h[(0+1)];
        shiftdown(h, h[h_index_size], (0+1));
        h[h_index_size] = 1000;
        h_index_size--;
        return x;
    }
}
/*
int closet(){
    int mindist = MAX;
    int i = 0;
    int notbechecked = 0;

    for(i = 0; i < NUM_VERTEX; i++){
        if((!tobechecked[i]) && (mindist >= dist[i])){
            mindist = dist[i];
            notbechecked = i;
        }
    }
    return notbechecked;
}

void dijkstra(){
    int mindist = MAX;
    int i = 0;
    int notbechecked = 0;
    int count = 0;

    while(count < NUM_VERTEX){
        notbechecked = closet();
        tobechecked[notbechecked] = TRUE;
        for(i = 0; i < NUM_VERTEX; i++){
            if((!tobechecked[i]) && (graph[notbechecked][i] > 0)){
                if(dist[i] >  dist[notbechecked] + graph[notbechecked][i]){
                    dist[i] = dist[notbechecked] + graph[notbechecked][i];
                    prev[i] = notbechecked;
                }
            }
        }
        count++;
    }
}*/

//�������� next�� ����
int find_next_vertex(int min_dist)
{
    int i;
    for(i=1;i<NUM_VERTEX+1;i++)
    {
        if(dist[i]==min_dist)
        {
            return i;
        }
    }
}

void Dijstra(int graph[NUM_VERTEX+1][NUM_VERTEX+1], int first)
{
    //���� �ʱ�ȭ�� main���� ����. while�� ����.


    /*
    heap �� dist�� ���׷��̵� �ȴٸ� �� �ǹ̴� �ᱹ dist�� �ƴҰ�.
    ����ڷῡ ���ͽ�Ʈ�� �Լ��� ���� �����, main�������� ���ͽ�Ʈ�� while����
    �ٸ� �� ����.

    ��ư �� ���ͽ�Ʈ�� �Լ� ������ ��.
    */

    int dist_adj_vertex;
    int index_row_adj_matrix;
    int index_col_adj_matrix;
    int vertex;
    while( h_index_size !=0 )
    {
        dist_adj_vertex=deleteMin(h);
        //�������� ���ظ� ���� �Ʒ��� ���� ����.
        index_row_adj_matrix=find_next_vertex(dist_adj_vertex);
        vertex=index_row_adj_matrix;
        visited[vertex]=true;
/*
        int j;
        for(j=(0+1);j<NUM_VERTEX+1;j++)
        {
            printf("%d ",visited[j]);
        }
        printf("\n");
*/
        for(index_col_adj_matrix=1;index_col_adj_matrix<NUM_VERTEX+1;index_col_adj_matrix++)
        {
            //�湮�� ���� ����,�׷����� �� ���� 0, MAX�� �ƴ϶�� �����ϴ�.
            if(visited[index_col_adj_matrix]!=true && graph[vertex][index_col_adj_matrix] != 0 && graph[vertex][index_col_adj_matrix] != MAX)
            {
                /*
                dist[vertex]�� ���ݱ��� ������ �̵��Ÿ�,
                graph[vertex][index_col_adj_matrix]�� ������ �� �Ÿ� �� �� �ϳ�.
                */
                if(dist[index_col_adj_matrix] >  dist[vertex] + graph[vertex][index_col_adj_matrix])
                {
                    dist[index_col_adj_matrix] = dist[vertex] + graph[vertex][index_col_adj_matrix];
                    prev[index_col_adj_matrix] = vertex;
                }
            }
        }
        makeheap(dist,h,NUM_VERTEX+1);
        int i;
        for(i=1;i<NUM_VERTEX+1;i++)
        {
            if(visited[i]==true)
            {
                deleteMin(h);
            }
        }
    }
}

void main(){
    //start vertex=1, �̰ſ� �°� ������� ��ȯ��.
    int FIRST=1;

    //���� ���� �迭 �ʱ�ȭ
    int i=1;
    for(i=1;i<NUM_VERTEX+1;i++)
    {
        dist[i]=MAX;
        prev[i]=0;
    }
    dist[FIRST]=0;
    prev[FIRST]=FIRST;
    /*
    dist 0   0  max  max  max~
    prev 0   1  0    0    0 ~
    */

    //heap�� 1��°���� �Ҷ�ϱ� ��ĥ �� �ʹ� ����. �ᱹ ������, ��ȸ.
    /*
    h    0   0  max  max  max~
    */

    //������ heap�� �����Ǽ� test ����, �ϴ� �Ʒ� ���̽��� ����� �۵�.
/*
    dist[1]=1;dist[2]=2;dist[3]=3;dist[4]=4;
    dist[5]=5;dist[6]=6;dist[7]=7;dist[8]=8;
*/
    printf("make heap at FIRST\n");
    makeheap(dist,h,NUM_VERTEX+1);
    for(i=(0+1);i<NUM_VERTEX+1;i++)
    {
        printf("%d ",h[i]);
    }
    printf("\n");
    printf("%d",h_index_size);
    printf("\n");

    printf("Testing deletemin of heap\n");
    for(i=(0+1);i<NUM_VERTEX+1;i++)
    {
        printf("%d ",deleteMin(h));
    }
    printf("\n");
    printf("%d",h_index_size);
    printf("\n");

    printf("make heap at FIRST again\n");
    makeheap(dist,h,NUM_VERTEX+1);
    for(i=(0+1);i<NUM_VERTEX+1;i++)
    {
        printf("%d ",h[i]);
    }
    printf("\n");
    printf("%d",h_index_size);
    printf("\n");


    printf("Execute Dijstra\n");
    Dijstra(graph,FIRST);


    for(i=(0+1);i<NUM_VERTEX+1;i++)
    {
        printf("Node %d: distance %d:%d ;   those are derived from FIRST Vertex:just before Vertex \n",i,dist[i],prev[i]);
    }

}
