#include <stdio.h>
#include <stdlib.h>

char *pLine;//���ۿ� ������;����.
int arr[1024]={0};
int len_index=0;

void FiletoArr()
{
    const int max = 1024;
    char line[max];//buffer

    FILE *in = fopen("input.txt", "r");//�Է� ��Ʈ�� ����.
    while (!feof(in)) {
        pLine = fgets(line, max, in);
        printf("%s\n", pLine);
    }
    fclose(in);

    char *temp = strtok(pLine,"\t"); //\t �������� ���ڿ� �ڸ���

    int i=0;
    while (temp != NULL) { //���� �ƴҶ����� �ݺ�
        //printf("%s\n",temp); // ���
        arr[i++]=atoi(temp);
        //printf("%d\n",arr[i++]);
        temp = strtok(NULL, "\t");
    }
    //printf("Hello world2!\n");

    for(i=0;arr[i]!=0;i++){
        printf("%d ",arr[i]);
        len_index=i;
    }

}

void insertion_sort(int list[], int n){
  int i, j, key;

  // ���ؽ� 0�� ���� -1�� ���ĵ� ����� ���
  for(i=1; i<n; i++){
    key = list[i]; // ���� ���Ե� ������ i��° ������ key ������ ����

    for(j=i-1; j>=0 && list[j]>key; j--){
      list[j+1] = list[j]; // ���ڵ��� ���������� �̵�
    }

    list[j+1] = key;
  }
}

int main()
{
    FiletoArr();
    insertion_sort(arr,len_index+1);

    printf("\n\n");

    int i=0;
    for(i=0;arr[i]!=0;i++){
        printf("%d ",arr[i]);
    }


    return 0;
}
