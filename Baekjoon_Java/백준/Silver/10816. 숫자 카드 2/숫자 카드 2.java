import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        HashMap<Integer, Integer> map = new HashMap<>();
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i = 0; i < N; i++){
            int num = Integer.parseInt(st.nextToken());
            if(map.containsKey(num)){
                map.replace(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int num2 = Integer.parseInt(st.nextToken());
            if(map.containsKey(num2)){
                bw.write(String.valueOf(map.get(num2)) + " ");
            } else {
                bw.write(String.valueOf(0) + " ");
            }
        }

        bw.flush();
    }
}