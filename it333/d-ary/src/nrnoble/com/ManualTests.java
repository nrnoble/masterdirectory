package nrnoble.com;

import java.util.Random;

/** Class ManualTests **/
public class ManualTests
{
    private static Random rand = new Random();
    public static void main(String[] args)
    {

        MaryHeap dh = new MaryHeap(10,3);
       // MarryHeap<Integer> dh = new MarryHeap<>();

        //   int[] input = {9,8,7,6,5,4,3,2,1};
        //   int[] input = {1,2,3,4,5,6,7,8,9,10,11,12};
        //   String [] input = {"a", "c", "b", "a"};

         int[] input = getRandomNumbers(12);

        for (int i = 0; i < input.length; i++)
        {
            System.out.print("size (" + (String.format("%03d", dh.size()) + ") " + "inserting input[" + String.format("%02d",i) + "]: " + String.format("%02d",input[i]) + "  "));
            dh.insert(input[i]);
            dh.printHeap();
        }

        System.out.println("Are element in the correct order: " + dh.verifyHeapOrder());


        System.out.println();
        System.out.println();

        maryClassDump(dh);

    }


    private static int[] getRandomNumbers(int size)
    {
        int[] intNumbers = new int[size+1];

        for (Integer i = 1; i <= size; i++)
        {
            intNumbers[i] = i;
        }
        intNumbers = shuffle(intNumbers,3);
        return intNumbers;
    }


    private void listsmallChild(MaryHeap dh2)
    {
        for (int i = 0; i < dh2.size()-1 ; i++)
        {
            System.out.println(" dh2.getIndexOfSmallestChild(i): " + String.format("%03d", dh2.getIndexOfSmallestChild(i))  +" (" + String.format("%03d", dh2.data[dh2.getIndexOfSmallestChild(i)]  )+ ") ");
            System.out.println("dh2.getIndexOfSmallestChild2(i): " + String.format("%03d", dh2.getIndexOfSmallestChild2(i)) +" (" + String.format("%03d", dh2.data[dh2.getIndexOfSmallestChild2(i)]  ) + ") ");
            System.out.println();
        }
    }



    private static int[] shuffle(int[] testData, int shuffles)
    {
        for (int i = 0; i < shuffles ; i++)
        {
            for (int j = 0; j <testData.length ; j++)
            {
                int swap1 = randInt(0,testData.length-1);
                int swap2 = randInt(0,testData.length-1);
                int element = testData[swap1];
                testData[swap1] = testData[swap2];
                testData[swap2] = element;
            }

        }
        return testData;
    }



    public static int randInt(int min, int max) {

        int randomNum = rand.nextInt((max - min) + 1) + min;
        return randomNum;
    }

    public static MaryHeap maryClassDump (MaryHeap heap)
    {
        System.out.println("heap");
        int lineCount = 0;
        int previous = (int) heap.peek();
        MaryHeap dh2 = new MaryHeap(10,3);
        while (!heap.isEmpty())
        {
            int result = (int) heap.delMin();
            dh2.insert(result);
            System.out.print(String.format("%03d", ++lineCount) + " Pulling: " + String.format("%03d",result )  + "   ");
            //  System.out.print(String.format("%03d", result )  + " ");
            heap.printHeap();

            if (previous >  result)
            {
                System.out.println("    ERROR previous " + previous + " > " +  result + " result");
                previous = result;
            }
            else
            {
                previous = result;
            }
        }
        return dh2;
    }


}