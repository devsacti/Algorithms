#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LENGTH_ARRAY 33
#define LENGTH_BUFFER 1024

int* S;
int h[];
int index_size_heap = -1;

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
    while (temp != NULL)//���� �ƴҶ����� �ݺ�
    {
        //printf("%s\n",temp); // ���
        arr[i]=atoi(temp);
        //printf("%d ",arr[i]);
        ++i;
        temp = strtok(NULL, "\t");
    }
    printf("\n");

    return arr;
}

void insert(int h[], int x)
{
    bubbleup(h, x, index_size_heap);
}

void bubbleup(int h[], int x, int i)
{
    h[i] = x;

    int p = ceil(i/4);
    // �̷��� �ϸ�, level 1�� 4���� ��� �θ��带 �ǿ��� �ڽ����� ����. level2�� �� ������ h[2]�� ù �θ���� �����ٰ� h[1]��.
    //���߿� shiftdown���� ������ ��迭 �ҰŴϱ� �̷��� rough�ϰ� �Ҵ��ϴµ�.
    //�ٸ� �̰��, �̶� p�� �θ��� �ε��� �� ��������� �ε����� ��¡.
    int temp;

    while(i != 0 && h[p] > x)
    {
        temp = h[i];
        h[i] = h[p];
        h[p] = temp;
        i = p;
        p = ceil(i/4);//�̰ɷ� p�� i�� �������� x==h[p]�� while�� �ƿ�.
    }
}

int minimum_child(int h[], int i)
{
    int p;
    int min;
    if(4*i+1 > index_size_heap)
        return 0;
    else{
        min = h[4*i+1];
        for(p=4*i+1; p <= 4*i+4 ; p++)
        {
            if(min > h[p])
                min = h[p];
        }
        if(min == h[4*i+1])
            return 4*i+1;
        else if(min == h[4*i+2])
            return 4*i+2;
        else if(min == h[4*i+3])
            return 4*i+3;
        else if(min == h[4*i+4])
            return 4*i+4;
    }
}

void shiftdown(int h[], int x, int i)
{
    int c = minimum_child(h, i);
    int temp;
    h[i] = x;
    while(c != 0 && h[c] < x)
    {
        temp = h[i];
        h[i] = h[c];
        h[c] = temp;
        i = c;
        c = minimum_child(h, i);
    }
}


void makeheap(int S[], int h[])
{
    int i;
    for(i=0; i<LENGTH_ARRAY; i++)
    {
        index_size_heap++;
        insert(h, S[i]);
    }
    printf("\n\nheap array before shiftdown\n");

    for(i=0; i<LENGTH_ARRAY; i++)
    {
        printf("%d ", h[i]);
    }

    for(i=0; i<LENGTH_ARRAY; i++)
        shiftdown(h, h[i], i);

}

int deleteMin(int h[])
{
    int x;
    if(index_size_heap == -1)
        return -1000;
    else{
        x = h[0];
        shiftdown(h, h[index_size_heap], 0);
        h[index_size_heap] = 1000;
        index_size_heap--;
        return x;
    }
}


int main()
{
    S=FiletoArray();

    int len_index=0;
    int i=0;
    for(i=0;S[i]!=0;i++)
    {
        printf("%d ",S[i]);
        len_index=i;
    }
    printf("\n\n");

    printf("Input array S : ");
    for(i=0;i<len_index+1;i++)
    {
        printf("%d ", S[i]);
    }

    makeheap(S, h);
    printf("\n\n");

    printf("Quaternary Heap Array: \n");
    while(index_size_heap != -1)
    {
        printf("%d ", deleteMin(h));
    }
    printf("\nHello world!\n");
    return 0;
}
