// Neal R Noble
// IT333
// April 2016
// week_3_Algorithm Analysis

public class Algorithm_2 extends BaseAlgorithmClass
{



    public Algorithm_2(int[] _testData)
    {
        super(_testData);
        this.algorithmName = "algorithm#2";

    }

    // Instructions:
    // Same as algorithm (1), but keep an extra array called the used When a random number, ran
    // is first put in the array a, set used[ran] = true. This means that when filling a[i]
    // with a random number, you can test in one step to see whether the random number has been
    // used, instead of the (possibly) i steps in the first algorithm.
    @Override
    public int algorithm(int _n)
    {

        int counter = 0;
        int[] randomNumbers = new int[_n];
        boolean[] used = new boolean[_n];
        int index = 0;

        while (index < _n)
        {
                                                                        counter++;
            int randomNumber = Utils.randInt(1,_n);
            if (used[randomNumber - 1] != true)
            {

                used[randomNumber - 1] = true;
                randomNumbers[index++] = randomNumber;
            }
        }
        return counter;
    }


}
