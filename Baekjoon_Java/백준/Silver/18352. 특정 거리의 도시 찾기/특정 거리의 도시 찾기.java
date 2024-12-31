import java.util.*;
import java.io.*;

public class Main{
    static int N, M, K, X; //도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
    static ArrayList<Integer> town [];
    static boolean visited [];
    static ArrayList<Integer> answer;
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        town = new ArrayList[N+1];
        visited = new boolean[N+1];
        answer = new ArrayList<>();

        for (int i = 1; i < N+1; i++) {
            town[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            town[Integer.parseInt(st.nextToken())].add(Integer.parseInt(st.nextToken()));
        }
        bfs();
        Collections.sort(answer);

        for(int ans : answer){
            System.out.println(ans);
        }
    }
    public static void bfs(){
        Queue<Integer> q = new LinkedList<>();
        boolean find = false;
        q.offer(X);
        visited[X] = true;
        while(!q.isEmpty()){
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int num = q.poll();
                if(count == K){
                    answer.add(num);
                    find = true;
                }
                for (int end : town[num]) {
                    if(!visited[end]){
                        visited[end] = true;
                        q.offer(end);
                    }
                }
            }
            count++;
        }
        if(!find)
            System.out.println(-1);
    }
}