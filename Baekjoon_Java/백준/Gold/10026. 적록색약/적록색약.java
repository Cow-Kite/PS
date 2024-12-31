import java.io.*;
import java.util.*;
public class Main {
    // 적록색맹은 빨강-초록 같이 생각
    static char [][] color;
    static boolean visited [][];
    static int N;
    static int count;
    static int [] X = {0, 0, 1, -1};
    static int [] Y = {1, -1, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        color = new char [N][N];
        visited = new boolean [N][N];
        count = 0;
        for(int i=0; i<N; i++){
            String str = br.readLine();
            for(int j=0; j<N; j++){
                color[i][j] = str.charAt(j);
            }
        }

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(color[i][j] == 'R' && visited[i][j] == false){
                    count++;
                    dfs(i, j, 'R');
                }
                if(color[i][j] == 'G' && visited[i][j] == false){
                    count++;
                    dfs(i, j, 'G');
                }
                if(color[i][j] == 'B' && visited[i][j] == false){
                    count++;
                    dfs(i, j, 'B');
                }
            }
        }
        System.out.println(count);
        visited = new boolean [N][N];
        count = 0;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(color[i][j] == 'G')
                    color[i][j] = 'R';
            }
        }

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(color[i][j] == 'R' && visited[i][j] == false){
                    count++;
                    dfs(i, j, 'R');
                }
                if(color[i][j] == 'B' && visited[i][j] == false){
                    count++;
                    dfs(i, j, 'B');
                }
            }
        }
        System.out.println(count);
    }
    public static void dfs(int n1, int n2, char c) {
        int newX = 0, newY = 0;
        visited[n1][n2] = true;
        for(int i=0; i<4; i++){
            newX = n1 + X[i];
            newY = n2 + Y[i];
            if(newX >= 0 && newX < N && newY >= 0 && newY <N){
                if(visited[newX][newY]==false && color[newX][newY] == c){
                    visited[newX][newY] = true;
                    dfs(newX, newY, c);
                }
            }
        }
    }
}