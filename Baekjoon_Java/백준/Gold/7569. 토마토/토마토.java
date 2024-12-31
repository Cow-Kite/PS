import java.util.*;
import java.io.*;

public class Main{
    static int M, N, H;
    static boolean [][][] visited;
    static Queue<tomato> q;
    static int [] Z = {0, 0, 0, 0, 1, -1};
    static int [] X = {0, 1, 0, -1, 0, 0};
    static int [] Y = {1, 0, -1, 0, 0, 0};
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        visited = new boolean[H][N][M];
        q = new LinkedList<>();
        count = -1;
        boolean isTrue = false;
        for(int k=0; k<H; k++) {
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < M; j++) {
                    int num = Integer.parseInt(st.nextToken());
                    if (num == 1) {
                        q.offer(new tomato(i, j, k));
                        visited[k][i][j] = true;
                    }
                    if (num == -1) {
                        visited[k][i][j] = true;
                    }
                }
            }
        }
        bfs(q);
        for(int k=0; k<H; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (!visited[k][i][j]) {
                        System.out.println(-1);
                        return;
                    }
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
                for (int j = 0; j < 6; j++) {
                    int newX = now.x + X[j];
                    int newY = now.y + Y[j];
                    int newZ = now.z + Z[j];
                    if(newX>=0 && newX <N && newY >=0 && newY <M && newZ >= 0 && newZ <H) {
                        if (visited[newZ][newX][newY] == false) {
                            visited[newZ][newX][newY] = true;
                            q.offer(new tomato(newX, newY, newZ));
                        }
                    }
                }
            }
            count++;
        }
    }
    static class tomato{
        int x, y, z;
        public tomato(int x, int y, int z){
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }

}