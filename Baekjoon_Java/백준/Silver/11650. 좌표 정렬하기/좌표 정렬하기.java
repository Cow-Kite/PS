import java.util.*;
import java.io.*;

class xy{
    int x, y;
    xy(int x, int y){
        this.x = x;
        this.y = y;
    }
}
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<xy> list = new ArrayList<>();

        for(int i = 0; i < N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            list.add(new xy(x, y));
        }

        list.sort(((o1, o2) -> {
            if(o1.x == o2.x){
                return o1.y - o2.y;
            }
            return o1.x - o2.x;
        }));

        for(xy a : list){
            System.out.println(a.x + " " + a.y);
        }
    }
}