import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Stack<Long>stack = new Stack<>();
        stack.push(Long.parseLong(br.readLine()));
        long sum = 0;
        for (int i = 0; i < N-1; i++) {
            long height = Long.parseLong(br.readLine());
            while(!stack.isEmpty()) {
                if (stack.peek() > height) {
                    sum += stack.size();
                    break;
                } else {
                    stack.pop();
                }
            }
            stack.push(height);
        }
        System.out.println(sum);
    }
}