#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LENGTH_ARRAY 1024
#define LENGTH_BUFFER 1024

int* S;
int h[];
int h_index_size = -1;// stack���� top�̶� ���� �����ε�.

int* FiletoArray()
{
    static int arr[LENGTH_ARRAY]={0};

    int *pLine;//���۰��� ���޹޾� ������ �迭.

    int line[LENGTH_BUFFER];//buffer
    int i=0;

    FILE *in = fopen("input.txt", "r");//�Է� ��Ʈ�� ����.
    //while (!feof(in)) {
        pLine = fgets(line, LENGTH_BUFFER, in);
        printf("%s\n", pLine);
    //}
    fclose(in);

    int *temp = strtok(pLine,"\t"); //\t �������� ���ڿ� �ڸ���, �� �� ���� ����ȴ�.
    while (temp != NULL) { //���� �ƴҶ����� �ݺ�
        //printf("%s\n",temp); // ���
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
    h[i] = key; // �ϴ�, �迭�� ���������ٰ� key�� ��ġ

    // p is parent's index, ���� ���� ���� ������ ��ġ�� ã�� ���ؼ� ������ ��.
    //int p = ceil(i/2); // ������ ���� �𸣰ھ �н�.
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
    //Ű������ �θ� ũ�� Ű���� ���� �÷����ϴϱ� �Ʒ�ó�� �ε�ȣ,
    // ���� �ִ��� heap array�� �ε����� 0, �� �迭 ���̰� 1�̸� �н�.
    while(i != 0 && h[p] > key)
    {
        temp = h[i];// ���� ����
        h[i] = h[p];// �θ��� Ű���� ��� ���� �ְ�
        h[p] = temp;// ������ Ű���� �θ� �ڸ��� �ֱ�.

        // �θ��带 ����Ű�� p�� child�� i�� ������,
        //���� ����� child�� �����͵� �θ��带 ����Ų�ٰ� ���ذ���.
        i = p;
        //�׸��� �Ʒ����� �θ��带 ����Ű�� ������ �����͸� level�� ���� �÷��� ��������� ����.
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
//insert, key comes from input array S by 'for��'
void insert(int h[], int key){
    bubbleup(h, key, h_index_size);
}

//'i'�� �θ��� �ε������ ������ ��
//����, ������ �ڽ� �߿��� minimum_child's index�� ã��.
int minimum_child(int h[], int i)
{
    if(2*i+1 > h_index_size)
        return 0;
    else//���� �ڽİ� ������ �ڽ� �� ���� ���� �ε����� ������.
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
//shift down for min heap, makeheap ���� deletemin�� �ݵ�� �ʿ��� �Լ��ε�.
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
        h_index_size++;// ���� heap array�� 1ĭ Ȯ���Ѵٴ� ����, for insert.
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

    printf("heap array before deletemin after shiftdown_���� �� ������ ���Խ�Ű�� ���⼱ �ʿ���µ�_ in makeheap \n");
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
