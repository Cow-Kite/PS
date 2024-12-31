import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            if(num != 0){
                q.offer(num);
            } else {
                if(q.isEmpty()){
                    bw.write(String.valueOf(0) + "\n");
                } else {
                    bw.write(String.valueOf(q.poll()) + "\n");
                }
            }
        }
        bw.flush();
    }
}
