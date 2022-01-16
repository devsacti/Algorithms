/*
https://cocoon1787.tistory.com/38

*/
package test;

import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        // 2차원 '배열(array)' 방식 입력
        int cnt_row=3;
        int cnt_column=4;
        int[][] matrix = new int[cnt_row][cnt_column];

        for (int r=0;r<cnt_row;r++){
            for (int c=0;c<cnt_column;c++){
                matrix[r][c]=sc.nextInt();
            }
        }

        // 2차원 '배열(array)' 방식 출력
        System.out.println();
        for (int r=0;r<cnt_row;r++){
            for (int c=0;c<cnt_column;c++){
                System.out.printf("%d ",matrix[r][c]);
            }
            System.out.println();
        }
    }
}