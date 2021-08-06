#include <stdio.h>
#include <stdlib.h>

#define LENGTH 1024

char *pLine;//버퍼로부터 문자열 전달받을 포인터.
int arr[LENGTH];
int len_index=0;

void FiletoArr()
{
    char line[LENGTH];//buffer

    FILE *in = fopen("input.txt", "r");//입력 스트림 생성.
    while (!feof(in)) {
        pLine = fgets(line, LENGTH, in);//buffer, length, stream
        printf("First Input row %s\n", pLine);
    }
    fclose(in);


    int i=0;

    char *temp = strtok(pLine," "); //\t 기준으로 문자열 자르기, 첫번째 리턴

    //널이 아닐때까지 작동.
    while (temp != NULL)
    {
        arr[i++]=atoi(temp);
        temp = strtok(NULL, " ");//뜬금없이 널을 대입하는데, 작동 중 구분자 대신 넣을 값인듯.
    }

    for(i=0;arr[i]!=0;i++){
        printf("%d ",arr[i]);
        len_index=i;
    }
    printf("\n");
    printf("length of 'index of arr', not arr : %d\n",len_index);
}

typedef struct segment{
    int startpoint;
    int endpoint;
    int length_segment;
}Segment;

int min_point;
int max_point;

void make_segment(int arr[], Segment arr_segment[])
{
    int i;

    min_point=1000;
    max_point=-1000;

    for(i=0;i<(len_index+1);i++)
    {
        if(i%2==0)
        {
            if(arr[i]<min_point)
            {
                min_point=arr[i];
            }
            arr_segment[i/2].startpoint=arr[i];
        }
        else
        {
            if(arr[i]>max_point)
            {
                max_point=arr[i];
            }
            arr_segment[(i-1)/2].endpoint=arr[i];
            arr_segment[(i-1)/2].length_segment=arr_segment[(i-1)/2].endpoint-arr_segment[(i-1)/2].startpoint;
        }

    }
}

Segment h[10];
int h_index_size = (-1);


