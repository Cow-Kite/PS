import java.util.*;
import java.io.*;

class Homework {
    int day;
    int score;
    Homework(int day, int score){
            this.day = day;
            this.score = score;
    }
}
public class Main {
    static int N, sum;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        ArrayList<Homework> list = new ArrayList<>();
        int maxDay = 0;

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int day = Integer.parseInt(st.nextToken());
            int score = Integer.parseInt(st.nextToken());
            list.add(new Homework(day, score));
            maxDay = Math.max(maxDay, day);
        }
        
        for (int i = maxDay; i > 0; i--) {
            Homework ans = new Homework(0, 0);
            for(Homework hw : list){
                if(hw.day >= i){
                    if(ans.score < hw.score){
                        ans = hw;
                    }
                }
            }
            sum += ans.score;
            list.remove(ans);
        }
        bw.write(String.valueOf(sum));
        bw.flush();
    }
}