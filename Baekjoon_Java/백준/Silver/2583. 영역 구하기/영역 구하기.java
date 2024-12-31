import java.util.*;
import java.io.*;

public class Main{
    static int M, N, K;
    static boolean [][] map;
    static int x1, y1, x2, y2;
    static int area;
    static int getsu;
    static int [] X = {1, -1, 0, 0};
    static int [] Y = {0, 0, 1, -1};
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        map = new boolean [N][M];
        getsu = 0;
        area = 0;
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            x1 = Integer.parseInt(st.nextToken());
            y1 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            for(int j=x1; j<x2; j++){
                for(int k=y1; k<y2; k++){
                    map[j][k] = true;
                }
            }
        }

        List<Integer> size = new LinkedList<>();
        for (int i = 0; i < N; i++) {

            for (int j = 0; j < M; j++) {
                if(!map[i][j]){
                    getsu++;
                    is(i, j);
                }
                if(area!=0){
                    size.add(area);
                }
                area=0;
            }
        }

        System.out.println(getsu);
        Collections.sort(size);
        for(int i : size){
            System.out.print(i + " ");
        }
    }

    public static void is(int x, int y){
        map[x][y] = true;
        area++;
        int newXX, newYY;
        for(int i=0; i<4; i++){
            newXX = x + X[i];
            newYY = y + Y[i];
            if(newXX >= 0 && newXX <N && newYY >= 0 && newYY <M){
                if(!map[newXX][newYY]){
                    is(newXX, newYY);
                }
            }
        }
    }
}