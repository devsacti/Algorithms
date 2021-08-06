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

    char *temp = strtok(pLine,"\t"); //\t �������� ���ڿ� �ڸ���, ù��° ����

    //���� �ƴҶ����� �۵�.
    while (temp != NULL)
    {
        arr[i++]=atoi(temp);
        temp = strtok(NULL, "\t");//��ݾ��� ���� �����ϴµ�, �۵� �� ������ ��� ���� ���ε�.
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
    �켱 500�� ���� ��� �������� ǥ���ϰ�
    �� �������� 300�� ���� ��� �������� ǥ���ϴٺ���
    �־��� ���� 500�� 300���� �ɰ��� ���� ȿ��.

    �� �ƴ϶�, �ϴ� 500¥�� ���� ���������� 300���� Ȯ���ϰ�
    �ݺ��ε�.
    */

    for(j=0;j<len_index+1;j++)
    {
        cup_300=0;
        cup_500=0;
        quantity=arr[j];
        printf("given quantity of bottel : %d\n",quantity);
        for(i=quantity/500;i>=0;i--)
        {
            //300�� 500�� �ּҰ������ ����� �����ؼ� 500�� ����� 500¥���� ���ϴ� �� ����.
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
