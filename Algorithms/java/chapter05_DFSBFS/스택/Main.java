import java.util.*;

/*
<python>
(no import)
stack=[]
append, pop
<java>
import java.util.*;
Stack<Integer> s = new Stack<>();
push, pop

*/

public class Main {

    public static void main(String[] args) {
        // AS-IS, python
        // stack=[]
        // TO-BE
        Stack<Integer> s = new Stack<>();

        // AS-IS, python
        // stack.append(5)
        // stack.append(2)
        // stack.append(3)
        // stack.append(7)
        // stack.pop()
        // stack.append(1)
        // stack.append(4)
        // stack.pop()

        // TO-BE
        // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
        s.push(5);
        s.push(2);
        s.push(3);
        s.push(7);
        s.pop();
        s.push(1);
        s.push(4);
        s.pop();
        // 스택의 최상단 원소부터 출력
        while (!s.empty()) {
            System.out.println(s.peek());
            s.pop();
        }
    }

}