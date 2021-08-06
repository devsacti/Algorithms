#include <stdio.h>
#include <stdlib.h>

#define LENGTH 1024

char *pLine;//���۷κ��� ���ڿ� ���޹��� ������.
int arr[LENGTH];
int len_index=0;

void FiletoArr()
{
    char line[LENGTH];//buffer

    FILE *in = fopen("input.txt", "r");//�Է� ��Ʈ�� ����.
    while (!feof(in)) {
        pLine = fgets(line, LENGTH, in);//buffer, length, stream
        printf("First Input row %s\n", pLine);
    }
    fclose(in);


    int i=0;

    char *temp = strtok(pLine," "); //\t �������� ���ڿ� �ڸ���, ù��° ����

    //���� �ƴҶ����� �۵�.
    while (temp != NULL)
    {
        arr[i++]=atoi(temp);
        temp = strtok(NULL, " ");//��ݾ��� ���� �����ϴµ�, �۵� �� ������ ��� ���� ���ε�.
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


//bubbleup, argument 'index_NextofLast'�� ������ ������ +1�Ǳ� ������
//������ �迭 ���� �����ڸ��� ��������.
void bubbleup(Segment h[], Segment key, int index_NextofLast)
{
    h[index_NextofLast] = key; // �ϴ�, �迭�� ���������ٰ� key�� ��ġ

    //�Ǹ����� �迭������ ���� �ڸ����� �����Ͽ� parent index�� �����ϱ� ���� ��������.
    //�״�� �ᵵ ������ ���� �򰥸�.
    int index_child=index_NextofLast;
    // p is parent's index, ���� ���� ���� ������ ��ġ�� ã�� ���ؼ� ������ ��.
    int p = ceil(index_child/2);
    Segment temp;
    //Ű������ �θ� ũ�� Ű���� ���� �÷����ϴϱ� �Ʒ�ó�� �ε�ȣ,
    // ���� �ִ��� heap array�� �ε����� -1, �� �迭 ���̰� 1�̸� �н�.
    while(index_child != (0) && h[p].length_segment > key.length_segment)
    {
        temp = h[index_child];// ���� ����
        h[index_child]= h[p];// �θ��� Ű���� ��� ���� �ְ�
        h[p]= temp;// ������ Ű���� �θ� �ڸ��� �ֱ�.

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
void insert(Segment h[], Segment key,int h_index_size)
{
    bubbleup(h, key, h_index_size);
}

//'i'�� �θ��� �ε������ ������ ��
//����, ������ �ڽ� �߿��� minimum_child's index�� ã��.
int minimum_child(Segment h[], int i)
{
    /*
    2i+1�� h index size ���� ũ�ٴ� �� �ڽ��� �ε����� ���� ũ�⸦ �Ѿ�ٴ� �ǹ�.
    �� ��� ���ʿ� ��尡 1���ų�, shiftdown�� �Ϸ�Ȱ�.

    ��尡 1���� ���, ������� �θ� �ε����� �ڱ��ڽ��� 0�ε�
    ����, level 2 �̻󿡼� �ڽ��� ���� ���
    */
    if(2*i+1 > h_index_size || 2*i+2 > h_index_size)
        return (0);
    else//���� �ڽİ� ������ �ڽ� �� ���� ���� �ε����� ������.
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
//shift down for min heap, makeheap�� �ʿ������� deletemin�� �ݵ�� �ʿ��� �Լ��ε�.
//key_h�� h�� ���ҵ�� ���ڸ��� ã�� �� �̴�.
void shiftdown(Segment h[], Segment key_h, int index_p)
{
    //printf("%d--",index_p);
    //printf("%4d--",key_h);

    int c = minimum_child(h, index_p);
    //printf("%d--",c);
    Segment temp;
    h[index_p] = key_h;
    //printf("%d\n", h[index_p]);
    //������ ������
    //h[9]�� ����ǰų� ���ǵ��� ��������, c=9�̰� h[c]�� 0���� ���ֵǾ� �����߻�.
    //�Ʒ� while���� && c<9�ʵ� �ǳ� ���� �� minimum_child �Լ� ����.
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
S�� Series of input���� �����ϸ� ���ҵ�,
input, desti, condition ���̾��µ�, insert�� ���缭
destini, input, conditon ���� ����.
*/
void makeheap(Segment h[],Segment S[], int len_S)
{
    int i;
    for(i=(0); i<len_S; i++)
    {
        h_index_size++;// ���� heap array�� 1ĭ Ȯ���Ѵٴ� ����, for insert.
        //printf("%d\n", h_index_size);
        //insert(h, S[i]);

        //insert �ȿ� bubbleup�� ������ h index size ������Ų�Ŵ�, �� ���ظ� ���� ����
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
    //����ġ ���ϰ� ������ ����Ʈ�� ī��Ʈ�� �ȵǼ� �˾Ƽ� ���ϵ��� �۵�.
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

    //�־��� ����� �ε����� ���Ͻ�Ű���� 0�Ⱦ� ����.
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
