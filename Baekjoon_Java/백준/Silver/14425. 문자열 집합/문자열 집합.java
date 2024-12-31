import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        ArrayList<String> list = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            list.add(str);
        }

        int count = 0;
        for (int i = 0; i < M; i++) {
            String is = br.readLine();
            if(list.contains(is)) count++;
        }

        System.out.println(count);
    }
}