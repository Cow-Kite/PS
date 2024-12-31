import java.io.*;
import java.util.*;


public class Main {
  
	
	public static void changeR(Deque<Integer> q) {
		
		int v=q.getLast();
		q.pollLast();
		q.addFirst(v);
		
	}
	
	public static void changeL(Deque<Integer> q) {
		
		int v=q.getFirst();
		q.removeFirst();
		q.addLast(v);
		
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	
    	StringTokenizer st=new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        LinkedList<Integer> deque = new LinkedList<Integer>();
        int arr[]=new int[N];
        
        st=new StringTokenizer(br.readLine());
        for(int i=0; i<M; i++) {
        	arr[i]=Integer.parseInt(st.nextToken());
        }
        for(int i=1; i<=N; i++) {
        	deque.add(i);
        }
        int count=0;
       
    	for(int i=0; i<M; i++) {
    		while(true) {
    			if(deque.getFirst()==arr[i]) {
        			deque.remove();
        			break;
        		}
        		if(deque.indexOf(arr[i])<=deque.size()/2) {
        			changeL(deque);
        			count++;
        		}
        		else {
        			changeR(deque);
        			count++;
        		}
    		}
            	
        	
        }
        System.out.println(count);
    }
}