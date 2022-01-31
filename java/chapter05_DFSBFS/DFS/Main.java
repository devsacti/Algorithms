/*

Depth-First Search example refactoring

example In-Out

8 18
1 2
1 3
1 8
2 1
2 7
3 1
3 4
3 5
4 3
4 5
5 3
5 4
6 7
7 2
7 6
7 8
8 1
8 7
-
1 [2, 3, 8]
2 [1, 7]
3 [1, 4, 5]
4 [3, 5]
5 [3, 4]
6 [7]
7 [2, 6, 8]
8 [1, 7]
1 2 7 6 8 3 4 5

*/

import java.util.*;

public class Main {

    public static boolean[] visited = new boolean[9];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

    // DFS 함수 정의
    public static void dfs(int x) {
        // 현재 노드를 방문 처리
        visited[x] = true;
        System.out.print(x + " ");
        // 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for (int i = 0; i < graph.get(x).size(); i++) {
            int y = graph.get(x).get(i);
            if (!visited[y]) dfs(y);
        }
    }

    // refactoring part
    public static int[] visitedRE = new int[9];
    // python에서는 애당초 리턴값이 리스트로서 전달되는 동시에 자료형이 설정되는 경우가 많고,
    // 나아가, 리스트 자체는 애당초 자료형 구분없이 받을 수 있도록 설계 및 지원되었다고 이해가능, 가령, li_python = [True,False, 1, 1.2, "who am i"]
    // 그래서 List 안에 또 구태여? List를 설정하는 것이 낯설 수 있지만, 보다 엄밀한 정의방식으로 우선 납득
    public static ArrayList<ArrayList<Integer>> graphRE = new ArrayList<ArrayList<Integer>>();

    // DFS 함수 리팩토링
    public static void dfsRE(int x) {
        // System.out.println(Arrays.toString(visitedRE));
        // 현재 노드를 방문 처리
        visitedRE[x] = 1;
        System.out.print(x + " ");
        // 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for (int i = 0; i < graphRE.get(x).size(); i++) {
            int y = graphRE.get(x).get(i);
            if (visitedRE[y]==0) dfsRE(y);
        }
    }

    public static void main(String[] args) {
        // python에서 유사한 대응케이스를 찾자면 graph=defaultdict(list)이 있고,
        // graph[key1]=[True,False, 1, 1.2, "who am i"] 에서 자동으로 key,일종의 인덱스,가 설정되고, 그 value는 입력된 리스트로 정의된다.
        // 이런 점에서 왜 아무것도 안들어있는 객체를 graphRE 리스트에 집어넣는지 이해가 안됬고,

        // 또한 String[][] arr_String = new String[10][10]; 에서는 굳이 String temp = null;
        // 을 미리 할당하는 짓거리는 하지 않기에 유달리 아래와같은 초기화 과정이 와닿지 않았다.
        // 그러나, 애당초 Array 와 List라는 서로 다른 개념과 방식을 비교하는 것이 잘못된 것이었고, 특히나 python에서는 List만 존재하기 때문에 이런 혼란이 더욱 가중되었다.

        // Array vs List
        // Array는 선언 시, 길이를 반드시 지정해야되서 인덱스가 특정가능하나, List는 그러한 Array의 한계를 보완하고자 나왔고, 먼저 item이 들어간 다음에 인덱스가 생성된다.
        // 그렇기 때문에 리스트는 기본적으로 무언갈 넣어줘야 인덱스를 통해 호출가능하다!!
        // 참고로, defaultdict는 이러한 패턴_무언갈 넣은 다음, 인덱스가 생김_을 보완하고자 다른 개념을 활용해서, 여전히 길이에 기반한 인덱스는 못만들지만 key를 통해 우회했다고 이해가능

        // 그래프 초기화, 사용할 만큼의 item을 넣어서 숫자 인덱스로 호출하자!
        for (int i = 0; i < 9; i++) {
            graph.add(new ArrayList<Integer>());
        }

        // 노드 1에 연결된 노드 정보 저장 
        graph.get(1).add(2);
        graph.get(1).add(3);
        graph.get(1).add(8);
        
        // 노드 2에 연결된 노드 정보 저장 
        graph.get(2).add(1);
        graph.get(2).add(7);
        
        // 노드 3에 연결된 노드 정보 저장 
        graph.get(3).add(1);
        graph.get(3).add(4);
        graph.get(3).add(5);
        
        // 노드 4에 연결된 노드 정보 저장 
        graph.get(4).add(3);
        graph.get(4).add(5);
        
        // 노드 5에 연결된 노드 정보 저장 
        graph.get(5).add(3);
        graph.get(5).add(4);
        
        // 노드 6에 연결된 노드 정보 저장 
        graph.get(6).add(7);
        
        // 노드 7에 연결된 노드 정보 저장 
        graph.get(7).add(2);
        graph.get(7).add(6);
        graph.get(7).add(8);
        
        // 노드 8에 연결된 노드 정보 저장 
        graph.get(8).add(1);
        graph.get(8).add(7);

        for(int i=1;i<graph.size();i++){
            System.out.print(i+" ");
            System.out.print(graph.get(i)+"\n");
        }

        dfs(1);

        System.out.println();
        System.out.println("now is the part of REfactoring, Input the Example In-Out");

        Scanner sc = new Scanner(System.in);

        int n=sc.nextInt();
        int cntEdge=sc.nextInt();

        // 1 based indexing 을 위해 1개 더 추가
        for (int i = 0; i < n+1; i++) {
            graphRE.add(new ArrayList<Integer>());
        }

        for (int i = 1; i < cntEdge+1; i++) {
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();
            graphRE.get(v1).add(v2);
        }

        for(int i=1;i<graphRE.size();i++){
            System.out.print(i+" ");
            System.out.print(graphRE.get(i)+"\n");
        }

        dfsRE(1);

    }

}