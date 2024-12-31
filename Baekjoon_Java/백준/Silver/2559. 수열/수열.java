import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int [] nums = new int [N];
        st = new StringTokenizer(br.readLine());
        int sum = 0;
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            if(i<K) sum += nums[i];
        }

        int result = sum;
        int start = 0;
        int end = K;
        while(end < N){
            sum -= nums[start];
            sum += nums[end];
            result = Math.max(result, sum);
            start++; end++;
        }

        System.out.println(result);
    }
}