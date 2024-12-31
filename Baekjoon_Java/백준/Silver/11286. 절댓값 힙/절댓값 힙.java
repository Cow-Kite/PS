import java.util.*;
import java.io.*;

public class Main {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> q = new PriorityQueue<>(((o1, o2) -> {
            int num1 = Math.abs(o1);
            int num2 = Math.abs(o2);
            if(num1 == num2)
                return o1 - o2;
            return num1 - num2;
        }));
        for (int i = 0; i < N; i++) {
            int n = Integer.parseInt(br.readLine());
            if(n==0){
                if(q.isEmpty()) bw.write(String.valueOf(0) + "\n");
                else {
                    bw.write(String.valueOf(q.poll()) + "\n");
                }
            } else {
                q.offer(n);
            }
        }
        bw.flush();
    }
}