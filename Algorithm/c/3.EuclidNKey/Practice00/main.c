#include <stdio.h>
#include <string.h>

int XOR(unsigned int c, unsigned int key)
{
    return c^key;
}

int* encryption(char m[])
{
    int key=5;
    int len=strlen(m);
    static char enc[100];


    int i=0;
    for(i=0;i<len;i++)
    {
        char ch=m[i];
        unsigned int c=(unsigned int)ch;
        enc[i]=XOR(c,key);

    }
    //printf("%s\n", enc);
    return enc;

}

int* decryption(char enc_msg[])
{
    int key=5;
    int len=strlen(enc_msg);
    static char m[100];

    int i=0;
    for(i=0;i<len;i++)
    {
        char ch=enc_msg[i];
        unsigned int c=(unsigned int)ch;
        m[i]=XOR(c,key);

    }
    //printf("%s\n", enc);
    return m;
}


int main()
{
    char msg[]="Hello, I love Dongguk. Please love KJHKJHKJH!!!";
    //printf("%d ",strlen(msg));
    char enc_msg[strlen(msg)];
    char dec_msg[strlen(msg)];


    printf("encrypted message : ");
    //int* p=encryption(msg);
    strcpy(enc_msg,encryption(msg));
    printf("%s\n", enc_msg);

    int i=0;
    for(i=0;i<strlen(enc_msg);i++)
    {
        printf("%d ", enc_msg[i]);
    }
    printf("\n");


    printf("decrypted message : ");
    //int* p=encryption(msg);
    strcpy(dec_msg,decryption(enc_msg));
    printf("%s\n", dec_msg);

    for(i=0;i<strlen(dec_msg);i++)
    {
        printf("%d ", dec_msg[i]);
    }

    return 0;
}
