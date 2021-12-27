#include <string.h>
#include <stdio.h>

static int distance (char * word1, int len1,char * word2,int len2)
{
    //1행(또는 1열) 추가
    int matrix[len1 + 1][len2 + 1];
    int i;

    //문자열 행렬에 업데이트
    for (i = 0; i <= len1; i++)
    {
        matrix[i][0] = i;
    }

    for (i = 0; i <= len2; i++)
    {
        matrix[0][i] = i;
    }

    //계산
    for (i = 1; i <= len1; i++)
    {
        int j;
        char c1;

        c1 = word1[i-1];
        for (j = 1; j <= len2; j++)
        {
            char c2;

            c2 = word2[j-1];

            if (c1 == c2)
            {
                matrix[i][j] = matrix[i-1][j-1];
            }
            else
            {
                int cnt_delete;
                int cnt_insert;
                int cnt_substitute;
                int minimum;

                cnt_delete = matrix[i-1][j] + 1;
                cnt_insert = matrix[i][j-1] + 1;
                cnt_substitute = matrix[i-1][j-1] + 1;
                minimum = cnt_delete;
                if (cnt_insert < minimum) {
                    minimum = cnt_insert;
                }
                if (cnt_substitute < minimum) {
                    minimum = cnt_substitute;
                }
                matrix[i][j] = minimum;
            }
        }
    }
    return matrix[len1][len2];
}

int main ()
{
    char* word1;
    char* word2;
    int len1;
    int len2;
    int d;

    word1 = "snow";
    word2 = "sunny";

    printf("입력 %s %s\n", word1, word2);


    len1 = strlen (word1);
    len2 = strlen (word2);
    d = distance (word1, len1, word2, len2);
    printf ("%d\n", d);

    return 0;
}
