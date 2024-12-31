import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        Set<String> set = new HashSet<>();
        for (int i = 0; i < str.length(); i++) {
            set.add(String.valueOf(str.charAt(i)));
            for (int j = i+1; j < str.length(); j++) {
                set.add(str.substring(i, j+1));
            }
        }

        System.out.println(set.size());
    }
}