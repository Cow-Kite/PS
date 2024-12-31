import java.io.*;
import java.util.*;
public class Main {
    static int [][] arr;
    static boolean [] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); // 정점의 개수
        int M = Integer.parseInt(st.nextToken()); // 간선의 개수
        int V = Integer.parseInt(st.nextToken()); // 탐색을 시작할 정점의 번호

        arr = new int[N+1][N+1];
        visited = new boolean [N+1];

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            arr[start][end] = 1;
            arr[end][start] = 1;
        }

        dfs(V);
        System.out.println();

        visited = new boolean[N+1];
        bfs(V);

    }
    public static void dfs(int V){
        visited[V] = true;
        System.out.print(V + " ");
        for(int i=1; i<arr.length; i++){
            if(visited[i]==false && arr[V][i]==1){
                dfs(i);
            }
        }
    }

    public static void bfs(int V){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(V);
        System.out.print(V + " ");
        visited[V] = true;
        while(!queue.isEmpty()){
            int index = queue.poll();
            for(int i=1; i<arr.length; i++){
                if(arr[index][i] == 1 && visited[i]==false){
                    queue.add(i);
                    visited[i] = true;
                    System.out.print(i + " ");
                }
            }
        }
    }
}