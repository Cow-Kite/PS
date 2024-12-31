import java.util.*;
import java.io.*;

public class Main{

    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int getsu = Integer.parseInt(br.readLine());
        int [] top = new int [getsu+1];
        int [] answer = new int [getsu+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=1; i<=getsu; i++){
            top[i] = Integer.parseInt(st.nextToken());
        }
        Stack<Integer>stack = new Stack<>();
        stack.push(getsu);
        int index = getsu-1;
        while(index >= 0){
            while(!stack.isEmpty()) {
                int height = top[stack.peek()];
                if (top[index] > height) {
                    answer[stack.pop()] = index;
                } else {
                    break;
                }
            }
            stack.push(index);
            index--;
        }
        for (int i = 1; i <= getsu; i++) {
            System.out.print(answer[i] + " ");
        }
    }
}