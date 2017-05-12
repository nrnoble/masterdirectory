/**
 * Created by Neal on 5/4/2016.
 */
public class findVowels
{


    public static void printVowels(String[] vowels, String[] alpha)
    {
        for (int i = 0; i < vowels.length; i++)
        {
            for (int j = 0; j < alpha.length; j++)
            {
                if (vowels[i] == alpha[j])
                {
                    System.out.println(vowels[i]);
                }
            }
        }
    }
}
