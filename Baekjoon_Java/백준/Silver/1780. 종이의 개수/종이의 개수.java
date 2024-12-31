import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int paper [][];
    static int minus, zero, plus;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        paper = new int [N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                paper[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        divide(0, 0, N);
        bw.write(String.valueOf(minus)+"\n");
        bw.write(String.valueOf(zero)+"\n");
        bw.write(String.valueOf(plus));
        bw.flush();
    }
    public static void divide(int row, int col, int size){
        if(checkNum(row, col, size)){
            if(paper[row][col] == -1){
                minus++;
            } else if(paper[row][col] == 0){
                zero++;
            } else {
                plus++;
            }
            return;
        }

        int newSize = size / 3;
        divide(row, col, newSize);
        divide(row, col+newSize, newSize);
        divide(row, col + (newSize*2), newSize);

        divide(row + newSize, col, newSize);
        divide(row+newSize, col+newSize, newSize);
        divide(row+newSize, col+(newSize*2), newSize);

        divide(row+(newSize*2), col, newSize);
        divide(row+(newSize*2), col+newSize, newSize);
        divide(row+(newSize*2), col+(newSize*2), newSize);
    }

    public static boolean checkNum(int row, int col, int size){
        int start = paper[row][col];
        for (int i = row; i < row+size; i++) {
            for (int j = col; j < col+size; j++) {
                if(paper[i][j] != start)
                    return false;
            }
        }
        return true;
    }
}