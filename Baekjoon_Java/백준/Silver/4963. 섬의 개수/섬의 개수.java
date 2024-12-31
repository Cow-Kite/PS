import java.io.*;
import java.util.*;
public class Main {
    static int [][] map;
    static boolean visited [][];
    static int W;
    static int H;
    static int count;
    static int [] X = {0, 0, 1, -1, -1, -1, +1, +1};
    static int [] Y = {1, -1, 0, 0, -1, +1, -1, +1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            W = Integer.parseInt(st.nextToken()); // 가로 길이
            H = Integer.parseInt(st.nextToken()); // 세로 길이
            map = new int[H][W];
            visited = new boolean[H][W];
            count = 0;
            if(W == 0 && H == 0) return;
            else if(W == 1 && H == 1){
                int num = Integer.parseInt(br.readLine());
                if(num == 0) count = 0;
                else if(num == 1) count = 1;
            }
            else {
                for (int i = 0; i < H; i++) {
                    st = new StringTokenizer(br.readLine());
                    for (int j = 0; j < W; j++) {
                        map[i][j] = Integer.parseInt(st.nextToken());
                    }
                }

                for (int i = 0; i < H; i++) {
                    for (int j = 0; j < W; j++) {
                        if (visited[i][j] == false && map[i][j] == 1) {
                            count++;
                            dfs(i, j);
                        }
                    }
                }
            }
            System.out.println(count);
        }
    }
    public static void bfs(int n1, int n2){
        int newX = 0, newY = 0;
        visited[n1][n2] = true;
        for(int i=0; i<8; i++){
            newX = n1 + X[i];
            newY = n2 + Y[i];
            if(newX<H && newX >=0 && newY<W && newY >=0){
                if(visited[newX][newY] == false && map[newX][newY] == 1){
                    visited[newX][newY] = true;
                    dfs(newX, newY);
                }
            }
        }
    }
}
