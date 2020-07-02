package Lesson1;

import java.util.*;

public class loop1 {


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        for ( int i=1 ; i <=10 ; i++){
            System.out.println(String.format("%d x %d = %d", N,i,N*i));
        }

        scanner.close();
    }
    
}