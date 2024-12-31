import java.util.*;
import java.io.*;

public class Main {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        ArrayList<String> list = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            if(!list.contains(str)) list.add(str);
        }
        list.sort(((o1, o2) -> {
            if(o1.length() == o2.length()) return o1.compareTo(o2);
            return o1.length() - o2.length();
        }));

        for(String st : list){
            bw.write(st + "\n");
        }
        bw.flush();
    }
}