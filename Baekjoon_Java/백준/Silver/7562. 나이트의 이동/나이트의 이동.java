import java.util.*;
import java.io.*;

public class Main{
    static int T, I;
    static boolean visited [][];
    static int [] x = {-2, -1, 1, 2, 2, 1, -1, -2};
    static int [] y = {-1, -2, -2, -1, 1, 2, 2, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            I = Integer.parseInt(br.readLine());
            visited = new boolean[I][I];
            StringTokenizer st = new StringTokenizer(br.readLine());
            int startX = Integer.parseInt(st.nextToken());
            int startY = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            int endX = Integer.parseInt(st.nextToken());
            int endY = Integer.parseInt(st.nextToken());
            bfs(startX, startY, endX, endY);
        }
    }
    public static void bfs(int startX, int startY, int endX, int endY){
        int count = 0;
        Queue<Graph> q = new LinkedList<>();
        q.offer(new Graph(startX, startY));
        while(!q.isEmpty()){
            int size = q.size();
            for(int j=0; j<size; j++) {
                Graph now = q.poll();
                if(now.x == endX && now.y == endY){
                    System.out.println(count);
                    return;
                }
                for (int i = 0; i < 8; i++) {
                    int newX = now.x + x[i];
                    int newY = now.y + y[i];
                    if (newX >= 0 && newX < I && newY >= 0 && newY < I) {
                        if(!visited[newX][newY]) {
                            visited[newX][newY] = true;
                            q.offer(new Graph(newX, newY));
                        }
                    }
                }
            }
            count++;
        }
    }

    public static class Graph{
        int x, y;
        public Graph(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}