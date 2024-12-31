import java.util.*;
import java.io.*;

public class Main{
    static int N, M; //컴퓨터 개수, 신뢰하는 관계
    static ArrayList<Integer> computer [];
    static int answer [];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        computer = new ArrayList[N+1];
        answer = new int[N+1];

        for (int i = 0; i < N+1; i++) {
            computer[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int num1 = Integer.parseInt(st.nextToken());
            int num2 = Integer.parseInt(st.nextToken());
            computer[num1].add(num2);
        }

        for (int i = 1; i < N+1; i++) {
            bfs(i);
        }

        int max = 0;
        for (int i = 1; i <= N; i++) {
            max = Math.max(max, answer[i]);
        }
        for (int i = 1; i <= N; i++) {
            if(max == answer[i]){
                System.out.print(i + " ");
            }
        }
    }
    public static void bfs(int start){
        boolean visited [] = new boolean[N+1];
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        visited[start] = true;
        answer[start]++;
        while(!q.isEmpty()){
            int com = q.poll();
            for(int link : computer[com]){
                if(!visited[link]){
                    visited[link] = true;
                    answer[link]++;
                    q.offer(link);
                }
            }
        }
    }
}