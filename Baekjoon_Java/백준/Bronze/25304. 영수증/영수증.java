import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        int hap = 0;

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            hap += Integer.parseInt(st.nextToken()) * Integer.parseInt(st.nextToken());
        }

        if(hap == X){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}