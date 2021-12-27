#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MESSAGE_LENGTH 38

char message[]={"Hello Dongguk.My name is JeongHyu Kim"};//printf("%d ",strlen(message));
unsigned int encryption[MESSAGE_LENGTH];
char decryption[MESSAGE_LENGTH];

//a*x+b*y=gcd(a,b) is background, a=(p-1)(q-1), b=3
struct _node
{
    int first;//x
    int second;//y
    int third;//gcd=1 로 임의 설정될 예정.
};

struct _node* extended_Euclid(int a, int b);
unsigned int do_exp(int c, int key, int N);//public key=3,private key=107, N=p*q로 주어짐.
unsigned int do_exp2(unsigned int c, int key, int N);//public key=3,private key=107, N=p*q로 주어짐.

void encryption_msg(char m[], int public_key,int N);
void decryption_msg(unsigned int m[], int private_key,int N);

void print_ASKII_value(char e[]);
void print_encryption(unsigned int e[]);
void print_decryption(char e[]);


int main()
{
    printf("Input message[%d] : %s\n\n",strlen(message),message);
    print_ASKII_value(message);
    printf("\n");

    int p=11, q=17;
    int N=p*q;//N=187
    int e=3;//public key 'e'
    int d;//private key
    struct _node* n;

    n = extended_Euclid((p-1)*(q-1), e);

    while(n->second<0)
    {
        n->second+=(p-1)*(q-1);// p, q, e에서 파생된 공식이지만 정리하면 Eu((p-1)(q-1),e)를 푸는 과정이고 이는 한편 Eu(e,(p-1)(q-1)) 므로 1=ed mod (p-1)(q-1)를 푸는 과정이다.
    }

    printf("About ((p-1)*(q-1)*x) + (e*d)=1,\n x is %d, d is %d, and c is %d\n\n", n->first, n->second, n->third);

    d=n->second;

    encryption_msg(message,e,N);
    print_encryption(encryption);
    printf("\n");

    decryption_msg(encryption,d,N);
    printf("\n\n");

    printf("decypted : ");
    print_decryption(decryption);

    return 0;
}


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

unsigned int do_exp(int c, int key, int N)//c means character, key means public or private, N=pq
{
	// do_exp()는 ckey mod N 해준 값을 리턴한다.
	// 단 c를 key 번 곱하게 되면 그 값이 정수형으로 감당할 수 없을 정도로 커지므로
	// c를 곱해줄 때 마다 mod 연산 (%연산)을 구행하여 그 값을 충분히 작은 값으로
    // 유지시킬 필요가 있다. 물론 수업시간에 배운 내용을 적용하여 ckey mod N 을 구할
    // 수도 있다.
    unsigned int prod=1;

    int i=0;
    for(i=0;i<key;i++)
    {
        prod=(prod*c)%N;
    }

	return prod;		// ckey mod N을 리턴
}

unsigned int do_exp2(unsigned int c, int key, int N)//c means character, key means public or private, N=pq
{
	// do_exp()는 ckey mod N 해준 값을 리턴한다.
	// 단 c를 key 번 곱하게 되면 그 값이 정수형으로 감당할 수 없을 정도로 커지므로
	// c를 곱해줄 때 마다 mod 연산 (%연산)을 구행하여 그 값을 충분히 작은 값으로
    // 유지시킬 필요가 있다. 물론 수업시간에 배운 내용을 적용하여 ckey mod N 을 구할
    // 수도 있다.
    unsigned int prod=1;

    int i=0;
    for(i=0;i<key;i++)
    {
        prod=(prod*c)%N;
    }

	return prod;		// ckey mod N을 리턴
}

void encryption_msg(char m[], int public_key,int N)// (e,N)=(3,187)
{

    int i=0;
    for(i=0;i<MESSAGE_LENGTH;i++)
    {
        char ch=m[i];
        unsigned int c=(unsigned int)ch;
        encryption[i]=do_exp(c,public_key,N);

    }
    //printf("%s\n", encryption);

}

void decryption_msg(unsigned int m[], int private_key,int N)
{
    int i=0;
    for(i=0;i<MESSAGE_LENGTH;i++)
    {
        //char ch=m[i];
        unsigned int c=m[i];//printf("%d ",c);
        decryption[i]=do_exp2(c,private_key,N);
        printf("%d ", decryption[i]);
    }
    //printf("%s\n", decryption);
}

void print_encryption(unsigned int e[]) {
	for (int i = 0; i < MESSAGE_LENGTH; i++)
		printf("%d ", e[i]);
	printf("\n");
}

void print_ASKII_value(char e[]) {
	for (int i = 0; i < MESSAGE_LENGTH; i++)
		printf("%d ", e[i]);
	printf("\n");
}

void print_decryption(char e[]) {
	for (int i = 0; i < MESSAGE_LENGTH; i++)
		printf("%c", e[i]);
	printf("\n");
}
