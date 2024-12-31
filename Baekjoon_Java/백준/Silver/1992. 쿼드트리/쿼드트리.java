import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int paper [][];
    static String answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        paper = new int [N][N];
        answer = "";
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < N; j++) {
                paper[i][j] = Integer.parseInt(String.valueOf(str.charAt(j)));
            }
        }
        divide(0, 0, N);
        System.out.println(answer);
    }
    public static void divide(int row, int col, int size){
        if(colorCheck(row, col, size)){
            answer += String.valueOf(paper[row][col]);
            return;
        }
        answer += "(";
        int newSize = size / 2;
        divide(row, col, newSize); //제2사분면
        divide(row, col + newSize, newSize); //제1사분면
        divide(row + newSize, col, newSize); //제3사분면
        divide(row + newSize, col + newSize, newSize); //제4사분면
        answer += ")";
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