import java.util.*;


public class kth
{

    public kth()
    {

    }

    /**
     * returns the highest value of two numbers
     * @param a any integer number
     * @param b any integer number
     * @return highest value of two numbers
     */
    public static int getHighest(int a, int b)
    {
        if (a < b)
            return b;
        else
            return a;
    }

    /**
     * returns the lowest value of two numbers
     * @param a any integer number
     * @param b any integer number
     * @return lowest value of two numbers
     */
    public static int getLowest(int a, int b)
    {
        if (a > b)
            return b;
        else
            return a;
    }


    /**
     * generates random numbers, then prints out the
     * highest random number, then the lowest random number
     */
    public static void findHighLow()
    {
        int highest = 0;
        int lowest = 101;

        List<Integer> randomNumbers = getRandomNumbers(25,1,100);

        for (Integer i : randomNumbers)
        {
            highest = getHighest(highest,i);
            lowest = getLowest(lowest,i);
        }

        System.out.println("highest: " + highest);
        System.out.println("lowest: " + lowest);
        System.out.println();

        int counter = 0;
        for (Integer i : randomNumbers)
        {
            System.out.println(counter++ +": " + i);
        }


    }

    /**
     * Generates random numbers between a lowerRange and upperRange
     * @param total number of random number to be generated
     * @param lowerRange lowest possible random number
     * @param upperRange highest possible random number
     * @return random numbers as a List of <integer>
     */
    public static List<Integer> getRandomNumbers(int total,int lowerRange, int upperRange)
    {
        List<Integer> list = new ArrayList<Integer>();
        Random rnd = new Random();
        for (int i = 0; i <= total; i++)
        {
            list.add(rnd.nextInt((upperRange - lowerRange) + 1) + lowerRange);
        }
        return list;
    }


    /**
     * No fully implemented.
     * First in, First out
     * @param k
     */
    public static void fifo1(int k)
    {
        List<Integer> list = new ArrayList<Integer>();
        PriorityQueue <Integer>  prq = new PriorityQueue<Integer>(k);
        Random rnd = new Random();
        int randomNum = rnd.nextInt(100);
        prq.add(randomNum);
        System.out.println("Adding first to que: " + randomNum);

        for (int i = 0; i <= 25; i++)
        {
            int nextRandomNum = rnd.nextInt(100);
            if (randomNum <= nextRandomNum)
            {
                System.out.println("Adding: " + nextRandomNum);
                prq.add(nextRandomNum);
                randomNum = nextRandomNum;
            }
            else
            {
                System.out.println("dropping: " + nextRandomNum);
            }

        }

        int count = 0;
        for (Integer i : prq)
        {

            System.out.println(count++ + ": " +i);
        }


    }



    /**
     * Find the kth largest value in a list of random numbers
     * @param kth largest number
     */
    public static void Sort(int kth)
    {
        System.out.println();
        System.out.println("<---------- Exercise Question #1 Start ---------->");
        List<Integer> list = new ArrayList<Integer>();
        Random rnd = new Random();
        for (int i = 0; i <= 25; i++)
        {
            list.add(rnd.nextInt(100));
        }


        Collections.sort(list);

        int item = 0;
        for (Integer i : list) {
            System.out.println(item++ + " " + i);
        }

        System.out.println(list.get(kth));
        System.out.println("<---------- Exercise Question #1 end ---------->");
        System.out.println();
    }

}
