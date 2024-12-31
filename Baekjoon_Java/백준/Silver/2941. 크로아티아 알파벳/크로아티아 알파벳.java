import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       String str=sc.next();
       int count=0;
       char c[]=new char[str.length()];
       for(int i=0; i<str.length(); i++) {
          c[i]=str.charAt(i);
         
       }
       for(int i=0; i<c.length-1; i++) {
          count++;
          if((c[i]=='c' && c[i+1]=='=') || (c[i]=='c' && c[i+1]=='-')|| (c[i]=='d' && c[i+1]=='-')|| (c[i]=='l' && c[i+1]=='j')|| (c[i]=='n' && c[i+1]=='j')|| (c[i]=='s' && c[i+1]=='=')) {
             count--;
          }
          if(c[i]=='z' && c[i+1]=='=') {
             count--;
             if(i!=0 && c[i-1]=='d') {
                count--;
             }
          }
       }
       System.out.println(count+1);
    } 
}