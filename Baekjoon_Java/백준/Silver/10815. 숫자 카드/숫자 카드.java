import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long [] cards = new long[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            cards[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(cards);
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            long find = Long.parseLong(st.nextToken());
            System.out.print(search(cards, find) + " ");
        }
    }
    public static int search(long [] cards, long find){
        int low = 0;
        int high = cards.length-1;
        while(low <= high){
            int mid = (low+high)/2;
            if(cards[mid] == find){
                return 1;
            } else if(cards[mid] < find){
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return 0;
    }
}