import java.io.*;
import java.util.*;
public class Main {
    static int [][] arr;
    static boolean visited [];
    static int N;
    static int M;
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken()); // 정점의 개수
        M = Integer.parseInt(st.nextToken()); // 간선의 개수
        arr = new int [N+1][N+1];
        visited = new boolean[N+1];
        count = 0;
        for(int i=1; i<M+1; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr[x][y] = 1;
            arr[y][x] = 1;
        }

        for(int i=1; i<N+1; i++){
            if(visited[i]) continue;
            count++;
            bfs(i);
        }

        System.out.println(count);
    }
    public static void bfs(int n){
        visited[n] = true;
        for(int i=1; i<N+1; i++){
            if(visited[i]==false && arr[n][i] == 1){
                visited[i] = true;
                bfs(i);
            }
        }
    }
}