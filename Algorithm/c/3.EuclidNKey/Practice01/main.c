#include <stdio.h>
#include <stdlib.h>

/*


*/
//a*x+b*y=gcd(a,b) is background
struct _node
{
    int first;//x
    int second;//y
    int third;//gcd
};

//확장 유클리드.
struct _node* extended_Euclid(int a, int b)
{
    struct _node *n1,*n2;

    n1=(struct _node*)malloc(sizeof(struct _node));

    if(b==0)
    {
        n1->first=1;
        n1->second=0;//b=0
        n1->third=a;
        return n1;//n1=(1,0,a)
    }
    else
    {
        n2=extended_Euclid(b,a%b);

        n1->first=n2->second;//x'
        n1->second=(n2->first)-(a/b)*(n2->second);//y'
        n1->third=n2->third;//d
        return n1;
    }

}

int main()
{

    struct _node *n;
    int u,v;
    // do some more initialization.

        printf("\n\n Type two positive integers -> ");
        scanf("%d %d", &u, &v);

           // if (u < 0  ||  v < 0)// if inputs are invalid, then do nothing.
              //  continue;
           // if (u == 0  ||  v == 0)// if one of inputs are 0, then terminate
             //   break;

            n = extended_Euclid(u, v);

        printf("x is %d, y is %d, and c is %d\n ", n->first, n->second, n->third);


    return 0;
}
