package nrnoble.com;
/*
* Neal Noble
* May 2017
* Assignment: Priority queue
* Instructor: Josh Archer
*/

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.Random;


public class UnitTests<T extends Comparable<T>>
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
        T result = (T) data.delMin();
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
        T result = (T)data.delMin();

        Assert.assertTrue(name + " test has failed", result != null);
        System.out.println();
    }


    @Test
    public void addTwelveElements() throws Exception
    {
        String name = new Object(){}.getClass().getEnclosingMethod().getName();
        System.out.println("running test: " + name);

        data.clear();
        Object[] randnums = getRandomNumbers(12);
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

        T value1 = (T)data.delMin();
        while (data.size() > 0)
        {
            System.out.print(value1 + " ");

            T value2 = (T)data.delMin();

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
        T LargestElement = (T) data.findMax();
        System.out.println("LargestElement = " +  LargestElement);
        T deleteElement = (T) data.delMax();
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
            if (!data.contains((T)stringData[i]))
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
        Object[] randnums = getRandomNumbers(10000);
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
    private void fillData(Object[] elements)
    {
        data.clear();
        for (int i = 0; i < elements.length ; i++)
        {
            data.insert((T)elements[i]);
        }
    }


    // fill heap with  test data
    private void fillData(String[] elements)
    {
        data.clear();
        for (int i = 0; i < elements.length ; i++)
        {
            data.insert((T)elements[i]);
        }
    }



    private Object[] getRandomNumbers(int size)
    {
        Object[] intNumbers = new Object[size];

        for (Integer i = 0; i < size; i++)
        {
            intNumbers[i] = i;
        }
        intNumbers = shuffle(intNumbers,3);
        return intNumbers;
    }


    private Object[] shuffle(Object[] testData, int shuffles)
    {
        for (int i = 0; i < shuffles ; i++)
        {
            for (int j = 0; j <testData.length ; j++)
            {
                int swap1 = randInt(0,testData.length-1);
                int swap2 = randInt(0,testData.length-1);
                Object element = testData[swap1];
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

}