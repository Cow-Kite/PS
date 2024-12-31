import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<String, String> map = new HashMap<>();

        for (int i = 1; i < N+1; i++) {
            String name = br.readLine();
            String number = Integer.toString(i);
            map.put(name, number);
            map.put(number, name);
        }

        for (int i = 0; i < M; i++) {
            bw.write(map.get(br.readLine()) + "\n");
        }
        bw.flush();
    }
}