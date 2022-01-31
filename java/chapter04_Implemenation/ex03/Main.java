/*
ex03 : 왕실의 나이트

example In-Out
a1
=>
2

* 체스판에 대해서 미국은 열에 대해서는 abcd...로 인덱싱, 행에 대해서는 1,2,3,4,...로 인덱싱한다.
이에 따라서 인풋값은 체스판 기준, 열값과 행값이 전달받은 것으로 접근가능하다.

*/
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 현재 나이트의 위치 입력받기
        String inputData = sc.nextLine();
        int row = inputData.charAt(1) - '0';
        int column = inputData.charAt(0) - 'a' + 1;
        
        int experi_row=(int)inputData.charAt(1);
        
        // '1'의 본질은 (아스키코드기준) 이진수이고_0110001, 이를 10진수 int화 하면 49
        System.out.printf("%d %d", row,experi_row);
        System.out.println();

        // 나이트가 이동할 수 있는 8가지 방향 정의
        int[] dx = {-2, -1, 1, 2, 2, 1, -1, -2};
        int[] dy = {-1, -2, -2, -1, 1, 2, 2, 1};

        // 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
        int result = 0;
        for (int i = 0; i < 8; i++) {
            // 이동하고자 하는 위치 확인
            int nextRow = row + dx[i];
            int nextColumn = column + dy[i];
            // 해당 위치로 이동이 가능하다면 카운트 증가
            if (nextRow >= 1 && nextRow <= 8 && nextColumn >= 1 && nextColumn <= 8) {
                result += 1;
            }
        }

        System.out.println(result);
    }

}
