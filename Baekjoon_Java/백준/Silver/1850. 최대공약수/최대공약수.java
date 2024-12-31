import java.util.*;
import java.io.*;

public class Main{
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        long c = gcd(a, b);
        for (long i=0; i<c; i++){
            bw.write("1");
        }
        bw.flush();
        bw.close();
    }
    public static long gcd(long a, long b){
        if(b==0) {
            return a;
        } else {
            return gcd(b, a%b);
        }
    }
}