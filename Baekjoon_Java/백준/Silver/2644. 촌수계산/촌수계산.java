import java.util.*;
import java.io.*;

public class Main{
    static int N, M;
    static int start, target;
    static int [][] map;
    static boolean [] visited;
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        target = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(br.readLine());
        map = new int [N+1][N+1];
        visited = new boolean[N+1];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            map[n1][n2] = 1;
            map[n2][n1] = 1;
        }
        bfs(start, 0);
    }
    public static void bfs(int start, int count){
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        while(!queue.isEmpty()){
            int size = queue.size();
            for (int k = 0; k < size; k++) {
                int person = queue.poll();
                visited[start] = true;
                if(person == target){
                    System.out.println(count); return;
                }
                for(int i=1; i<=N; i++){
                    if(map[person][i] == 1 && visited[i] == false){
                        queue.offer(i);
                        visited[i] = true;
                    }
                }
            }
            count++;
        }
        System.out.println(-1);
    }
}