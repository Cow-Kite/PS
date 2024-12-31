import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine());
        for(int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long [] arr = new long[st.countTokens()];
            for (int j = 0; j < arr.length; j++) {
                arr[j] = Long.parseLong(st.nextToken());
            }

            List<Long> nums = new LinkedList<>();
            for(int k=0; k<arr.length-1; k++){
                for(int h=k+1; h< arr.length; h++){
                    nums.add(gcd(arr[k], arr[h]));
                }
            }
            Collections.sort(nums, Collections.reverseOrder());
            System.out.println(nums.get(0));
        }

    }
    public static long gcd(long A, long B){
        if(B == 0)
            return A;
        else
            return gcd(B, A%B);
    }
}