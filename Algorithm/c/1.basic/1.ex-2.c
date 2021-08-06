#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct point{
    int x;
    int y;
}coordinate;

int main()
{
    double distance_zero;//distance from the zero

    int cnt_a, cnt_b=0;//count of a or b
    int n;//total count of making coordinate of two dimension

    double approximate_pi;

    srand((unsigned int)time(NULL));

    for(int i=0; i<1000; i++)//making coordinate of two dimension 1000 times
    {
        coordinate pointpoint={(int) ((double)rand()/RAND_MAX*10 ),(int) ((double)rand()/RAND_MAX*10 )};
        //double은 소수점화를 위해,RAND_MAX=32767

        distance_zero=sqrt( (pointpoint.x*pointpoint.x)+(pointpoint.y*pointpoint.y) );

        if(distance_zero<=10)//distance is less than 10 from the zero
            cnt_a++;
        else
            cnt_b++;

    }
    printf("a의 갯수, b의 갯수: %d %d\n", cnt_a, cnt_b);

    n=cnt_a+cnt_b;
    printf("전체 점의 갯수: %d\n", n);

    approximate_pi=(double)4*cnt_a/n;

    printf("%lf\n", approximate_pi);
}
