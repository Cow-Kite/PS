
import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long T = Long.parseLong(br.readLine());
        int n = Integer.parseInt(br.readLine());
        long [] A = new long[n] ;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            A[i] = Long.parseLong(st.nextToken());
        }
        int m = Integer.parseInt(br.readLine());
        long [] B = new long [m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            B[i] = Long.parseLong(st.nextToken());
        }
        //System.out.println(Arrays.toString(A));
        //System.out.println(Arrays.toString(B));
        List<Long> subA = new ArrayList<>();
        List<Long> subB = new ArrayList<>();
        //subA 구하기
        for(int i=0; i<n; i++){
            long sum = 0;
            for(int j = i; j<n; j++){
                sum += A[j];
                subA.add(sum);
            }
        }
        //subB 구하기
        for(int i=0; i<m; i++){
            long sum = 0;
            for(int j=i; j<m; j++){
                sum += B[j];
                subB.add(sum);
            }
        }
        //subA, subB 정렬하기
        Collections.sort(subA);
        Collections.sort(subB, Collections.reverseOrder());
        //System.out.println(subA);
        //System.out.println(subB);
        int p1 = 0;
        int p2 = 0;
        long count = 0;

        while(true){
            long hap = subA.get(p1) + subB.get(p2);
            long sameA = 1, sameB = 1;
            if(hap==T){
                //hap이 T랑 같으면
                //subA의 현재 값 이랑 똑같은 값의 개수 *
                for(int i = p1+1; i<subA.size(); i++){
                    if(subA.get(p1).equals(subA.get(i))) {
                        sameA++;
                    }
                    else break;
                }
                //subB의 현재 값이랑 똑같은 값의 개수
                for(int j = p2+1; j< subB.size(); j++){
                    if(subB.get(p2).equals(subB.get(j))) {
                        sameB++;
                    }
                    else break;
                }
                count += (sameA*sameB);
                p1 += sameA; // 같은 값들 건너뛰기
                p2 += sameB;

            } else if(hap < T){
                //hap이 T보다 작으면
                //subA를 다음 값으로 p1++
                p1++;
            } else {
                //hap이 T보다 크면
                //subB를 다음 값으로 p2++
                p2++;
            }
            if(p2 >= subB.size() || p1 >= subA.size())
                break;
        }
        System.out.println(count);
    }

}