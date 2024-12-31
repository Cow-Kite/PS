import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static ArrayList<Integer> human[];
    static int [] edgeCount;
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        human = new ArrayList[N+1];
        edgeCount = new int[N+1];
        for (int i = 0; i < N+1; i++) {
            human[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            human[A].add(B);
            edgeCount[B]++;
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i < N+1; i++) {
            if(edgeCount[i] == 0){
                q.offer(i);
            }
        }
        while(!q.isEmpty()){
            int n = q.poll();
            bw.write(String.valueOf(n) + " ");
            for(int i : human[n]){
                edgeCount[i]--;
                if(edgeCount[i] == 0)
                    q.offer(i);
            }
        }
        bw.flush();
    }
}