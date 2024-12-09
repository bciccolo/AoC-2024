import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Day1
{
    private static final String FILE = "day1.dat";

    public static void main(String[] args)
    {
        try
        {
            ArrayList<Integer> left = new ArrayList<Integer>(1000);
            ArrayList<Integer> right = new ArrayList<Integer>(1000);

            // Load the data into the 'left' and 'right' lists
            Scanner input = new Scanner(new File(FILE));
            while (input.hasNextLine())
            {
                String line = input.nextLine();
                String[] parts = line.split("\\s+");
                left.add(Integer.parseInt(parts[0]));
                right.add(Integer.parseInt(parts[1]));
            }
            input.close();

            // Sort the 'left' and 'right' lists
            Collections.sort(left);
            Collections.sort(right);

            // Calculate the distance between each pair
            int distance = 0;
            for (int i = 0; i < left.size(); i++)
            {
                distance += Math.abs(left.get(i) - right.get(i));
            }

            System.out.println(distance);
        } catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}