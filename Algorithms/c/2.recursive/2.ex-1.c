#include <stdio.h>

long combination(int n, int r)
{
    if(r==0||r==n)
    {
        return 1L;//n combination c==1, if n==0,r==n
    }
    return combination(n-1,r-1)+combination(n-1,r);
}

int main()
{

    int i,j=0;

    while(scanf("%d %d", &i,&j)!=EOF)
    {
        printf("%dC%d = %d\n", i,j, combination(i,j));
    }


    return 0;
}
