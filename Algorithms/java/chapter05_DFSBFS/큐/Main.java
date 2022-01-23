import java.util.*;
/*

<python>
from collections import deque
q=deque()
q.append, q.popleft

<java>
import java.util.*;
Queue<Integer> q = new LinkedList<>();
q.offer,q.poll

왜 poll일까? 왠지 투표함을 까보는 느낌이 아닐까함. 그래서 맨 위 표를 개표하는 느낌
*/
public class Main {

    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();

        // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
        q.offer(5);
        q.offer(2);
        q.offer(3);
        q.offer(7);
        q.poll();
        q.offer(1);
        q.offer(4);
        q.poll();
        // 먼저 들어온 원소부터 추출
        while (!q.isEmpty()) {
            System.out.println(q.poll());
        }
    }

}