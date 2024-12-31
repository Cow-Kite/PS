import java.util.*;
import java.io.*;

public class Main{
    static int N, M;//사다리 수, 뱀의 수
    static int [] map;
    static boolean [] visited;
    static int [] ladderAndsnake;
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int [101]; //1번 부터 100번 칸
        visited = new boolean[101];
        ladderAndsnake = new int [101];

        for (int i = 0; i < N+M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            ladderAndsnake[x] = y;
        }
        Queue<Integer> q = new LinkedList<>();

        q.offer(1);
        visited[1] = true;

        count = 0;
        boolean find = false;
        while(!q.isEmpty()){
            int size = q.size();

            for(int k=0; k<size; k++) {
                int n = q.poll();

                if(n==100){
                    System.out.println(count);
                    return;
                }

                for (int i = 1; i <= 6; i++) {
                    if(n+i <= 100){
                        int next = n + i;
                        if(ladderAndsnake[next] > 0){
                            next = ladderAndsnake[next];
                        }
                        if(!visited[next]){
                            visited[next] = true;
                            q.offer(next);
                        }
                    }
                }
            }
            count++;
        }
    }
}