import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long M = Long.parseLong(st.nextToken());
        long N = Long.parseLong(st.nextToken());

        long [] snack = new long [(int)N];
        long max = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            snack[i] = Integer.parseInt(st.nextToken());
            if(max < snack[i])
                max = snack[i];
        }
        long result = 0;
        long low = 1;
        long high = max;
        while(low <= high){
            long mid = (low+high) / 2;
            long human = 0;
            for (int i = 0; i < N; i++) {
                human += snack[i] / mid;
            }
            if(human >= M) {
                result = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        System.out.println(result);
    }
}