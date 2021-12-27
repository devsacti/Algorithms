#include <stdio.h>
#include <stdlib.h>

char *pLine;//버퍼용 포인터;한줄.
int arr[1024]={0};
int len_index=0;

void FiletoArr()
{
    const int max = 1024;
    char line[max];//buffer

    FILE *in = fopen("input.txt", "r");//입력 스트림 생성.
    while (!feof(in)) {
        pLine = fgets(line, max, in);
        printf("%s\n", pLine);
    }
    fclose(in);

    char *temp = strtok(pLine,"\t"); //\t 기준으로 문자열 자르기

    int i=0;
    while (temp != NULL) { //널이 아닐때까지 반복
        //printf("%s\n",temp); // 출력
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

  // 인텍스 0의 값은 -1과 정렬된 결과라 상상
  for(i=1; i<n; i++){
    key = list[i]; // 현재 삽입될 숫자인 i번째 정수를 key 변수로 복사

    for(j=i-1; j>=0 && list[j]>key; j--){
      list[j+1] = list[j]; // 레코드의 오른쪽으로 이동
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
