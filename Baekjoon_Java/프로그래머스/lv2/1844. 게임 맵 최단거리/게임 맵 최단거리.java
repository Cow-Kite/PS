import java.util.*;
class number {
    int x; 
    int y;
    public number(int x, int y){
        this.x = x;
        this.y = y;
    }
}
class Solution {
    static int [][] map;
    static boolean [][] visited;
    static int [] X = {1, -1, 0, 0};
    static int [] Y = {0, 0, 1, -1};
    public int solution(int[][] maps) {
        map = maps;
        visited = new boolean [map.length][map[0].length];
        visited[0][0] = true;
        bfs(0, 0);
        
        int answer = map[map.length-1][map[0].length-1];
        if(answer == 0 || answer == 1)
            return -1;
        else
            return answer;
    }
    static void bfs(int x, int y){
        Queue<number> queue = new LinkedList<>();
        queue.offer(new number(x, y));
        while(!queue.isEmpty()){
            number move = queue.poll();
            for(int i=0; i<4; i++){
                int newX = move.x + X[i];
                int newY = move.y + Y[i];
                if(newX >= 0 && newX < map.length && newY >= 0 && newY < map[0].length){
                    if(map[newX][newY]!=0 && !visited[newX][newY]){
                        visited[newX][newY] = true;
                        map[newX][newY] = map[move.x][move.y] + 1;
                        queue.offer(new number(newX, newY));
                    }
                }
            }
        }
    }
}