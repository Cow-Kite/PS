import java.util.*;
import java.io.*;

public class Main {
    static int N, S;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());

        int [] number = new int [N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            number[i] = Integer.parseInt(st.nextToken());
        }

        int length = 100001;
        int start = 0;
        int end = 0;
        int hap = 0;

        while(true){
            if(hap >= S){
                hap -= number[start++];
                length = Math.min(length, (end-start)+1);
            } else if(end == N){
                break;
            } else {
                hap += number[end++];
            }
        }
        if(length==100001) bw.write(String.valueOf(0));
        else {
            bw.write(String.valueOf(length));
        }
        bw.flush();
    }
}