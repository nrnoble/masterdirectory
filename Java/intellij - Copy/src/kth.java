import java.util.*;


public class kth
{

    public kth()
    {

    }

    public static int getHighest(int a, int b)
    {
        if (a < b)
            return b;
        else
            return a;
    }

    public static int getLowest(int a, int b)
    {
        if (a > b)
            return b;
        else
            return a;
    }



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


    public static void fifo(int k)
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
