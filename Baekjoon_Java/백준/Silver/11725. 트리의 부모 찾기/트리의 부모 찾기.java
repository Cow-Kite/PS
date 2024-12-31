import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static ArrayList<Integer> list [];
    static boolean [] visited;
    static int [] ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());

        list = new ArrayList[N+1];
        visited = new boolean[N+1];
        ans = new int[N+1];
        for (int i = 1; i < N+1; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < N-1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            list[A].add(B);
            list[B].add(A);
        }

        Queue<Integer> q = new LinkedList<>();
        q.offer(1);
        visited[1] = true;
        while(!q.isEmpty()){
            int parent = q.poll();
            for(int child : list[parent]){
                if(!visited[child]){
                    ans[child] = parent;
                    visited[child] = true;
                    q.offer(child);
                }
            }
        }

        for (int i=2; i<N+1; i++){
            bw.write(String.valueOf(ans[i] + "\n"));
        }

        bw.flush();
        bw.close();
    }
}