/**
 * Created by Neal on 4/14/2016.
 */
public class BaseAlgorithmClass
{

    private int n = 10;
    private int counter;
    private int[] testData = null;
    public String algorithmName = "algorithmName1bas";

    public BaseAlgorithmClass()
    {
        super();
    }

    public BaseAlgorithmClass(String _algorithmName)
    {
        super();
        this.algorithmName = _algorithmName;
    }


    public BaseAlgorithmClass(int[] _testData)
    {
        this.testData = _testData;

    }



    public int algorithm(int _n)
    {

        return this.counter;
    }


    public long testLoop_b(int _integrations, int _n)
    {
        int total = 0;
        for (int i = 0; i < _integrations; i++)
        {
            total = total + this.algorithm(_n);
        }


        long executionSteps = total / _integrations;
        System.out.println(this.algorithmName
                + "(n=" +  _n +", Test loop x"
                + _integrations
                + ") average execution steps: " + executionSteps);

        return executionSteps;

    }

    public long testLoop_c()
    {
        long total = 0;
        long executionSteps = 0;
        for (int index = 0; index <testData.length ; index++)
        {
            this.testLoop_b(this.n,testData[index]);
        }
        return executionSteps;

    }



}
