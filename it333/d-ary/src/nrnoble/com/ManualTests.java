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

        // int[] input = {140,130,120,110,100,90,80,70,60,5,40,30,20,10};
        // int[] input = {14,13,12,11,10,9,8,7,6,5,4,3,2,1};
         int[] input = {9,8,7,6,5,4,3,2,1};
   //      int[] input = {1,2,3,4,5,6,7,8,9,10,11,12};
     //    int[] input = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
      //   String [] input = {"a", "c", "b", "a"};
        // int[] input = {6, 22, 5, 77, 12, 11, 42, 150, 11, 11, 11};
       //  int[] input = {22,12,13,25,18,20,6,9,2,24,17,5,4,0,3,21,11,1,10,19,14,23,8,7,16,15};         // 000 001 003 002 004 006 007 008 009 010 011 013 012 014 005 015 016 017 018 019 020 021 022 023 024 025


        // int[] input = {12,11,10,9,8,7,6,5,4,3,2,1};
       // int[] input = {13,15,8,7,14,00,6,9};
       // int[] input = {8,9,0,2,13,11,7};
      //  int[] input = {5,3,1,0,4,2};
       // int[] input = {2,1,4,3,11,17,0};
        // int[] input = getRandomNumbers(25);
       //  int[] input = {25,8,32,9,5,6,14,4,11,12,3, 2, 1};

            // Broken [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 6, 12, 13, 15, 16, 17, 18, 19, 14, 20, 21, 22, 23, 24, 25]

        // Working MaryHeap Order:           [0]:01, [1]:5, [2]:02, [3]:14, [4]:12, [5]:09, [6]:6, [7]:03, [8]:19, [09]:18, [10]:23, [11]:16, [12]:15, [13]:25, [14]:20, [15]:13, [16]:22, [17]:11, [18]:10, [19]:21, [20]:08, [21]:07, [22]:24, [23]:17, [24]:04
                    // not working [0]:null, [1]:01, [2]:5, [3]:02, [4]:14, [5]:12, [6]:09, [7]:6, [8]:03, [9]:19, [10]:18, [11]:23, [12]:16, [13]:15, [14]:25, [15]:20, [16]:13, [17]:22, [18]:11, [19]:10, [20]:21, [21]:08, [22]:07, [23]:24, [24]:17
    //       int[] input = {25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1};
           //String[] input = {"z","y","x","w","v","u","t","s","r","q","p","o","n","m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"};

        dh.printHeap();

        for (int i = 0; i < input.length; i++)
        {
            System.out.print("size (" + (String.format("%03d", dh.size()) + ") " + "inserting input[" + String.format("%02d",i) + "]: " + String.format("%02d",input[i]) + "  "));
            dh.insert(input[i]);
            dh.printHeap();
        }

        System.out.println("Are element in the correct order: " + dh.verifyHeapOrder());

        MaryHeap dh2 = maryClassDump(dh);
        System.out.println();
        System.out.println();





//        System.out.println();
//        System.out.println();
//        System.out.println();
//
//        MaryHeap dh3 = maryClassDump(dh2);
//        System.out.println();
//        System.out.println();
//        MaryHeap dh4 = maryClassDump(dh3);
//        System.out.println();
//        System.out.println();
//        MaryHeap dh5 = maryClassDump(dh4);


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

            //System.out.println(dh2.getIndexOfSmallestChild(i));
            //System.out.println(dh2.getIndexOfSmallestChild2(i));
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