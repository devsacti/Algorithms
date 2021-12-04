// 거스름돈 문제
public class Main {

    public static void main(String[] args) {
        int n = 1260;
        int cnt = 0;
        int[] coinTypes = {500, 100, 50, 10};
		
        int limit = coinTypes.length;

        for (int i = 0; i < limit; i++) {
            int coin = coinTypes[i];
            cnt += n / coin;
            n %= coin;
        }

        System.out.println(cnt);
    }

}