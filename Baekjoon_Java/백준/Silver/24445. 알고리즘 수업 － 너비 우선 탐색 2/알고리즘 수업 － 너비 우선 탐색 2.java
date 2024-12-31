import java.util.*;
import java.io.*;

public class Main{
    static  int N, M, R;
    static ArrayList<Integer> graph [];
    static int [] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken()); //정점의 수
        M = Integer.parseInt(st.nextToken()); //간선의 수
        R = Integer.parseInt(st.nextToken()); //시작 정점

        graph = new ArrayList [N+1];
        visited = new int [N+1];
        for(int i=1; i<=N; i++){
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            graph[x].add(y);
            graph[y].add(x);
        }

        for (int i = 1; i < N+1; i++) {
            graph[i].sort(Comparator.reverseOrder());
        }
        bfs(R);

        for (int i = 1; i < N+1; i++) {
            System.out.println(visited[i]);
        }

    }
    public static void bfs(int R){
        int count = 1;
        Queue<Integer> q = new LinkedList<>();
        q.offer(R);
        visited[R] = count;
        while(!q.isEmpty()){
            Integer num = q.poll();
            for(Integer a : graph[num]){
                if(visited[a] == 0){
                    q.offer(a);
                    count++;
                    visited[a] = count;
                }
            }
        }
    }
}