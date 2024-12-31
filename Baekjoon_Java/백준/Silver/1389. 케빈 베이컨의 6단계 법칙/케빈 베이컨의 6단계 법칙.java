import java.util.*;
import java.io.*;

public class Main{
    static int N, M;
    static boolean [][] friend;
    static boolean [] visited;
    static int count;
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        friend = new boolean [N+1][N+1];
        M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            friend[start][end] = true;
            friend[end][start] = true;
        }
        int [] answer = new int[N+1];
        for(int i=1; i<=N; i++){
            int sum = 0;
            for(int j=1; j<=N; j++){
                visited = new boolean[N+1];
                if(i == j) {
                    continue;
                }
                int num = bfs(i, j);
                sum += num;
            }
            answer[i] = sum;
        }
        int min = answer[1];
        int index = 1;
        for(int i=2; i<=N; i++){
            if(min > answer[i]) {
                min = answer[i];
                index = i;
            }
        }
        System.out.println(index);
    }
    public static int bfs(int human, int find){
        Queue<Integer> q = new LinkedList<>();
        q.offer(human);
        visited[human] = true;
        count = 0;
        while(!q.isEmpty()){
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int now = q.poll();
                if(now == find){
                    return count;
                }
                for (int j = 1; j <= N; j++) {
                    if(friend[now][j] && !visited[j]){
                        visited[j] = true;
                        q.offer(j);
                    }
                }
            }
            count++;
        }
        return -1;
    }
}