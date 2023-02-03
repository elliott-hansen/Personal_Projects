import java.util.*;
import java.util.Arrays;

public class Kaprekar
{
    public static int[] toArray(String str)
    {
            int[] chars = {0, 0, 0, 0};
            int b = 0;
            for(char i : str.toCharArray())
            {
                chars[b] = i;
                b += 1;
            }
            return chars;
    }

    public static String kapr(String input)
    {
        int[] chars = toArray(input);
        System.out.println("Input of: "+input);
        Arrays.sort(chars);
        int small = Integer.parseInt(Arrays.toString(chars));
        System.out.println("Small: "+small);
        Collections.reverse(Arrays.asList(chars));
        int big = Integer.parseInt(Arrays.toString(chars));
        System.out.println("Big: "+big);
        System.out.println("Difference: "+(big-small));
        return Integer.toString(big-small);
    }
    public static void main(String[] args)
    {
        Scanner Inputs = new Scanner(System.in);
        System.out.println("Enter a 4-digit number without repeating the same four digits:");
        String FirstNumber = Inputs.nextLine();
        Inputs.close();
        kapr(FirstNumber);


    }

}