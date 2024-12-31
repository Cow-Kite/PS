import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int [] ans = new int [N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            ans[i] = Integer.parseInt(st.nextToken());
        }

        int M = Integer.parseInt(br.readLine());
        int [] nums = new int [M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(ans);

        for (int i = 0; i < M; i++) {
            System.out.println(find(nums[i], ans));
        }
    }
    public static int find(int A, int [] ans){
        int low = 0;
        int high = ans.length-1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(A == ans[mid]){
                return 1;
            } else if (A > ans[mid]){
                low = mid + 1 ;
            } else {
                high = mid - 1;
            }
        }
        return 0;
    }
}