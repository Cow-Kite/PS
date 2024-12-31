import java.io.*;

public class Main {
    static int N;
    static String str;
    static int alpha [];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        str = br.readLine();
        int [] alpha = new int [26];

        int start = 0;
        int end = 0;
        alpha[str.charAt(0)-97]++;
        int count = 1;
        int max = 1;

        while(true){
            end++;
            if(end == str.length()) break;

            int num = str.charAt(end) - 'a';
            alpha[num]++;

            if(alpha[num] == 1){
                count++;
            }

            while(count > N){
                int num2 = str.charAt(start) - 'a';
                alpha[num2]--;

                if(alpha[num2] == 0){
                    count--;
                }

                start++;
            }

            max = Math.max(max, end-start+1);
        }
        System.out.println(max);
    }
}