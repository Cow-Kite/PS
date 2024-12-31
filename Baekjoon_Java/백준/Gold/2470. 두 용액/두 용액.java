import java.util.*;
import java.io.*;

public class Main {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        long [] number = new long [N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            number[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(number);

        int start = 0;
        int end = N-1;
        long hap = number[start] + number[end];
        long close = Math.abs(hap);
        long min = number[start];
        long max = number[end];
        if(hap >= 0) end--;
        else start++;

        while(start < end){
            hap = number[start] + number[end];
            if(Math.abs(hap) < close){
                close = Math.abs(hap);
                min = number[start];
                max = number[end];
            }

            if(hap >= 0) end--;
            else start++;
        }
        bw.write(String.valueOf(min) + " " + String.valueOf(max));
        bw.flush();
    }
}