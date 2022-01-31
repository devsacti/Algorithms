/*
ex02 : 동빈이의 큰 수의 법칙

example In&Out

5 8 3
2 4 5 4 6
=>
46

*/


import java.util.*; 
// Scanner, Arrays

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // N, M, K를 공백, 스페이스랑 엔터 모두 해당, 을 기준으로 구분하여 입력 받기
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        sc.close();
        // N개의 수를 공백을 기준으로 구분하여 입력 받기
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr); // 입력 받은 수들 정렬하기
        int first = arr[n - 1]; // 가장 큰 수
        int second = arr[n - 2]; // 두 번째로 큰 수

        // 최대치에 도달하는 최고의 시나리오는 (가장 큰 수 * k 번 그리고 두번째로 큰수 * 1번)이 최대한 많이 반복되야하고,
        // 나머지 짜투리도 이 최대단위로 접근해야한다.
        // 가장 큰 수가 더해지는 횟수 계산
        // below 'Unit' is best Unit that can make maximum
        int lenUnit = (k + 1);
        int cntUnit = (m / lenUnit);
        int cntK = cntUnit*k;

        // 마지막 rest에서도 max가 k개 그리고 second 최대가 1개 반복된다는 전제하에 접근한다면
        // 나머지 갯수는 언제난 max 값이 반복될 것이다.
        // 참고로, m이 lenUnit의 배수라면, rest에서의 k 갯수는 상단 에서 모두 카운팅되고 아래선 0이된다.
        cntK += m % (k + 1);

        int result = 0;
        result += cntK * first; // 가장 큰 수 더하기
        result += (m - cntK) * second; // 두 번째로 큰 수 더하기

        System.out.println(result);
    }

}
