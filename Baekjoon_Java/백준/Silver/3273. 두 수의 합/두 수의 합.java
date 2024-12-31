import java.util.*;
import java.io.*;

public class Main {
    static int N, X, count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        int [] number = new int [N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            number[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(number);

        X = Integer.parseInt(br.readLine());

        int start = 0;
        int end = N-1;
        while(start < end){
            if(number[start] + number[end] >= X){
                if(number[start] + number[end] == X){
                    count++;
                }
                end--;
            } else {
                start++;
            }
        }
        bw.write(String.valueOf(count));
        bw.flush();
    }
}