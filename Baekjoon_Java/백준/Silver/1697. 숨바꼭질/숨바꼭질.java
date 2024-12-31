import java.util.*;
import java.io.*;

public class Main{
    static int N, K;
    static int count;
    static boolean [] visited;
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        count = 0;
        visited = new boolean[100001];
        bfs(N);
    }
    public static void bfs(int start){
        visited[start] = true;
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        while(!q.isEmpty()){
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int now = q.poll();
                visited[now] = true;
                if(now == K){
                    System.out.println(count);
                    return;
                }
                if(now-1 >=0 && !visited[now-1]){
                    visited[now-1] = true;
                    q.offer(now-1);
                }
                if(now+1 < 100001 && !visited[now+1]){
                    visited[now+1] = true;
                    q.offer(now+1);
                }
                if(now*2 < 100001 && !visited[now*2]){
                    visited[now*2] = true;
                    q.offer(now*2);
                }
            }
            count++;
        }
    }
}