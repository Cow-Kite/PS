import java.io.*;
import java.util.*;
public class Main {
    static int [][] map;
    static int M;
    static int N;
    static boolean [][] visited;
    static int worm;
    static int [] X = {0, 0, -1, 1};
    static int [] Y = {1, -1, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int i=0; i<T; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            map = new int [M][N];
            visited = new boolean [M][N];
            worm = 0;
            for(int j=0; j<K; j++){
                st = new StringTokenizer(br.readLine());
                map[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())] = 1;
            }

            for(int n1 = 0; n1<M; n1++){
                for(int n2 = 0; n2<N; n2++){
                    if(map[n1][n2]==1 && visited[n1][n2]==false){
                        worm++;
                        dfs(n1, n2);
                    }
                }
            }
            System.out.println(worm);
        }
    }
    public static void dfs(int n1, int n2){
        int newX = 0;
        int newY = 0;
        visited[n1][n2] = true;
        for(int i=0; i<4; i++){
            newX = n1 + X[i];
            newY = n2 + Y[i];
            if(newX>=0 && newX<M && newY>=0 && newY <N){
                if(visited[newX][newY] == false && map[newX][newY] == 1){
                    visited[newX][newY] = true;
                    dfs(newX, newY);
                }
            }
        }
    }
}