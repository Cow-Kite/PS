import java.util.*;
import java.io.*;

public class Main {
    static int N, M; //문제 수, 문제 정보 수
    static ArrayList<Integer> problem [];
    static int [] count;
    static boolean [] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        problem = new ArrayList[N+1];
        count = new int[N+1];
        visited = new boolean [N+1];
        for (int i = 0; i < N+1; i++) {
            problem[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            problem[a].add(b);
            count[b]++;
        }

        PriorityQueue<Integer> q = new PriorityQueue<>();
        for (int i = 1; i < N+1; i++) {
            if(count[i]==0){
                q.offer(i);
            }
        }

        while(!q.isEmpty()){
            int n = q.poll();
            bw.write(String.valueOf(n) + " ");
            for(int i : problem[n]){
                count[i]--;
                if(count[i]==0)
                    q.offer(i);
            }
        }
        bw.flush();
    }
}