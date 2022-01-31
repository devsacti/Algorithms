import java.util.*;

/*

exampleIn-Out
4 5
00110
00011
11111
00000
-
3

*/

public class Main {

    public static int n, m;
    public static int[][] graph = new int[1000][1000];

    // DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
    public static boolean dfs(int x, int y) {
        // 주어진 범위를 벗어나는 경우에는 즉시 종료
        if (x <= -1 || x >=n || y <= -1 || y >= m) {
            return false;
        }
        // 현재 노드를 아직 방문하지 않았다면
        if (graph[x][y] == 0) {
            // 해당 노드 방문 처리
            graph[x][y] = 1;
            // 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
            dfs(x - 1, y);
            dfs(x, y - 1);
            dfs(x + 1, y);
            dfs(x, y + 1);
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // N, M을 공백을 기준으로 구분하여 입력 받기
        // 입력값이 2차원이든 3차원 그 이상으로 내눈에 보여도, 
        // 컴퓨터는 1줄짜리 버퍼론 입력되고,중간에 별다른 처리가없다면, 1줄로 출력된다고 이해할 수 있다.
        // 이런 점에서 nextInt()는 버퍼에서 \n 전까지 변수를 저장한다. 그리고 \n은 여전히 버퍼에 남아있는데,
        
        // 이번 인풋값에서 1행이 띄어쓰기나 엔터 없이 입력되는 상황이라, nextInt로는 부족
        // 1줄 단위로 처리할것인데 이때, 버퍼안에 nextInt 이후 \n을 제거해야한다.
        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine(); // 버퍼 지우기

        // 2차원 리스트의 맵 정보 입력 받기
        for (int i = 0; i < n; i++) {
            String str = sc.nextLine();// 1줄 단위로 String
            for (int j = 0; j < m; j++) {
                // 파이썬이라면 기승전 리스트였겠지만
                // 자바는 리스트 아니고, 배열아니고, '문자열' 그래서 인덱스로 접근
                graph[i][j] = str.charAt(j) - '0';
            }
        }

        // 모든 노드(위치)에 대하여 음료수 채우기
        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // 현재 위치에서 DFS 수행
                if (dfs(i, j)) {
                    result += 1;
                }
            }
        }
        System.out.println(result); // 정답 출력 
    }

}