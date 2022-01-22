import java.util.*;
/*

팩토리얼과 재귀구조, 그리고 백트래킹

*/
public class Main {

    // 반복적으로 구현한 n!
    public static int factorialIterative(int n) {
        int result = 1;
        // 1부터 n까지의 수를 차례대로 곱하기
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    // 재귀적으로 구현한 n!
    public static int factorialRecursive(int n) {
        // n이 1 이하인 경우 1을 반환
        if (n <= 1) return 1;
        // n! = n * (n - 1)!를 그대로 코드로 작성하기
        return n * factorialRecursive(n - 1);
    }

    // Recursive and Backtracking
    // 당연히 비효율적이지만 Recursive 구조에서 응용가능한 부분을 체크한다.

    public static int factorialRecursiveAndBacktracking(int i){
        return 0;
    }

    public static void main(String[] args) {
        // 각각의 방식으로 구현한 n! 출력(n = 5)
        System.out.println("반복적으로 구현:" + factorialIterative(5));
        System.out.println("재귀적으로 구현:" + factorialRecursive(5));
        System.out.println("재귀+백트래킹으로 구현:" + factorialRecursive(5));
    }

}