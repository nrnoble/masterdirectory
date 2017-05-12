// Neal R Noble
// IT333
// April 2016
// week_3_Algorithm Analysis

public class Algorithm_3 extends BaseAlgorithmClass
{


    public Algorithm_3(int[] _testData)
    {
        super(_testData);
        this.algorithmName = "algorithm#3";

    }
    // Instructions:
    // Fill the array such that a[i] = i +1. Then:
    //  for(int i = 1; i < n; i++)
    //  {
    //    swapElements(a[i], a[randint(0, i)]);
    //  }
    @Override
    public int algorithm(int _n)
    {
        int counter = 0;                                            // counter++;
        int[] randomNumbers = new int[_n];                          // counter++;
        for (int i = 0; i < _n; i++)
        {                                                           // counter++;
            randomNumbers[i] = i + 1;                               //counter++;
        }

        for (int i = 0; i < _n; i++)
        {
            int randomPosition = Utils.randInt(0, _n - 1);           counter++;
            int currentNumber = randomNumbers[i];                   // counter++;
            randomNumbers[i] = randomNumbers[randomPosition];       // counter++;
            randomNumbers[randomPosition] = currentNumber;          // counter++;
        }
        return counter;
    }
}
