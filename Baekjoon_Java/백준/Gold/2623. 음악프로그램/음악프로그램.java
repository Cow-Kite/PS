import java.util.*;
import java.io.*;

public class Main {
    static int N, M; //가수의 수, 보조 PD의 수
    static ArrayList<Integer> singer [];
    static int edgeCount [];
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        singer = new ArrayList[N+1];
        edgeCount = new int[N+1];
        for (int i = 0; i < N+1; i++) {
            singer[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken()); 
            for (int j = 0; j < num-1; j++) {
                int m = Integer.parseInt(st.nextToken()); 
                singer[n].add(m); 
                edgeCount[m]++; 
                n = m; 
            }
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = N; i > 0 ; i--) {
            if(edgeCount[i]==0)
                q.offer(i);
        }
        while(!q.isEmpty()){
            int sing = q.poll();
            bw.write(String.valueOf(sing) + "\n");
            for(int i : singer[sing]){
                edgeCount[i]--;
                if(edgeCount[i]==0)
                    q.offer(i);
            }
        }

        for (int i = 1; i < N+1; i++) {
            if(edgeCount[i]!=0){
                System.out.println(0);
                return;
            }
        }
        bw.flush();
    }
}