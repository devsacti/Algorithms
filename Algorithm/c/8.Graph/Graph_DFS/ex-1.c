#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define COUNT 8
/*
이제 알았는데, c에서는 bool/boolean 형이 없어서 이렇게 끌고와야한다고 한다.
아니면 논리상 0 이 false, 1과 그 외 숫자가 true로 간주된다는 것을 활용하여
visiting order index 바로 써도 된다.
한편, bool로 저장해 %d로 출력 시 1나옴.
*/

/*
전체 구성.
1. 그래프를 정의하자
  1.1.노드와 노드의 관점에서 adjacent matrix &
  1.2.한 노드에 대해서 (visiting order index & visited array) &(pre&post)
2. DepthFirstSearch
3. DFS_core
*/

/*
1.1.
vertice & edge를 동시에 코드적으로 묘사하는
adjacent matrix를 정의하자.

노드의 갯수가 8개니까 1행은 노드넘버1의 edge를 표현, 즉 n행은 노드넘버n의 edge를 내포.

근데, 컴퓨터에서는 0번째를 깔고가는 게 편하니까,
아래처럼 내가 새로 인덱싱했다고 치자.

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
아직 방문전이니까, 방문순서인덱스는 1로 시작하고, 모든 곳은 방문 무를 의미하는 0으로 초기화.
방문할때마다 방문순서인덱스를 1 증가시킨 뒤 pre에 저장.
그리고 적절한 타이밍에 1 증가 시켜서 post에 저장.

한편,
그 방문순서인덱스값들을 visited 배열의 n(n>=0)번째에 저장해서
저장된 값이 노드#n의 방문순서를 의미하도록 할수있지 않을까 했는데,
그러면 순회?(순서)를 출력을 못하니까. pre랑 post를 쓰는 게 확장성이 있는듯.
*/
int visiting_order_index=1;
bool visited[8]={false};
int pre[8]={0};
int post[8]={0};

/*
인덱스 정리. 난 멍청이니까.투박하게.

index0_vertice_row is for void DepthFirstSearch()
index1 is for void DFS_Core(int vertice_number)
*/



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
	visited[v] = true;	// 노드의 방문순서 기록
	pre[v] = i++;
	for all vertices u adjacent to v   // G[v][u] == 1 인 경우 인접해있다.
		if visited[u] == 0	// 처음 방문한 노드일 경우
			DFS(u);
	post[u]= i++;
	*/

	//입력받은 벌틱스에 대해서 방문한거니까,true 할당.
	printf("%d ", vertice_number+1);
	visited[vertice_number]=true;

	pre[vertice_number]=visiting_order_index++;//1부터 시작하자.

	int index1_col;
    for(index1_col=0; index1_col<8; index1_col++)
    {
        /*
        무엇보다, DFS_Core는 모든 점에서의 노드방문이 아니라, 주어진 점에 대한 경로를 찾는 것을
        유념하자. 그렇기 때무에  아래 if에서 행값을 대입하는 것이고
        DepthFirstsearch는 단절된 부분을 염두해서 있는 것이다.
        즉, 이경우는 사실 DepthFirstsearch는 첫 0 이후 1,2,3,4 등등은 아무 의미가 없다.

        (graph[vertice_number][index1] != 0) means that it processes only adjacent node
        행값이 입력받은 vertice number라서 매트릭스 상에서 행별로 처리.
        (visited[index1]==0) means that it processes only unvisited node
        한편, for문을 통해 노드넘버순으로 방문 노드를 결정하는 방식이다.
        */
        if((graph[vertice_number][index1_col] != 0)&&(visited[index1_col]==0))
        {
            //여기 안에 들어왔다는 것은 인접노드이며, 아직까지 방문해 본 적이 없다는 것이다.
            //아래 행에서 노드방문 처리가 진행된다.
            DFS_Core(index1_col);
            //전진할때마다 돌아와야할 거리도 들어나니까,
            post[index1_col]=visiting_order_index++;
            //printf("%d ", post[index1]);

        }
    }
}
void DepthFirstSearch(int start_vertice_num)
{
    /*
    for all vertices v
		num[v] = 0; // num은 visited
	i = 0;
	while there is a vertex v such that num(v) is 0
		DFS(v)

    pre값이 적은 노드 순서로 각 노드의 번호를 출력한다.
    */

    //선언 시 초기화말고도, DFS상 초기화.
    int index0;
    for(index0=0;index0<8;index0++)
    {
        visited[index0]=0;
        pre[index0]=0;
        post[index0]=0;
    }
    //PDF대로, 벌틱스별로 방문유무를 체크하고, 미방문했으면 DFS 호출


    //참고로,이렇게 for문돌릴때 방문유무를 체크된 visited배열을 통해 경로가 N개 나오지 않음.
    //매트릭스 상에서 행별로 접근하게됨. 아래 for문상.
    for(index0=start_vertice_num; index0<8; index0++){
        if(visited[index0]==0)
            DFS_Core(index0);
    }

    /*
    pre가 작은 순서대로 출력하면 그게 방문순서가 된다고 한다.
    그러면 애당초 post는 추력하는데 쓰지도 않고, 무슨 용도 인가 싶다.
    아마도 순회 경로에서 쓸모가 있지 않을까? 되돌아가는 길도 내포하니까.
    그리고 적절한 pre값 산출을 위해 post가 필요한가보다.
    */

    int index2=0;
    for(index2=0;index2<8;index2++)
    {
        printf("\n%d -> Node#%d in picture ( %d, %d)/\n",index2, index2+1,pre[index2],post[index2]);
    }
    printf("\n");

    //pre 값이 작은순으로 출력해보자.
    int* sorted_pre;
    sorted_pre=bubbleinsertion(pre);

    printf("방문순서(pre작은순) : ");
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
    //그래프를 배열로
    //DFS 알고리즘 wiht recursive
    //시작 노드는 1, 방문순서 출력.

    //printf("%d",visited[0]);
    printf("pre가 교재에 1부터길래 1로 시작하였습니다.\n");

    //picture 기준
    int start_vertice_num=1;

    //0부터 재인덱싱 해기.
    start_vertice_num=start_vertice_num-1;

    DepthFirstSearch(start_vertice_num);



    printf("Hello world!\n");
    return 0;
}
