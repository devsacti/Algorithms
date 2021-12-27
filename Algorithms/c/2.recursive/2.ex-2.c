#include <stdio.h>

double Exponential_Taylorf(double x, double n)
{
    if(n==30)//upper limitation
    {
        return 0;
    }

    return 1+(x/n)*Exponential_Taylorf(x,n+1);
}

int main()
{

    double x,n=0;

    while(scanf("%lf %lf", &x,&n)!=EOF)
    {
        printf("the value of power of exponential : %f\n", x);
        printf("the value of n that defines starting step of recursive function %f\n", n);
        printf("the result of Taylor : %f\n", Exponential_Taylorf(x,n));
    }

    return 0;
}
