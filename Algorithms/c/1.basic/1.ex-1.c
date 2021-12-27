#include <stdio.h>

int main()
{
    int e;

    while(scanf("%d", &e) !=EOF)
    {
        switch(e)
        {
            case 1:
                printf("Welcome to Woong-Sup's Algorithm Class\n");
                break;
            case 2:
                printf("GoodLuck for 2020 class\n");
                break;
            case 3:
                exit(0);
                //break;
            default:
                printf("please select in 1,2,3\n");
                break;
                //exit(0);
        }
    }

}
