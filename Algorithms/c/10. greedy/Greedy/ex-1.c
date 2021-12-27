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

    char *temp = strtok(pLine,"\t"); //\t 기준으로 문자열 자르기, 첫번째 리턴

    //널이 아닐때까지 작동.
    while (temp != NULL)
    {
        arr[i++]=atoi(temp);
        temp = strtok(NULL, "\t");//뜬금없이 널을 대입하는데, 작동 중 구분자 대신 넣을 값인듯.
    }

    for(i=0;arr[i]!=0;i++){
        printf("%d ",arr[i]);
        len_index=i;
    }
    printf("\n");
    printf("%d\n",len_index);
}

void counter_bottle(int arr[])
{
    int j,i;
    int quantity;
    int cup_300,cup_500;
    /*
    우선 500에 대한 몫과 나머지로 표현하고
    이 나머지를 300에 대한 몫과 나머지로 표현하다보면
    주어진 것을 500과 300으로 쪼개는 듯한 효과.

    가 아니라, 일단 500짜리 빼고 나머지에서 300단위 확인하고
    반복인듯.
    */

    for(j=0;j<len_index+1;j++)
    {
        cup_300=0;
        cup_500=0;
        quantity=arr[j];
        printf("given quantity of bottel : %d\n",quantity);
        for(i=quantity/500;i>=0;i--)
        {
            //300과 500의 최소공배수의 배수를 포괄해서 500의 배수면 500짜리로 다하는 게 최적.
            if(quantity%500==0)
            {
                cup_500=quantity/500;
                printf("%d\n",cup_500);
                break;
            }
            else if(quantity%300==0 )
            {
                cup_300=quantity/300;
            }
            else
            {
                //500 one time
                quantity=quantity-500;
                if(quantity<0)
                {

                    cup_300=-1;
                    cup_500=0;
                    break;

                }
                cup_500=cup_500+1;
            }
        }
        //printf("CNT of 300 : %d\n",cup_300);
        printf("CNT of total : %d\n",cup_300+cup_500);
    }
}

int main()
{
    FiletoArr();

    counter_bottle(arr);

    printf("Hello world!\n");
    return 0;
}
