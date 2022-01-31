/*
ex01 : 상하좌우

example In&Out
5
R R R U D D
=>
3 4

learned
java programming language => java.lang ; Math

*/

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // N을 입력받고, 현재 사용중인 버퍼의 개행문자를 마저 받아서 던짐으로서 버퍼 비우기
        // 관련 링크 ; https://allg.tistory.com/17
        // 버퍼란 일단 경험적으로 나의 키보드 입력 값들을 중간에 모아서 현재 실행중인 java 파일에 인풋으로서 전달해주는 중간매개체 혹은 무언가로 일단 수용
        int n = sc.nextInt(); // 메커니즘인 버퍼 내에서 개행문자(' ' 이나 '\n') '전'까지 인풋으로 취급
        sc.nextLine(); // nextLine 메커니즘 상 버퍼 내에서 개행문자(' ' 이나 '\n') '까지' 인풋으로 취급
        // 결과적으로 바로 윗 행과 지금행까지해서 버퍼의 ????\n이 현재 Main java파일에 전달된다고 이해
        // 명령어 입력받기
        String[] plans = sc.nextLine().split(" ");
        int x = 1, y = 1;

        System.out.println(n);
        System.out.println(plans);
        System.out.println(Arrays.toString(plans));

        // L, R, U, D에 따른 이동 방향 
        char[] moveTypes = {'L', 'R', 'U', 'D'};
        
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        
        // 이동 계획을 하나씩 확인
        for (int i = 0; i < plans.length; i++) {
            char plan = plans[i].charAt(0);
            // 이동 후 좌표 구하기 
            int nx = -1, ny = -1;
            for (int j = 0; j < 4; j++) {
                if (plan == moveTypes[j]) {
                    nx = x + dx[j];
                    ny = y + dy[j];
                }
            }
            // 공간을 벗어나는 경우 무시 
            if (nx < 1 || ny < 1 || nx > n || ny > n) continue;
            // 이동 수행 
            x = nx;
            y = ny;
        }

        System.out.println(x + " " + y);
    }

}