package Lesson1;

import java.util.Scanner;

public class outformatting {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("================================");
        for(int i=0;i<3;i++){
            String s1=sc.next();
            int x=sc.nextInt();
            System.out.print(String.format("%-15s",s1));
            System.out.println(String.format("%03d", x));
            //Complete this line
        }
        System.out.println("================================");
        sc.close();
    }
    
}