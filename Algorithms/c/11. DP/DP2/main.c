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

    char *temp = strtok(pLine," "); //space �������� ���ڿ� �ڸ���, ù��° ����

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
    printf("%d\n",len_index);
}

int dp(int arr[],int dp_table[], int len_arr)
{
    int last_index_seq=0;
    int max=0;

    int i,j;
    for(i=0;i<len_arr+1;i++)
    {
        last_index_seq=0;

        for(j=0;j<i;j++)
        {
            if(arr[i]>arr[j] )
            {
                last_index_seq=dp_table[j];
            }
        }

        dp_table[i]=last_index_seq+1;
        if(max<dp_table[i])
        {
            max=dp_table[i];
        }
    }

    return max;
}

int find_index_arr(int sequence[],int dp_table[], int len_arr, int val)
{
    int i;
    //���� ������̴ϱ�, �������� ���� dp�� ���Ƶ� ���ڴ� �۾ƾ��ҵ�
    int min=1000;

    //�˼����¹����� ���޹����� 10�� 1�� �ٲ�, ������ �ʱ�ȭ
    printf("sequence : ");
    for(i=0;i<len_arr;i++)
    {
        //printf("%d ",arr[i]);
        sequence[i] = arr[i];
        printf("%d ",sequence[i]);
    }
    printf("\n");

    for(i=0;i<len_arr;i++)
    {
        if(dp_table[i]==val)
        {
            //printf("%d\n", i);
            //printf("%d\n", sequence[i]);
            if(sequence[i]<min)
            {
                //printf("%d\n", sequence[i]);
                min=sequence[i];
                //printf("%d\n", min);
            }
        }
    }

    for(i=0;len_arr;i++)
    {
        if(arr[i]==min)
        {
            return i;
        }
    }
}

int main()
{
    //arr ����
    FiletoArr();
    int len_arr=len_index+1;
    printf("%d \n",len_arr);

    //���� �ʱ�ȭ
    int sequence[8];
    int i;

    printf("sequence : ");
    for(i=0;i<len_arr;i++)
    {
        //printf("%d ",arr[i]);
        sequence[i] = arr[i];
        printf("%d ",sequence[i]);
    }
    printf("\n");

    //dp_table �ʱ�ȭ
    int dp_table[len_arr];
    for(i=0;i<len_arr;i++)
    {
        dp_table[i]=1;
    }

    int max=0;
    max=dp(sequence,dp_table,len_arr);
    printf("length of LIS :%d\n", max);

    printf("dp_table : ");
    for(i=0;i<len_arr;i++)
    {
        printf("%d ", dp_table[i]);
    }
    printf("\n");




    //�κм����� ��
    int sum_subseq=0;
    int index;

    for(i=1; i<=max ;i++)
    {
        index=find_index_arr(sequence,dp_table,len_arr,i);
        printf("val : %d\n",arr[index]);
        sum_subseq+=arr[index];
    }

    printf("sum : %d\n",sum_subseq);

    printf("Hello world!\n");
    return 0;
}
