import java.util.Scanner;

//A function to find the greatest commom divisor between two numbers
public class euclidian{
    public static int euclad(int x, int y){
        int r;
        while(y!=0){
            r = x % y;
            x = y;
            y = r; 
        }
        return x;
    }

    public static void main(String[] args){
        int x,y;
        Scanner input = new Scanner(System.in);
        System.out.println("Input 2 integers: ");
        x = Math.abs(input.nextInt());//taking only absolute numbers
        y = Math.abs(input.nextInt());
        int gcd = euclad(x,y);
        System.out.print("The gcd of\t" +x+ "\tand\t" +y+ "is\t"+gcd);
    }
}