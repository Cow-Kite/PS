import java.util.Scanner;

public class Main {
    
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int [] x = new int [N];
        int [] y = new int [N];
        int [] rank = new int [N];
        
        for(int i=0; i<N; i++) {
        	x[i] = sc.nextInt();
        	y[i] = sc.nextInt();
        }
        
        for(int i=0; i<N; i++) {
        	int count = 1;
        	for(int j=0; j<N; j++) {
        		if(x[i]<x[j] && y[i]<y[j])
        			count++;
        	}
        	System.out.print(count+" ");
        }
        
//        int array = 0;
//        while(array != 5) {
//        	int array2 = 0;
//        	int count = 1;
//        	while(array2 !=5) {
//        		if(x[array]>x[array2]&&y[array]>y[array2])
//        			continue;
//        		else
//        			count++;
//        		array2++;
//        	}
//        	rank[array] = count;
//        	array++;
//        }
        
//        for(int i=0; i<N; i++) {
//        	System.out.println(rank[i]);
//        }
    }
}