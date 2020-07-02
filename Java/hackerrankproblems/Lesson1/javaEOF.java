package Lesson1;

import java.util.*;

public class javaEOF {
	public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int i =1;
        while (scan.hasNext()){
            String s = scan.nextLine();
            System.out.println(String.format("%d %s",i,s));
            i = i + 1;
		}
		scan.close();
    }

}
