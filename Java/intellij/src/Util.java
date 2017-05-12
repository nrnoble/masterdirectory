import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * Created by Neal on 3/29/2016.
 */
public class Util
{


    public static List<Integer> getRandomNumbers(int total, int lowerRange, int upperRange)
    {
        List<Integer> list = new ArrayList<Integer>();
        Random rnd = new Random();
        for (int i = 0; i <= total; i++) {
            list.add(rnd.nextInt((upperRange - lowerRange) + 1) + lowerRange);
        }
        return list;
    }
}