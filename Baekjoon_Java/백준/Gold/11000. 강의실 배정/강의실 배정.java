import java.util.*;
import java.io.*;

class Time {
    int start, end;
    Time(int start, int end){
        this.start = start;
        this.end = end;
    }
}
public class Main {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        List<Time> list = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            list.add(new Time(start, end));
        }

        list.sort(((o1, o2) -> {
            if(o1.start == o2.start) return o1.end - o2.end;
            return o1.start - o2.start;
        }));

        PriorityQueue<Integer> q = new PriorityQueue<>();

        for (Time t : list){
            int endTime = t.end;
            if(!q.isEmpty() && q.peek() <= t.start){
                q.poll();
            }
            q.offer(endTime);
        }
        bw.write(String.valueOf(q.size()));
        bw.flush();
    }
}