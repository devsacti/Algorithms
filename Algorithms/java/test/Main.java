/*
https://cocoon1787.tistory.com/38

*/
package test;

import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int i=sc.nextInt();

        int constant = i;
        // constant = i + j 
        // => constant - j = i
        int j = 0; //차감하는 수

        for(int cnt_case=0;cnt_case<constant;cnt_case++){
            int current=constant-j;
            System.out.println(current);
            // 차감하는 변수 j
            j++;
        }

    }
}