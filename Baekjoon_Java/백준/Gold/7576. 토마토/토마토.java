import java.util.*;
import java.io.*;

public class Main{
    static int M, N;
    static boolean [][] visited;
    static Queue<tomato> q;
    static int [] X = {0, 1, 0, -1};
    static int [] Y = {1, 0, -1, 0};
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        visited = new boolean[N][M];
        q = new LinkedList<>();
        count = -1;
        boolean isTrue = false;
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int num = Integer.parseInt(st.nextToken());
                if(num == 1){
                    q.offer(new tomato(i, j));
                    visited[i][j] = true;
                }
                if(num == -1){
                    visited[i][j] = true;
                }
            }
        }
        bfs(q);
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(!visited[i][j]) {
                    System.out.println(-1);
                    return;
                }
            }
        }
        System.out.println(count);
    }
    public static void bfs(Queue<tomato> q){
        while(!q.isEmpty()){
            int size = q.size();
            for (int i = 0; i < size; i++) {
                tomato now = q.poll();
                for (int j = 0; j < 4; j++) {
                    int newX = now.x + X[j];
                    int newY = now.y + Y[j];
                    if(newX>=0 && newX <N && newY >=0 && newY <M) {
                        if (visited[newX][newY] == false) {
                            visited[newX][newY] = true;
                            q.offer(new tomato(newX, newY));
                        }
                    }
                }
            }
            count++;
        }
    }
    static class tomato{
        int x, y;
        public tomato(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

}