//bubbleup, argument 'index_NextofLast'는 들어오기 직전에 +1되기 때문에
//마지막 배열 원소 다음자리에 대응가능.
void bubbleup(Segment h[], Segment key, int index_NextofLast)
{
    h[index_NextofLast] = key; // 일단, 배열의 마지막에다가 key를 배치

    //맨마지막 배열원소의 다음 자리부터 시작하여 parent index를 설정하기 위해 변수설정.
    //그대로 써도 되지만 내가 헷갈림.
    int index_child=index_NextofLast;
    // p is parent's index, 새로 들어온 값의 적절한 위치를 찾기 위해서 정의한 값.
    int p = ceil(index_child/2);
    Segment temp;
    //키값보다 부모가 크면 키값을 위로 올려야하니까 아래처럼 부등호,
    // 한편 애당초 heap array의 인덱스가 -1, 즉 배열 길이가 1이면 패스.
    while(index_child != (0) && h[p].length_segment > key.length_segment)
    {
        temp = h[index_child];// 짐을 비우고
        h[index_child]= h[p];// 부모의 키값을 비운 곳에 넣고
        h[p]= temp;// 빼놓은 키값을 부모 자리에 넣기.

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
void insert(Segment h[], Segment key,int h_index_size)
{
    bubbleup(h, key, h_index_size);
}

//'i'를 부모노드 인데스라고 생각할 때
//왼쪽, 오른쪽 자식 중에서 minimum_child's index를 찾자.
int minimum_child(Segment h[], int i)
{
    /*
    2i+1이 h index size 보다 크다는 건 자식의 인덱스가 힙의 크기를 넘어선다는 의미.
    이 경우 애초에 노드가 1개거나, shiftdown이 완료된것.

    노드가 1개인 경우, 원래라면 부모 인덱스는 자기자신인 0인데
    한편, level 2 이상에서 자식이 없는 노드
    */
    if(2*i+1 > h_index_size || 2*i+2 > h_index_size)
        return (0);
    else//왼쪽 자식과 오른쪽 자식 중 작은 놈의 인덱스를 구하자.
    {
        if(h[2*i+1].length_segment < h[2*i+2].length_segment)
        {
            return 2*i+1;
        }
        else
        {
            return 2*i+2;
        }
    }
}
//shift down for min heap, makeheap도 필요하지만 deletemin에 반드시 필요한 함수인듯.
//key_h는 h의 원소들로 제자리를 찾기 전 이다.
void shiftdown(Segment h[], Segment key_h, int index_p)
{
    //printf("%d--",index_p);
    //printf("%4d--",key_h);

    int c = minimum_child(h, index_p);
    //printf("%d--",c);
    Segment temp;
    h[index_p] = key_h;
    //printf("%d\n", h[index_p]);
    //이유는 모르지만
    //h[9]는 선언되거나 정의되지 않음에도, c=9이고 h[c]는 0으로 간주되어 문제발생.
    //아래 while에서 && c<9너도 되나 역할 상 minimum_child 함수 변형.
    while(c != (0) && h[c].length_segment < key_h.length_segment)
    {
        temp = h[index_p];
        h[index_p]= h[c];
        h[c]= temp;
        //printf("%d++\n", h[c]);
        index_p = c;
        c = minimum_child(h, index_p);
    }
}


/*
make heap
S는 Series of input으로 이해하면 편할듯,
input, desti, condition 꼴이었는데, insert랑 맞춰서
destini, input, conditon 으로 변형.
*/
void makeheap(Segment h[],Segment S[], int len_S)
{
    int i;
    for(i=(0); i<len_S; i++)
    {
        h_index_size++;// 현재 heap array를 1칸 확장한다는 느낌, for insert.
        //printf("%d\n", h_index_size);
        //insert(h, S[i]);

        //insert 안에 bubbleup에 쓸려고 h index size 증가시킨거니, 내 이해를 위해 변형
        insert(h, S[i], h_index_size);
    }

    for(i=(0+1); i<len_S; i++)
        shiftdown(h, h[i], i);
}

//deletemin
Segment deleteMin(Segment h[])
{
    Segment x;

    if(h_index_size == (-1))
    {
        printf("heap is empty\n");
        return;
    }
    else
    {
        x = h[(0)];
        shiftdown(h, h[h_index_size], (0));
        h[h_index_size].length_segment = 1000;
        h_index_size--;
        //printf("(%d,%d) %d ",x.startpoint, x.endpoint, x.length_segment);
        return x;
    }
}

int test_if_there_is_segment(int start, int offset, int arr_selected[])
{
    //생각치 못하게 마지막 포인트는 카운트가 안되서 알아서 원하든대로 작동.
    for(offset;offset!=0;offset--)
    {
        if(arr_selected[start]!=0)
        {
            return 1;
        }
        start++;
    }
    return 0;
}

void printer_arr(int arr[],int index_size_arr)
{
    int i;
    for(i=1;i<index_size_arr+1;i++)
        printf("%d ", arr[i]);

    printf("\n");
}


int main()
{
    FiletoArr();

    int length_arr_segment=(len_index+1)/2;

    printf("\n\making segment struct\n");
    Segment arr_segment[length_arr_segment];

    make_segment(arr,arr_segment);

    printf("length of segment : ");
    int i;
    for(i=0;i<length_arr_segment;i++)
    {
        printf("(%d,%d) %d ",arr_segment[i].startpoint,arr_segment[i].endpoint,arr_segment[i].length_segment);
    }
    printf("\n");

    printf("min and max point : %d %d\n", min_point,max_point);

    printf("\nMaking heap of Segment,Testing the deletemin : \n");
    makeheap(h,arr_segment,10);
    Segment result;
    for(i=0;i<10;i++)
    {
        result=deleteMin(h);
        printf("(%d,%d) %d ",result.startpoint, result.endpoint, result.length_segment);
    }
    printf("\n");

    //주어진 점들과 인덱스를 통일시키려고 0안쓸 예정.
    int arr_selected_segment[max_point+1];

    printf("\nMake the coordinate system : \n");
    for(i=1;i<max_point+1;i++)
    {
        arr_selected_segment[i]=0;
        printf("%d ",arr_selected_segment[i]);
    }

    printf("\nMaking heap of Segment, Again : \n");
    makeheap(h,arr_segment,10);


    printf("\nSelect Segment based on length asc : \n");
    int start,offset;
    int CNT_updated_segment=0;
    for(i=0;i<10;i++)
    {
        printf("############################\n");
        printer_arr(arr_selected_segment,13);
        //step1 pop based on length of segment asc
        result=deleteMin(h);
        printf("(%d,%d) length %d\n",result.startpoint, result.endpoint, result.length_segment);

        //update the arr_selected_segment only if there is no segment
        if(test_if_there_is_segment(result.startpoint,result.length_segment,arr_selected_segment)==0)
        {
            CNT_updated_segment++;
            start=result.startpoint;
            offset=result.length_segment;
            for(offset;offset>=0;offset--)
            {
                arr_selected_segment[start]=start;
                start++;
            }
        }
        printer_arr(arr_selected_segment,13);
    }
    printf("\n");

    printf("\nshow the coordinate system and CNT of used segment : \n");
    printer_arr(arr_selected_segment,13);
    printf("CNT %d\n", CNT_updated_segment);

    printf("Hello world!\n");
    return 0;
}
