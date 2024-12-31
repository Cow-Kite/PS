class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean [] visited = new boolean[n];
        for(int i=0; i<n; i++){
            if(visited[i]) continue;
            answer++;
            dfs(i, computers, visited);
        }
        return answer;
    }
    void dfs(int start, int[][]computers, boolean [] visited){
        visited[start] = true;
        for(int i=0; i<computers.length; i++){
            if(visited[i]==false && computers[start][i]==1)
                dfs(i, computers, visited);
        }
    }
}