// Neal R Noble
// IT333
// April 2016
// week_3_Algorithm Analysis


public class Algorithm_1 extends BaseAlgorithmClass
{


    public Algorithm_1()
    {
        super("Algorithm#1");
    }

    public Algorithm_1(int[] _testData)
    {
        super(_testData);
        this.algorithmName = "algorithm#1";
    }

    // Instructions:
    // Fill the array a from a[0] to a[n-1] as follows: To fill a[i], generate random numbers
    // until you get one that is not already in a[0], a[1], … a[i-1].
    @Override
    public int algorithm(int _n)
    {
        int faults = 0;
        int counter = 0;
        int[] randomNumbers = new int[_n];
        for (int i = 0; i < _n ; i++)
        {

            int randomNumber = Utils.randInt(1,_n);
            int index = 0;

            while (index <= i)
            {
                                                                    counter++;
                if (randomNumber == randomNumbers[index])
                {

                    index = 0;
                    randomNumber = Utils.randInt(1,_n);
                    continue;
                }
                else
                {
                    faults++;
                    index++;
                }
            }
            randomNumbers[i] = randomNumber;
        }
        return counter;
    }



}
