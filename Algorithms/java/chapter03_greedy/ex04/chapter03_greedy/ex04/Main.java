/*
ex04 : 1이 될때까지
*/
package chapter03_greedy.ex04;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // N, K를 공백을 기준으로 구분하여 입력 받기
        int n = sc.nextInt();
        int k = sc.nextInt();
        int result = 0;

        // 아래 while에서는 최대한 나눌 수 있을때까지 다듬거나 나누는 과정이다.
        while (true) {
            // N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
            // target이란 N이 K의 배수가 되어 가장 빨리 1에 될수있도록 해주는 워너비 중간값들이라고 볼 수 있다.
            // 가령, n 이 23, k가 7 이면 target은 21, 그리고 나눗셈 후 다음 n1은 3
            int target = (n / k) * k;
            result += (n - target);
            n = target;
            // N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
            if (n < k) break;
            // K로 나누기
            result += 1;
            n /= k;
        }

        // 마지막으로 1이 되도록 n에서 1을 (n-1)번 뺀다는 가정에 대한 처리이다.
        result += (n - 1);
        System.out.println(result);
    }

}