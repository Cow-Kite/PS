import java.io.*;
import java.util.*;
public class Main {
    static int N;
    static int num;
    static int [][] house;
    static boolean [][] visited;
    static List<Integer> getsu;
    static int [] x = {0, 0, 1, -1};
    static int [] y = {1, -1, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int count = 0;
        getsu = new LinkedList<>();
        house = new int [N][N];
        visited = new boolean [N][N];
        for(int i=0; i<N; i++){
            String str = br.readLine();
            for(int j=0; j<N; j++){
                house[i][j] = str.charAt(j) - '0';
            }
        }

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(house[i][j]==1 && visited[i][j]==false){
                    num = 1;
                    dfs(i, j);
                    getsu.add(num);
                }
            }
        }
        System.out.println(getsu.size());
        Collections.sort(getsu);
        for(int i : getsu){
            System.out.println(i);
        }
    }
    public static void dfs(int n1, int n2){
        int newX = 0;
        int newY = 0;
        visited[n1][n2] = true;
        for(int i=0; i<4; i++){
            newX = n1 + x[i];
            newY = n2 + y[i];
            if(newX < N && newY <N && newX >= 0 && newY >= 0) {
                if (visited[newX][newY] == false && house[newX][newY] == 1) {
                    visited[newX][newY] = true;
                    num++;
                    dfs(newX, newY);
                }
            }
        }
    }
}