#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LENGTH_ARRAY 1024
#define LENGTH_BUFFER 1024

int* S;
int h[];
int h_index_size = -1;// stack에서 top이랑 같은 역할인듯.

int* FiletoArray()
{
    static int arr[LENGTH_ARRAY]={0};

    int *pLine;//버퍼값을 전달받아 저장할 배열.

    int line[LENGTH_BUFFER];//buffer
    int i=0;

    FILE *in = fopen("input.txt", "r");//입력 스트림 생성.
    //while (!feof(in)) {
        pLine = fgets(line, LENGTH_BUFFER, in);
        printf("%s\n", pLine);
    //}
    fclose(in);

    int *temp = strtok(pLine,"\t"); //\t 기준으로 문자열 자르기, 맨 앞 값이 저장된다.
    while (temp != NULL) { //널이 아닐때까지 반복
        //printf("%s\n",temp); // 출력
        arr[i]=atoi(temp);
        //printf("%d ",arr[i]);
        ++i;
        temp = strtok(NULL, "\t");
    }
    printf("\n");

    return arr;
}

//bubbleup, argument 'i' means index size of heap
void bubbleup(int h[], int key, int i)
{
    h[i] = key; // 일단, 배열의 마지막에다가 key를 배치

    // p is parent's index, 새로 들어온 값의 적절한 위치를 찾기 위해서 정의한 값.
    //int p = ceil(i/2); // 원리가 뭔지 모르겠어서 패스.
    int p;
    if( i%2 == 1)
    {
        p= (i-1)/2;
    }
    else
    {
        p= (i-2)/2;
    }

    int temp;
    //키값보다 부모가 크면 키값을 위로 올려야하니까 아래처럼 부등호,
    // 한편 애당초 heap array의 인덱스가 0, 즉 배열 길이가 1이면 패스.
    while(i != 0 && h[p] > key)
    {
        temp = h[i];// 짐을 비우고
        h[i] = h[p];// 부모의 키값을 비운 곳에 넣고
        h[p] = temp;// 빼놓은 키값을 부모 자리에 넣기.

        // 부모노드를 가리키던 p를 child의 i에 덮어씌우면,
        //여기 행까진 child의 포인터도 부모노드를 가리킨다고 이해가능.
        i = p;
        //그리고 아랭세서 부모노드를 가리키는 일종의 포인터를 level상 한층 올려서 재귀적으로 실행.
        if( i%2 == 1)
        {
            p= (i-1)/2;
        }
        else
        {
            p= (i-2)/2;
        }
    }
}
//insert, key comes from input array S by 'for문'
void insert(int h[], int key){
    bubbleup(h, key, h_index_size);
}

//'i'를 부모노드 인데스라고 생각할 때
//왼쪽, 오른쪽 자식 중에서 minimum_child's index를 찾자.
int minimum_child(int h[], int i)
{
    if(2*i+1 > h_index_size)
        return 0;
    else//왼쪽 자식과 오른쪽 자식 중 작은 놈의 인덱스를 구하자.
    {
        if(h[2*i+1] < h[2*i+2])
        {
            return 2*i+1;

        }
        else
        {
            return 2*i+2;
        }
    }
}
//shift down for min heap, makeheap 보단 deletemin에 반드시 필요한 함수인듯.
void shiftdown(int h[], int last_key_value_h, int index_p)
{
    int c = minimum_child(h, index_p);
    int temp;
    h[index_p] = last_key_value_h;
    while(c != 0 && h[c] < last_key_value_h)
    {
        temp = h[index_p];
        h[index_p] = h[c];
        h[c] = temp;
        index_p = c;
        c = minimum_child(h, index_p);
    }
}

//make heap
void makeheap(int S[], int h[], int len_S)
{
    int i;
    for(i=0; i<len_S; i++)
    {
        h_index_size++;// 현재 heap array를 1칸 확장한다는 느낌, for insert.
        insert(h, S[i]);
    }
    printf("\n\n");

    printf("heap array before shiftdown in makeheap\n");
    for(i=0;h[i]!=0;i++)
    {
        printf("%d ",h[i]);
    }
    printf("\n\n");

    for(i=0; i<len_S; i++)
        shiftdown(h, h[i], i);
}

//deletemin
int deleteMin(int h[])
{
    int x;
    if(h_index_size == -1)
        return -1000;
    else
    {
        x = h[0];
        shiftdown(h, h[h_index_size], 0);
        h[h_index_size] = 1000;
        h_index_size--;
        return x;
    }
}

int main()
{
    S=FiletoArray();

    printf("S which means series of input : ");
    int size_index_S=0;
    int i=0;
    for(i=0;S[i]!=0;i++)
    {
        printf("%d ",S[i]);
        size_index_S=i;
    }

    printf("\nrange of index %d, length of S array : %d ", size_index_S,size_index_S+1 );

    makeheap(S, h, (size_index_S+1) );

    printf("heap array before deletemin after shiftdown_넣을 때 엄밀히 대입시키면 여기선 필요없는듯_ in makeheap \n");
    for(i=0;h[i]!=0;i++)
    {
        printf("%d ",h[i]);
    }
    printf("\n\nh: ");

    while(h_index_size != -1)
    {
        printf("%d ", deleteMin(h));
    }
    printf("\nHello world!, I escaped from HW at least this time\n.");
    return 0;
}
