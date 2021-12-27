#include <stdio.h>
#include <stdlib.h>


#define TABLE_SIZE 512
int main()
{
    char str[13]="Hello world!";

    int i,h;

    for(i=0,h=0; i < strlen(str); i++)
    {
        printf("%d \n", i);
        printf("-%d %c\n", str[i], str[i]);
        printf("--%d\n", h*h);

        h = (str[i] + h*h)%TABLE_SIZE;
        printf("%d \n", h);
    }

    printf("--%d\n", str[3]+5);





    return 0;
}
