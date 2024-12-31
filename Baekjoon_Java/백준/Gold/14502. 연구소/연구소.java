import java.util.*;
import java.io.*;

public class Main {
    static int N, M, result;
    static int [][] map;
    static int [][] copymap;
    static int X [] = {0, 0, 1, -1};
    static int Y [] = {1, -1, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int [N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        wall(0);
        System.out.println(result);
    }

    public static void wall(int count){
        if(count == 3){
            spread();
            return;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(map[i][j] == 0){
                    map[i][j] = 1;
                    wall(count+1);
                    map[i][j] = 0;
                }
            }
        }
    }

    public static void spread(){
        copymap = new int [N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                copymap[i][j] = map[i][j];
            }
        }

        Queue<Virus> q = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(copymap[i][j] == 2) q.offer(new Virus(i, j));
            }
        }

        while(!q.isEmpty()){
            Virus v = q.poll();
            for (int i = 0; i < 4; i++) {
                int newX = X[i] + v.x;
                int newY = Y[i] + v.y;
                if(newX >= 0 && newX < N && newY >= 0 && newY <M) {
                    if (copymap[newX][newY] == 0) {
                        copymap[newX][newY] = 2;
                        q.offer(new Virus(newX, newY));
                    }
                }
            }
        }

        virusCount(copymap);
    }

    public static void virusCount(int [][] copymap){
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(copymap[i][j] == 0) cnt++;
            }
        }
        result = Math.max(result, cnt);
    }
}

class Virus {
    int x, y;
    Virus(int x, int y){
        this.x = x;
        this.y = y;
    }
}