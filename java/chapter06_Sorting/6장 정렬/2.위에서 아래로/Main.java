/*
example InOut

3
15
27
12
--
27 15 12

*/
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // N을 입력받기
        int n = sc.nextInt();

        // N개의 정수를 입력받아 리스트에 저장
        Integer[] arr = new Integer[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // 기본 정렬 라이브러리를 이용하여 내림차순 정렬 수행
        // 파이썬은 리스트 객체 자체에 정렬 기능이 탑재되어있다고 볼 수 있다.
        // arr.sort(reverse=True)
        // 하지만 java는 외부의 도움을 받아야하기에 어딘가로 던져져야 한다고 이해할 수 있다.
        Arrays.sort(arr, Collections.reverseOrder());

        for(int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }

}