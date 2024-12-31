import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int sum;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            int card = Integer.parseInt(br.readLine());
            q.offer(card);
        }
        while(q.size() >= 2){
            int n1 = q.poll();
            int n2 = q.poll();
            int hap = n1 + n2;
            sum += hap;
            q.offer(hap);
        }
        bw.write(String.valueOf(sum));
        bw.flush();
    }
}