import java.io.*;
import java.util.*;

class number {
    int x;
    int y;
    public number(int x, int y){
        this.x = x;
        this.y = y;
    }
}
public class Main {
    static int N, M;
    static int [][] map;
    static boolean [][] visited;
    static int [] X = {-1, 0, 1, 0};
    static int [] Y = {0, -1, 0, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int [N][M];
        visited = new boolean [N][M];
        for(int i=0; i<N; i++){
            String str = br.readLine();
            for(int j=0; j<M; j++){
                map[i][j] = str.charAt(j) - '0';
            }
        }
        visited[0][0] = true;
        bfs(0, 0);
        System.out.println(map[N-1][M-1]);
    }
    static void bfs(int x, int y){
        Queue<number> queue = new LinkedList<>();
        queue.offer(new number(x, y));
        while(!queue.isEmpty()){
            number move = queue.poll();
            for(int i=0; i<4; i++){
                int newX = move.x + X[i];
                int newY = move.y + Y[i];
                if(newX >= 0 && newX < N && newY >= 0 && newY <M){
                    if(map[newX][newY]!=0 && !visited[newX][newY]){
                        visited[newX][newY] = true;
                        map[newX][newY] = map[move.x][move.y] + 1;
                        queue.offer(new number(newX, newY));
                    }
                }
            }
        }
    }
}