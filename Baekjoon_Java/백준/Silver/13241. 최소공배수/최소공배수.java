import java.util.*;
import java.io.*;

public class Main{
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());
        long ans = gcd(A, B);
        System.out.println( A * B / ans);
    }
    public static long gcd(long A, long B){
        if(B == 0){
            return A;
        } else {
            return gcd(B, A%B);
        }
    }
}