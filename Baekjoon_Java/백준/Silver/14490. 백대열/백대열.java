import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), ":");
        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());
        long A1 = A;
        long B1 = B;
        long ans = gcd(A1, B1);
        System.out.println(A/ans + ":" + B/ans);
    }
    public static long gcd(long A, long B){
        if(B == 0){
            return A;
        } else {
            return gcd(B, A%B);
        }
    }
}
