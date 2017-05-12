import java.util.Arrays;
import java.util.List;

/**
 * Created by Neal on 3/29/2016.
 */
public class Excercise4
{

    public static void filterRandomNumb()
    {

        System.out.println();
        System.out.println("<---------- Exercise Question #4 Start ---------->");
        List<Integer> randomNums = Util.getRandomNumbers(20,0,9);
        int[] filtered = new int[10];


        for (Integer i:randomNums) 
        {
            filtered[i]++;
        }

        for (int i = 0; i < filtered.length ; i++) 
        {
            System.out.print(i + "'s[" + filtered[i] + "]");
            if  (filtered[i] >0)
            {
                for (int j = 1; j <= filtered[i]; j++)
                {
                    System.out.print("," + i);
                }
                System.out.println();
            }
            else
            {
                System.out.println();
            }
        }
        System.out.println("<---------- Exercise Question #4 finished ---------->");
    }


}

