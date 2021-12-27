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
    printf("last of index : %d\n",len_index);
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

int main()
{
    //arr ����
    FiletoArr();
    int len_arr=len_index+1;

    //�����̶� dptable ����
    int sequence[len_arr];
    int i;
    for(i=0;i<len_arr;i++)
    {
        sequence[i]=arr[i];
    }

    int dp_table[len_arr];
    for(i=0;i<len_arr;i++)
    {
        dp_table[i]=1;
    }

    int max=0;

    max=dp(sequence,dp_table,len_arr);

    printf("length of LIS :%d\n", max);

    printf("Hello world!\n");
    return 0;
}
