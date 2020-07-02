package Lession1;

import java.util.*;
/*
 * my first program
 */
public class MyClass {

	 public static void main(String []argh){
	        Scanner in = new Scanner(System.in);
	        System.out.print(Math.pow(2, 2));
	        int t=in.nextInt();
	        for(int i=0;i<t;i++){
	            int a = in.nextInt();
	            int b = in.nextInt();
	            int n = in.nextInt();
	            int seqval=a;
	            for ( int j =0; j< n ;j++){
	                seqval = seqval + b * (2^j);
	                System.out.print(seqval + ' ');
	            }
	            
	        }
	        in.close();
	    }

}
