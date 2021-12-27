#include <stdio.h>
#include <stdlib.h>
#define TABLE_SIZE 541
#define NAME_SIZE 20

int hash1_collision=0;
int hash2_collision=0;

struct hash {
    char names[NAME_SIZE]; // store inserted data
    unsigned short collision; // check collision for the data
};
struct hash hash_table[TABLE_SIZE];

int hash1(char str[]){
    int i,h;
    for(i=0,h=0; i < strlen(str); i++){
        h = ((int)str[i] + h)%TABLE_SIZE;
    }
    return h;
}

int hash_insert(char name[]){ // �ؽ� ���̺� �����͸� �����ϴ� �Լ�
    int number = 0; // for collision
    int key = hash1(name); // hash1 �Լ��� �����Ͽ� �ؽ� ���� ��´�.
    // int hey = hash2(dat); // hash2 �Լ��� �����Ͽ� �ؽ� ���� ��´�.

    while (strcmp(hash_table[key].names, "") != 0) // collision�� �߻��� ���
    {
        hash_table[key].collision++; // �ش� ���Կ� collision�� �߻����� ���.
        number++; // ���� collision �� �߻��� Ƚ��
        hash1_collision++;
        key = (number + key)%TABLE_SIZE;// linear probing�� �����Ͽ� collision�� ���� ������ ã��.
    }
    // key ���� �浹�� ���� ��� �����͸� �ؽ� ���̺� ������.
    strcpy(hash_table[key].names, name);
    return key;
}
int hash2(char str[]){
    int i,h;

    for(i=0,h=0; i < strlen(str); i++)
    {
        h = (str[i] + h*h)%TABLE_SIZE;
    }
    return h;
}

int hash_insert2(char name[]){ // �ؽ� ���̺� �����͸� �����ϴ� �Լ�
    int number = 0; // for collision
    int key = hash2(name); // hash2 �Լ��� �����Ͽ� �ؽ� ���� ��´�.

    while (strcmp(hash_table[key].names, "") != 0) // collision�� �߻��� ���
    {
        hash_table[key].collision++; // �ش� ���Կ� collision�� �߻����� ���.
        number++; // ���� collision �� �߻��� Ƚ��
        hash2_collision++;
        key = (number + key)%TABLE_SIZE;// linear probing�� �����Ͽ� collision�� ���� ������ ã��.
    }
    // key ���� �浹�� ���� ��� �����͸� �ؽ� ���̺� ������.
    strcpy(hash_table[key].names, name);
    return key;
}

void initialize_table() { // �ؽ� ���̺��� �ʱ�ȭ�Ѵ�.
    int i;

    for (i = 0; i < TABLE_SIZE; i++) {
        strcpy(hash_table[i].names,"");
        hash_table[i].collision = 0;
    }
}

void main(){
    initialize_table();
    int i=0;
    char name[TABLE_SIZE];
    FILE *fp1, *fp2;
    fp1 = fopen("names.txt", "r");
    fp2 = fopen("names.txt", "r");
/*
    while(fscanf(fp1, "%s", name) != EOF)
    {
        hash_insert(name);
        i++;
    }
    printf("Using Hash1 \n");

    for(i=0; i<TABLE_SIZE; i++)
    {
        if(strcmp(hash_table[i].names, "")==0)
        {
            strcpy(hash_table[i].names, "EMPTY");
        }
        printf("table[%d] : %s\t %d\n" , i, hash_table[i].names, hash_table[i].collision);
    }

    initialize_table();
    while(fscanf(fp2, "%s", name) != EOF)
    {
        hash_insert2(name);
        i++;
    }

    printf("Using Hash2 \n");
    for(i=0; i<TABLE_SIZE; i++)
    {
        if(strcmp(hash_table[i].names, "")==0)
        {
            strcpy(hash_table[i].names, "EMPTY");
        }
        printf("table[%d] : %s\t %d\n" , i, hash_table[i].names, hash_table[i].collision);
    }
        printf("Total collision number in Hash1 is %d\n",hash1_collision);
        printf("Total collision number in Hash2 is %d\n",hash2_collision);

    */


}
