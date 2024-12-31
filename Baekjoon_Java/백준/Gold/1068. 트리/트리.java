import java.util.*;
import java.io.*;

public class Main {
    static int N, root, deleteNode, answer;
    static ArrayList<Integer> list [];
    static boolean visited [];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        list = new ArrayList[N];
        visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            list[i] = new ArrayList<>();
        }

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            int k = Integer.parseInt(st.nextToken());
            if(k != -1){
                list[i].add(k);
                list[k].add(i);
            } else {
                root = i;
            }
        }

        deleteNode = Integer.parseInt(br.readLine());
        if(deleteNode == root){
            System.out.println(0);
        } else {
            DFS(root);
            System.out.println(answer);
        }
    }
    static void DFS(int number){
        visited[number] = true;
        int child = 0;
        for(int i : list[number]){
            if(!visited[i] && i != deleteNode){
                child++;
                DFS(i);
            }
        }
        if(child == 0){
            answer++;
        }
    }
}