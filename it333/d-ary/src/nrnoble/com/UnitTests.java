package nrnoble.com;

import static org.junit.Assert.*;

import java.util.Random;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;


public class UnitTests //<T extends Comparable<T>>
{
    private String[] stringData = {"z","y","x","w","v","u","t","s","r","q","p","o","n","m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"};
    private static Random rand = new Random();
    private MaryHeap data;

    @Before
    public void setup()
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running: " + name);

         data = new MaryHeap(10,3);
    }



    @Test
    public void sizeIsEmpty() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();

        System.out.println("running test: " + name);
        data.clear();

        Assert.assertTrue(name + " test has failed", data.size() == 0);
        System.out.println();
    }


    @Test
    public void sizeIsNotEmpty() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        data.clear();
        // add some elements
        int numberOfElements = 100;
        this.fillData(numberOfElements);

        Assert.assertTrue(name + " test has failed", data.size() == numberOfElements);
        System.out.println();
    }


    @Test
    public void clear() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        data.clear();

        Assert.assertTrue(name + " test has failed", data.isEmpty());
        System.out.println();
    }



    @Test
    public void peek() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        data.peek();

        Assert.assertTrue(name + " test has failed", data.isEmpty());
        System.out.println();
    }



    // Calling insert() on an initially empty tree.
    @Test
    public void emptyInsert() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        data.clear();
        int numberOfElements = data.size();

        int addMore = 100;
        for (int i = 0; i < addMore ; i++)
        {
            data.insert(i);
        }

        numberOfElements += addMore;

        Assert.assertTrue(name + " test has failed", numberOfElements == data.size());
        System.out.println();

    }


    // Calling insert() on an initially non-empty tree.
    @Test
    public void non_EmptyInsert() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        emptyInsert();

        int numberOfElements = data.size();

        int addMore = 100;
        for (int i = 0; i < addMore ; i++)
        {
            data.insert(i);
        }

        numberOfElements += addMore;

        Assert.assertTrue(name + " test has failed", numberOfElements == data.size());
        System.out.println();
    }

    // Call delMin() on an empty tree.
    @Test
    public void delMinOnEmptyTree() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        data.clear();
        Object result = (Object) data.delMin();
        Assert.assertTrue(name + " test has failed", result == null);
        System.out.println();
    }

    // Call delMin() on a non empty tree.
    @Test
    public void delMinOnNonEmptyTree() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        non_EmptyInsert();
        Object result = (Object)data.delMin();

        Assert.assertTrue(name + " test has failed", result != null);
        System.out.println();
    }


    @Test
    public void addTwelveElements() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        data.clear();
        Integer[] randnums = getRandomNumbers(12);
        this.fillData(randnums);

        for (int i = 0; i < randnums.length ; i++)
        {
            //System.out.println("randnums[" + i + "] " + randnums[i]);
           if (!data.contains(i))
           {
               System.out.println("Missing: randnums[" + i + "]: " + randnums[i]);
               Assert.assertTrue(name + " test has failed", false);
           }
        }

        Integer value1 = (Integer)data.delMin();
        while (data.size() > 0)
        {
            System.out.print(value1 + " ");

            Integer value2 = (Integer)data.delMin();

            if (value2.compareTo(value1) < 0)
            {
                System.out.println("Fail: " + value2 + " < " + value1 );
                Assert.assertTrue(name + " test has failed", false);
            }
            value1 = value2;
        }

        System.out.println();
    }

    // Delete the largest element
    @Test
    public void deleteLargestElement() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        non_EmptyInsert();
        System.out.println("running test: " + name);
        Integer LargestElement = (Integer) data.findMax();
        System.out.println("LargestElement = " +  LargestElement);
        Integer deleteElement = (Integer) data.delMax();
        System.out.println("deleteElement = " +  deleteElement);

        Assert.assertTrue(name + " test has failed", LargestElement.compareTo(deleteElement) ==  0);
        System.out.println();
    }


    //Verify A-Z elements
    @Test
    public void containsAlphabet() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        data.clear();
        this.fillData(stringData);
        for (int i = 0; i < stringData.length ; i++)
        {
            if (!data.contains((String)stringData[i]))
            {
                System.out.println("stringData[" + i + "]: " + stringData[i]);
                Assert.assertTrue(name + " test has failed", false);
                break;
            }


        }

        System.out.println();
    }

    @Test
    public void insert10KElements() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);
        data.clear();
        Integer[] randnums = getRandomNumbers(10000);
        this.fillData(randnums);
       // fillData(10000);
        if (data.size() != 10000)
        {
            Assert.assertTrue(name + " test has failed", false);
        }

        System.out.println();
    }

    // Insert 1 million elements and verify size
    @Test
    public void MillionElements() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);
        data.clear();

        fillData(1000000);
        if (data.size() != 1000000)
        {
            Assert.assertTrue(name + " test has failed", false);
        }
        System.out.println();
    }

    // Verify that an element does not exist after after deletion
    @Test
    public void doesNotContain() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        data.clear();
        this.fillData(stringData);
        if (!data.contains("k"))
        {
            Assert.assertTrue(name + " test has failed", false);
        }

        int elementIndex = data.findElementIndex("k");
        data.delete(elementIndex);

        if (data.contains("k"))
        {
            Assert.assertTrue(name + " test has failed", false);
        }

        System.out.println();
    }

    @Test
    public void VerifySortOrder1MillElements() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        data.clear();
        MillionElements();
        data.verifyHeapOrder();
    }



    //Verify A-Z elements
    @Test
    public void AlphabetInSortedOrder() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        data.clear();
        this.fillData(stringData);
        String previous = (String)data.delMin();
        System.out.print(previous + " ");
        while (!data.isEmpty())
        {
            String next = (String)data.delMin();
            System.out.print(next + " ");
            if (next.compareTo(previous) < 0)
            {
                Assert.assertTrue(name + " test has failed", false);
                return;
            }

            previous = next;


        }

        System.out.println();
        System.out.print(name + " test has passed");
        System.out.println();
        System.out.println();

    }



    /// Private Test Helpers ///

    // fill heap with interger test data
    private void fillData(int size)
    {
        data.clear();;
        for (int i = 0; i < size ; i++)
        {
            data.insert(i);
        }
    }



    // fill heap with  test data
    private void fillData(Integer[] elements)
    {
        data.clear();
        for (int i = 0; i < elements.length ; i++)
        {
            data.insert((Integer)elements[i]);
        }
    }


    // fill heap with  test data
    private void fillData(String[] elements)
    {
        data.clear();
        for (int i = 0; i < elements.length ; i++)
        {
            data.insert(elements[i]);
        }
    }



    private Integer[] getRandomNumbers(int size)
    {
        Integer[] intNumbers = new Integer[size];

        for (Integer i = 0; i < size; i++)
        {
            intNumbers[i] = i;
        }
        intNumbers = shuffle(intNumbers,3);
        return intNumbers;
    }


    private Integer[] shuffle(Integer[] testData, Integer shuffles)
    {
        for (int i = 0; i < shuffles ; i++)
        {
            for (int j = 0; j <testData.length ; j++)
            {
                //int swap1 = randInt(0,testData.length-1);
                Integer swap2 = randInt(0,testData.length-1);
                Integer element = testData[j];
                testData[j] = testData[swap2];
                testData[swap2] = element;
            }

        }
        return testData;
    }


    public static int randInt(int min, int max) {

        int randomNum = rand.nextInt((max - min) + 1) + min;
        return randomNum;
    }

}