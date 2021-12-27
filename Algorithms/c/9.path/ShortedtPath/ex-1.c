#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//graph는 vertex 갯수파악을 시작으로.
#define NUM_VERTEX 8
#define MAX 9999
//vertex별 정보모음이라고 생각하자
//한편,그림의 인덱싱과 대응하며 로직을 짜기 위해 1칸추가.
int dist[NUM_VERTEX+1];
int prev[NUM_VERTEX+1];
int visited[NUM_VERTEX+1];
/*
주어진 vertex의 갯수를 확인하고, 이를 바탕으로 엣지 생성.

단, picture에는 노드1 이 컴퓨터는 0부터라, 헷갈린다.
그래서 눈에 보이는대로 코딩할 수 있게
adjacent matrix를 사람 기준으로 호출할수있게
일부로 2차원 배열의 크기를 가로세로 1씩 늘리고
0번째는 비워둔다.
+헷갈리니까 간격은 space 3칸씩, 이유는 모르겠고 tap해도 2칸밖에 안띄어짐.

한편, 값이 0도 아니고, MAX도 아니면 서로 인접함을 의미하는구나.
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

//위에까지가 일반적인 graph 정의

//아래는 사용할 queue나 heap
//생각치 못했는데, 얘도 +1해주고 코드 좀 변경해줘야 위 dist와 prev와 연동가능.
int h[NUM_VERTEX+1];
int h_index_size = (-1+1);
/*
stack에서 top이랑 같은 역할인듯.
원래라면,
0번째부터 시작인 컴퓨터 특성상
h_index_size가 0이면 배열에 1개 있다는 의미 가능.

근데 나는 0번째 안쓰고 1번째부터 쓸거라
heap index size는 결과적으로 0부터 시작.
*/

//bubbleup, argument 'index_NextofLast'는 들어오기 직전에 +1되기 때문에
//마지막 배열 원소 다음자리에 대응가능.
void bubbleup(int h[], int key, int index_NextofLast)
{
    h[index_NextofLast] = key; // 일단, 배열의 마지막에다가 key를 배치

    //맨마지막 배열원소의 다음 자리부터 시작하여 parent index를 설정하기 위해 변수설정.
    //그대로 써도 되지만 내가 헷갈림.
    int index_child=index_NextofLast;
    // p is parent's index, 새로 들어온 값의 적절한 위치를 찾기 위해서 정의한 값.
    int p = ceil(index_child/2);
    int temp;
    //키값보다 부모가 크면 키값을 위로 올려야하니까 아래처럼 부등호,
    // 한편 애당초 heap array의 인덱스가 0, 즉 배열 길이가 1이면 패스.
    while(index_child != (0+1) && h[p] > key)
    {
        temp = h[index_child];// 짐을 비우고
        h[index_child] = h[p];// 부모의 키값을 비운 곳에 넣고
        h[p] = temp;// 빼놓은 키값을 부모 자리에 넣기.

        /*
        방금전까지 부모이던 노드의 인덱스를
        child index에 부여한다.
        즉 부모의 부모 인덱스를 설정할 수 있게 된다.
        */
        index_child = p;
        //그리고 아랭세서 부모노드를 가리키는 일종의 포인터를 level상 한층 올려서 재귀적으로 실행.
        p = ceil(index_child/2);
    }
}
//insert, key comes from input array S by 'for문'
void insert(int h[], int key)
{
    bubbleup(h, key, h_index_size);
}

//'i'를 부모노드 인데스라고 생각할 때
//왼쪽, 오른쪽 자식 중에서 minimum_child's index를 찾자.
int minimum_child(int h[], int i)
{
    /*
    2i+1이 h index size 보다 크다는 건 자식의 인덱스가 힙의 크기를 넘어선다는 의미.
    이 경우 애초에 노드가 1개거나, shiftdown이 완료된것.

    노드가 1개인 경우, 원래라면 부모 인덱스는 자기자신인 0인데
    나의 경우 1을 시작점으로 설정하였으니 +1
    한편, level 2 이상에서 자식이 없는 노드

    근데 복잡한게, 1부터 시작이면 왼쪽 차일드가 짝수이다.
    이런 거 생각하면 그냥 0번째부터 할껄 했지만 여튼
    왼쪽 차일드는 2i

    근데,h[9]는 선언되거나 정의되지 않음에도, c=9이고 h[c]는 0으로 간주되어 문제발생.
    아래 if의 의미는 왼쪽 차일드를 지칭했는데,
    생각해보면 오른쪽이 초과되는 상황을 추가
    */
    if(2*i+1-1 > h_index_size || 2*i+2-1 > h_index_size)
        return (0+1);
    else//왼쪽 자식과 오른쪽 자식 중 작은 놈의 인덱스를 구하자.
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
//shift down for min heap, makeheap도 필요하지만 deletemin에 반드시 필요한 함수인듯.
//key_h는 h의 원소들로 제자리를 찾기 전 이다.
void shiftdown(int h[], int key_h, int index_p)
{
    //printf("%d--",index_p);
    //printf("%4d--",key_h);

    int c = minimum_child(h, index_p);
    //printf("%d--",c);
    int temp;
    h[index_p] = key_h;
    //printf("%d\n", h[index_p]);
    //이유는 모르지만
    //h[9]는 선언되거나 정의되지 않음에도, c=9이고 h[c]는 0으로 간주되어 문제발생.
    //아래 while에서 && c<9너도 되나 역할 상 minimum_child 함수 변형.
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
        h_index_size++;// 현재 heap array를 1칸 확장한다는 느낌, for insert.
        //printf("%d\n", h_index_size);
        insert(h, S[i]);
        //insert 안에 bubbleup에 쓸려고 h index size 증가시킨거니, 내 이해를 위해 변형
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

//시작점은 next의 초항
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
    //관련 초기화는 main에서 수행. while만 넣자.


    /*
    heap 이 dist로 업그레이드 된다면 그 의미는 결국 dist가 아닐가.
    배경자료에 다익스트라 함수에 대한 설명과, main문에서의 다익스트라 while문이
    다른 듯 보임.

    여튼 난 다익스트라 함수 설명대로 함.
    */

    int dist_adj_vertex;
    int index_row_adj_matrix;
    int index_col_adj_matrix;
    int vertex;
    while( h_index_size !=0 )
    {
        dist_adj_vertex=deleteMin(h);
        //스스로의 이해를 위해 아래와 같이 대입.
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
            //방문한 적이 없고,그래프의 그 값이 0, MAX가 아니라면 인접하다.
            if(visited[index_col_adj_matrix]!=true && graph[vertex][index_col_adj_matrix] != 0 && graph[vertex][index_col_adj_matrix] != MAX)
            {
                /*
                dist[vertex]는 지금까지 누적된 이동거리,
                graph[vertex][index_col_adj_matrix]는 앞으로 갈 거리 들 중 하나.
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
    //start vertex=1, 이거에 맞게 인접행렬 변환함.
    int FIRST=1;

    //관련 변수 배열 초기화
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

    //heap도 1번째부터 할라니까 고칠 게 너무 많다. 결국 했지만, 후회.
    /*
    h    0   0  max  max  max~
    */

    //변형한 heap이 걱정되서 test 진행, 일단 아래 케이스는 제대로 작동.
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
