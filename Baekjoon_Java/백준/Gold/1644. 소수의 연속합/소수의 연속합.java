import java.util.*;
import java.io.*;

public class Main {
    static int N, count;
    static boolean [] prime;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        //소수 구하기
        prime = new boolean[N+1];
        prime[0] = prime[1] = true;

        for (int i = 2; i*i < N+1; i++) {
            if(!prime[i]){
                for (int j = i*i; j < N+1; j+=i) {
                    prime[j] = true;
                }
            }
        }

        //소수 배열 만들기
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            if(!prime[i]) list.add(i);
        }

        //소수의 연속합
        int hap = 0;
        int start = 0;
        int end = 0;
        while(true){
            if(hap >= N){
                hap -= list.get(start++);
            } else if(end == list.size()) break;
            else {
                hap += list.get(end++);
            }
            if(hap == N) count++;
        }

        System.out.println(count);
    }
}