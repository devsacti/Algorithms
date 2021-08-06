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

    char *temp = strtok(pLine," "); //space 기준으로 문자열 자르기, 첫번째 리턴

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
    //arr 생성
    FiletoArr();
    int len_arr=len_index+1;

    //수열이랑 dptable 생성
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
