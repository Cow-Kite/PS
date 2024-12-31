import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Set<Integer> setA = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            setA.add(Integer.parseInt(st.nextToken()));
        }

        Set<Integer> setB = new HashSet<>();
        int count2 = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int b = Integer.parseInt(st.nextToken());
            setB.add(b);
            if(!setA.contains(b)) count2++;
        }

        int count1 = 0;
        for(int a : setA){
            if(!setB.contains(a)) count1++;
        }

        System.out.println(count1 + count2);
    }
}