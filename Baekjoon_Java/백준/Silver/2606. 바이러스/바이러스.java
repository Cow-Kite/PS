import java.io.*;
import java.util.*;
public class Main {
    static int [][] arr;
    static boolean [] visited;
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine()); // 정점의 개수
        int M = Integer.parseInt(br.readLine()); // 간선의 개수

        arr = new int[N+1][N+1];
        visited = new boolean [N+1];
        count = 0;
        for(int i=0; i<M; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            arr[start][end] = 1;
            arr[end][start] = 1;
        }

        dfs(1);
        System.out.println(count);

    }
    public static void dfs(int V){
        visited[V] = true;
        for(int i=1; i<arr.length; i++){
            if(visited[i]==false && arr[V][i]==1){
                dfs(i);
                count++;
            }
        }
    }
}