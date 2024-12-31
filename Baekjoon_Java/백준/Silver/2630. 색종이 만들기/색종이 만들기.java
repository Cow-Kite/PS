import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int paper [][];
    static int white, blue;
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        paper = new int [N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                paper[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        divide(0, 0, N);
        bw.write(String.valueOf(white) + "\n");
        bw.write(String.valueOf(blue));
        bw.flush();
    }
    public static void divide(int row, int col, int size){
        if(colorCheck(row, col, size)){
            if(paper[row][col]==0){
                white++;
            } else {
                blue++;
            }
            return;
        }
        int newSize = size / 2;
        divide(row, col, newSize); //제2사분면
        divide(row, col + newSize, newSize); //제1사분면
        divide(row + newSize, col, newSize); //제3사분면
        divide(row + newSize, col + newSize, newSize); //제4사분면
    }

    public static boolean colorCheck(int row, int col, int size){
        int start = paper[row][col];
        for (int i = row; i < row + size; i++) {
            for (int j = col; j < col + size; j++) {
                if(paper[i][j] != start)
                    return false;
            }
        }
        return true;
    }
}