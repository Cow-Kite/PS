import java.util.*;
import java.io.*;

class People{
    int age;
    String name;
    People(int age, String name){
        this.age = age;
        this.name = name;
    }
}
public class Main {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        ArrayList<People> list = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int age = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            list.add(new People(age, name));
        }
        list.sort(((o1, o2) -> {
            if(o1.age == o2.age) return 0;
            return o1.age - o2.age;
        }));

        for (People a : list){
            bw.write(String.valueOf(a.age) + " " + a.name + "\n");
        }
        bw.flush();
    }
}
