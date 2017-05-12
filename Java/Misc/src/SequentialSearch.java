/**
 * Created by Neal on 5/4/2016.
 */
public class SequentialSearch
{


    public static boolean find (Integer[] myarray, Integer _num)
    {
        for (int i = 0; i < myarray.length ; i++)
        {
            if (myarray[i] == _num)
                return true;

        }
        return false;
    }
}
