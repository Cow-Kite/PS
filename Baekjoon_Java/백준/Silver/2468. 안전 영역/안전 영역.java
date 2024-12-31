import java.io.*;
import java.util.*;
public class Main {
    static int [][] map;
    static boolean [][] sink;
    static int N;
    static int safe = 0;
    static int [] X = {0, 0, 1, -1};
    static int [] Y = {1, -1, 0, 0};
    static List<Integer> maxSafe;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int [N][N];
        int max = 0;
        maxSafe = new LinkedList<>();
        for(int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
                if(max < map[i][j]) max = map[i][j];
            }
        }

        for(int i=0; i<max; i++){
            safe = 0;
            sink = new boolean[N][N];
            for(int j=0; j<N; j++){
                for(int k=0; k<N; k++){
                    if(!sink[j][k] && map[j][k] > i){
                        safe++;
                        dfs(j, k, i);
                    }
                }
            }
            maxSafe.add(safe);
        }
        //System.out.println(maxSafe);
        Collections.sort(maxSafe, Collections.reverseOrder());
        System.out.println(maxSafe.get(0));
    }
    public static void dfs(int x, int y, int height) {
        int newX = 0, newY = 0;
        sink[x][y] = true;
        for(int i=0; i<4; i++){
            newX = x + X[i];
            newY = y + Y[i];
            if(newX >= 0 && newX < N && newY >= 0 && newY < N){
                if(sink[newX][newY] == false && map[newX][newY] > height){
                    sink[newX][newY] = true;
                    dfs(newX, newY, height);
                }
            }
        }
    }
}