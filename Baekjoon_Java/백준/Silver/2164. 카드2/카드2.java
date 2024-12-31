import java.util.*;
import java.io.*;

public class Main {

    static int n,m;
    static String[] arr;
    static ArrayList<String> list=new ArrayList<>();
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        n=Integer.parseInt(br.readLine());

        Queue<Integer> q=new LinkedList<>();

        for(int i=0; i<n; i++){
            q.add(i+1);
        }

        while(q.size()!=1){

            q.poll();
            int value=q.poll();
            q.add(value);
        }
        System.out.println(q.peek());



    }

}
