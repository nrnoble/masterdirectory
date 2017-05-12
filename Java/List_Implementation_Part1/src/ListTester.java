import java.util.Iterator;

public class ListTester
{
    public static void main(String[] args)
    {

    }

    public static boolean testAdd(EmptyArrayList<String> myList)
    {

        boolean testpass = true;
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data and verify list object has
        // been properly intialized.
        if (testClear(myList) == false)
            failCount++;

        // TEST: add a simple value and verify that it exists at the next index
        myList.add("A");
        if (myList.size() != 1)
            failCount++;
        if (myList.get(0) != "A")
            failCount++;

        // TEST: add a simple value and verify that it exists at the next index
        myList.add("B");
        if (myList.size() != 2)
            failCount++;
        if (myList.get(1) != "B")
            failCount++;

        // TEST: add a simple value and verify that it exists at the next index
        myList.add("C");
        if (myList.size() != 3)
            failCount++;
        if (myList.get(2) != "C")
            failCount++;


        // TEST: add the same value three times and verify that it exists at the next index
        myList.add("A");
        myList.add("A");
        myList.add("A");
        if (myList.size() != 6)
            failCount++;
        if (myList.get(5) != "A")
            failCount++;


        if (failCount == 0)
        {
            System.out.println("All \"add\" tests have passed");
            return true;
        }
        System.out.println("Failed \"add\" tests: " + failCount );
        return false;
    }


    public static boolean testInsert(EmptyArrayList<String> myList)
    {

        boolean testpass = true;
        int failCount =  0;


        // TEST: Call testAdd() to wipe existing data, verify list object has
        // been properly intialized, and method Add() passes all tests
        if (testAdd(myList) == false)
            failCount++;

        int currentElementCount = myList.size();


        // TEST. Enter invalid index.
        // this test is expected to throw an error
        try
        {
            failCount++;
            myList.add(-1,"b");

        } catch (Exception e)
        {
            failCount--;
            currentElementCount++;
            myList.add(1,"a");
        }


        // TEST: Add an element, check size, check if element is located at the correct index
        myList.add(0,"TEST: Add an element, check size, check if element is located at the correct index");
        if (myList.size() != ++currentElementCount)
            failCount++;
        if (myList.get(0) != "TEST: Add an element, check size, check if element is located at the correct index")
            failCount++;


        // TEST: Add an element, check size, check if element is located at the correct index
        myList.add(1,"100");
        if (myList.size() != ++currentElementCount)
            failCount++;
        if (myList.get(1) != "100")
            failCount++;


        // TEST: Add an element, check size, check if element is located at the correct index
        myList.add(2,"12314361@#$%!@+_)(");
        if (myList.size() != ++currentElementCount)
            failCount++;
        if (myList.get(2) != "12314361@#$%!@+_)(")
            failCount++;


        //TEST: invalid range. This is expected to throw an error
        try
        {
            failCount++;
            myList.add(100,"should fail");
        }
        catch (Exception e)
        {
            failCount--;
        }


        if (failCount == 0)
        {
            System.out.println("All \"testInsert\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testInsert\" tests: " + failCount );

        return false;
    }


    public static boolean testIsEmpty(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        int failCount =  0;

        // Test Clear all data
        myList.clear();
        if (myList.isEmpty() != true || myList.size() != 0)
            failCount++;

        // Add one element
        myList.add("TestData");
        if (myList.isEmpty() == true && myList.size() == 0)
            failCount++;

        // remove the only element in list
        myList.remove(0);
        if (myList.isEmpty() != true || myList.size() != 0)
            failCount++;


        // Add one element back
        myList.add("TestData");
        if (myList.isEmpty() == true && myList.size() == 0)
            failCount++;


        // Search and then remove the only element
        myList.remove("TestData");
        if (myList.isEmpty() != true && myList.size() != 0)
            failCount++;


        if (failCount == 0)
        {
            System.out.println("All \"testIsEmpty\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testIsEmpty\" tests: " + failCount );

        return false;
    }


    public static boolean testSize(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData = "Some test data 123123 58734583!@#$%^&*(+";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;

        //TEST: Check size. Verify size value is zero.
        if (myList.size() != 0)
            failCount++;

        //TEST: Add 1 element, check of size is incremented by 1
        myList.add("test data");
        if (myList.size() != 1)
            failCount++;

        //TEST: call clear() and verify size is zero
        myList.clear();
        if (myList.size() != 0)
            failCount++;

        //TEST: Add 1 element, check of size is incremented by 1
        myList.add("test data");
        if (myList.size() != 1)
            failCount++;

        //TEST: call remove("test data") and verify size is zero
        myList.remove("test data");
        if (myList.size() != 0)
            failCount++;


        //TEST: Add 1 element, check of size is incremented by 1
        myList.add("test data");
        if (myList.size() != 1)
            failCount++;

        //TEST: call remove(0) and verify size is zero
        myList.remove(0);
        if (myList.size() != 0)
            failCount++;

        //TEST: Add 100 elements, verify size = 100
        for (int i = 0; i < 100 ; i++)
        {
            myList.add("test data");
            if (myList.size() != i+1)
                failCount++;
        }



        if (failCount == 0)
        {
            System.out.println("All \"testSize\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testSize\" tests: " + failCount );

        return false;
    }


    public static boolean testClear(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData = "Some test data 123123 58734583!@#$%^&*(+";
        int failCount =  0;

        // TEST: Add some data and make sure the size returns a value greater than zero
        // This will ensure there that the clear() method is clearing existing data.
        myList.add(testData);
        if (myList.size() <=0 )
            failCount++;

        //TEST: Clear all data, check size
        myList.clear();
        if (myList.size() !=0 )
            failCount++;

        //TEST: isEmpty
        if (!myList.isEmpty() )
            failCount++;

        //TEST: Verify than a new element can be added after clearing data
        myList.add(testData);
        if (myList.size() <= 0)
            failCount++;

        //TEST: Verify new element can be located
        if (!myList.contains(testData))
            failCount++;

        //TEST: Clear all data again, check size
        myList.clear();
        if (myList.size() !=0 )
            failCount++;


        //TEST: Call Clear() mutliple times to testing for possible logic errors in var increments
        for (int i = 0; i < 100 ; i++)
        {
            myList.clear();
            if (myList.size() !=0)
                failCount++;
        }


        if (failCount == 0)
        {
            System.out.println("All \"testClear\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testClear\" tests: " + failCount );

        return false;
    }


    public static boolean testIndexOf(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData = "Some test data 123123 58734583!@#$%^&*(+";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;

        //TEST: Add some testdata and verify size
        myList.add(testData);
        if (myList.size() != 1)
            failCount++;

        //TEST: Verify that index of test data
        if (myList.indexOf(testData) !=0)
            failCount++;

        //TEST: Add more test data and verify size
        myList.add(testData);
        myList.add(testData);
        myList.add(testData);
        if (myList.size() != 4)
            failCount++;

        //TEST: Verify that index of test data
        if (myList.indexOf(testData) !=0)
            failCount++;


        // TEST: Verify failure to find data that is not in list
        // expected result is the return value of -1
        if (myList.indexOf(testData + "123") != -1)
            failCount++;


        if (failCount == 0)
        {
            System.out.println("All \"testIndexOf\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testIndexOf\" tests: " + failCount );

        return false;

    }


    public static boolean testContains(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData = "Some test data 123123 58734583!@#$%^&*(+";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;

        //TEST: Add some testdata and verify size
        myList.add(testData);
        if (myList.size() != 1)
            failCount++;

        if (!myList.contains(testData))
            failCount++;

        //TEST: Add more test data and verify size
        myList.add(testData);
        myList.add(testData);
        myList.add(testData);
        if (myList.size() != 4)
            failCount++;


        //TEST: Verify that index of test data
        if (!myList.contains(testData))
            failCount++;

        //TEST: Remove one of elements, and verify list still contains test data.
        myList.remove(testData);
        if (myList.size() != 3)
            failCount++;

        //TEST: Verify list still contains test data.
        if (!myList.contains(testData))
            failCount++;


        //TEST: remove all test data and verify test data can be found
        myList.remove(testData);
        myList.remove(testData);
        myList.remove(testData);
        if (myList.size() != 0)
            failCount++;

        //TEST: Verify list still contains test data.
        if (myList.contains(testData))
            failCount++;



        if (failCount == 0)
        {
            System.out.println("All \"testContains\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testContains\" tests: " + failCount );

        return false;
    }


    public static boolean testGet(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData0 = "Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "Some test data 123123 58734583!@#$%^&*(+2";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;

        //TEST: Add testdata2 and verify size
        myList.add(testData0);
        if (myList.size() != 1)
            failCount++;
        //TEST: Add testdata1 and verify size
        myList.add(testData1);
        if (myList.size() != 2)
            failCount++;

        //TEST: Add testdata2 and verify size
        myList.add(testData2);
        if (myList.size() != 3)
            failCount++;

        //TEST: Verify index of testData0
        if (myList.get(0) != testData0)
            failCount++;

        //TEST: Verify index of testData1
        if (myList.get(1) != testData1)
            failCount++;

        //TEST: Verify index of testData2
        if (myList.get(2) != testData2)
            failCount++;


        //TEST remove testData1. Verify index of testdata2
        myList.remove(testData1);
        if (myList.size() != 2)
            failCount++;

        //TEST: Verify index of testData2 has changed
        if (myList.get(1) != testData2)
            failCount++;


        if (failCount == 0)
        {
            System.out.println("All \"testGet\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testGet\" tests: " + failCount );

        return false;
    }


    public static boolean testSet(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData0 = "Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "Some test data 123123 58734583!@#$%^&*(+2";
        String testData3 = "Some test data 123123 58734583!@#$%^&*(+3";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;

        //TEST: Add testdata2 and verify size
        myList.add(testData0);
        if (myList.size() != 1)
            failCount++;
        //TEST: Add testdata1 and verify size
        myList.add(testData1);
        if (myList.size() != 2)
            failCount++;

        //TEST: Add testdata2 and verify size
        myList.add(testData2);
        if (myList.size() != 3)
            failCount++;

        //TEST remove testData1. Verify index of testdata2
        myList.remove(testData1);
        if (myList.size() != 2)
            failCount++;

        //TEST: Verify index of testData2 has changed
        if (myList.get(1) != testData2)
            failCount++;

        //TEST set index1 = testData3
        if (myList.set(1,testData3) != testData3)
            failCount++;

        //TEST: Verify index1 = testData3
        if (myList.get(1) != testData3)
            failCount++;


        //this method tests list.set(index, element)

        if (failCount == 0)
        {
            System.out.println("All \"testSet\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testSet\" tests: " + failCount );

        return false;

    }


    public static boolean testRemoveElement(EmptyArrayList<String> myList)
    {
        boolean testpass = true;

        String testData0 = "Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "Some test data 123123 58734583!@#$%^&*(+2";
        String testData3 = "Some test data 123123 58734583!@#$%^&*(+3";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;

        // TEST run all testGet tests
        if (!testGet(myList))
            failCount++;

        // TEST run all testSet tests
        if (!testGet(myList))
            failCount++;

        if (testClear(myList) == false)
            failCount++;

        //TEST: Add testdata2 and verify size
        myList.add(testData0);
        if (myList.size() != 1)
            failCount++;
        //TEST: Add testdata1 and verify size
        myList.add(testData1);
        if (myList.size() != 2)
            failCount++;

        //TEST: Add testdata2 and verify size
        myList.add(testData2);
        if (myList.size() != 3)
            failCount++;

        //TEST remove testData1. Verify index of testdata2
        myList.remove(testData0);
        if (myList.size() != 2)
            failCount++;

        //TEST remove testData1. Verify index of testdata1
        myList.remove(testData1);
        if (myList.size() != 1)
            failCount++;

        //TEST remove testData2. Verify index of testdata2
        myList.remove(testData2);
        if (myList.size() != 0)
            failCount++;


        if (failCount == 0)
        {
            System.out.println("All \"testRemoveElement\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testRemoveElement\" tests: " + failCount );

        return false;
    }


    public static boolean testRemoveIndex(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData0 = "Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "Some test data 123123 58734583!@#$%^&*(+2";
        String testData3 = "Some test data 123123 58734583!@#$%^&*(+3";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;


        // TEST run all testGet tests
        if (!testGet(myList))
            failCount++;

        // TEST run all testSet tests
        if (!testGet(myList))
            failCount++;


        if (testClear(myList) == false)
            failCount++;


        //TEST: Add testdata2 and verify size
        myList.add(testData0);
        if (myList.size() != 1)
            failCount++;
        //TEST: Add testdata1 and verify size
        myList.add(testData1);
        if (myList.size() != 2)
            failCount++;

        //TEST: Add testdata2 and verify size
        myList.add(testData2);
        if (myList.size() != 3)
            failCount++;

        //TEST remove testData1. Verify index of testdata2
        myList.remove(1);
        if (myList.size() != 2)
            failCount++;

        //TEST remove testData1. Verify index of testdata1
        myList.remove(1);
        if (myList.size() != 1)
            failCount++;

        //TEST remove testData2. Verify index of testdata2
        myList.remove(1);
        if (myList.size() != 0)
            failCount++;


        if (failCount == 0)
        {
            System.out.println("All \"testRemoveIndex\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testRemoveIndex\" tests: " + failCount );

        return false;


    }


    public static boolean testRemoveAll(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData0 = "Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "Some test data 123123 58734583!@#$%^&*(+2";
        String testData3 = "Some test data 123123 58734583!@#$%^&*(+3";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;


        // TEST run all testGet tests
        if (!testGet(myList))
            failCount++;

        // TEST run all testSet tests
        if (!testGet(myList))
            failCount++;


        if (testClear(myList) == false)
            failCount++;


        //TEST: Add testdata0 and verify size
        myList.add(testData0);
        if (myList.size() != 1)
            failCount++;
        //TEST: Add testdata1 and verify size
        myList.add(testData1);
        if (myList.size() != 2)
            failCount++;

        //TEST: Add testdata2 and verify size
        myList.add(testData2);
        if (myList.size() != 3)
            failCount++;

        //TEST: Add testdata3 and verify size
        myList.add(testData3);
        if (myList.size() != 4)
            failCount++;

        // create an list if items that will be removed from myList
        EmptyArrayList removeListItem = new EmptyArrayList();
        removeListItem.add(testData2);
        removeListItem.add(testData3);

        // check count to verify two elements have been remove d
        myList.removeAll(removeListItem);
        if (myList.size() != 2)
            failCount++;

       if  (myList.contains(testData2))
           failCount++;

        if  (myList.contains(testData3))
            failCount++;


        if (failCount == 0)
        {
            System.out.println("All \"testRemoveAll\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testRemoveAll\" tests: " + failCount );

        return false;


    }


    public static boolean testContainsAll(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData0 = "Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "Some test data 123123 58734583!@#$%^&*(+2";
        String testData3 = "Some test data 123123 58734583!@#$%^&*(+3";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;


        // TEST run all testGet tests
        if (!testGet(myList))
            failCount++;

        // TEST run all testSet tests
        if (!testGet(myList))
            failCount++;


        if (testClear(myList) == false)
            failCount++;


        //TEST: Add testdata0 and verify size
        myList.add(testData0);
        if (myList.size() != 1)
            failCount++;
        //TEST: Add testdata1 and verify size
        myList.add(testData1);
        if (myList.size() != 2)
            failCount++;

        //TEST: Add testdata2 and verify size
        myList.add(testData2);
        if (myList.size() != 3)
            failCount++;

        //TEST: Add testdata3 and verify size
        myList.add(testData3);
        if (myList.size() != 4)
            failCount++;

        // create an list if items
        EmptyArrayList testDataItems = new EmptyArrayList();
        testDataItems.add(testData2);
        testDataItems.add(testData3);
        testDataItems.add(testData0);



        // verify each item individually
        if  (!myList.contains(testData2))
            failCount++;

        if  (!myList.contains(testData3))
            failCount++;

        if  (!myList.contains(testData0))
            failCount++;

        // test containAll
        if (!myList.containsAll(testDataItems))
            failCount++;

        // remove an item and check again.
        myList.remove(testData3);

        // test containAll. Expected return false;
        if (myList.containsAll(testDataItems))
            failCount++;

        // add item back, and test again.
        myList.add(testData3);

        // test containAll. Expected return true;
        if (!myList.containsAll(testDataItems))
            failCount++;

        if (failCount == 0)
        {
            System.out.println("All \"testContainsAll\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testContainsAll\" tests: " + failCount );

        return false;


    }


    public static boolean testRetainAll(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData0 = "Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "Some test data 123123 58734583!@#$%^&*(+2";
        String testData3 = "Some test data 123123 58734583!@#$%^&*(+3";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;


        // TEST run all testGet tests
        if (!testGet(myList))
            failCount++;

        // TEST run all testSet tests
        if (!testGet(myList))
            failCount++;


        if (testClear(myList) == false)
            failCount++;


        //TEST: Add testdata0 and verify size
        myList.add(testData0);
        if (myList.size() != 1)
            failCount++;
        //TEST: Add testdata1 and verify size
        myList.add(testData1);
        if (myList.size() != 2)
            failCount++;

        //TEST: Add testdata2 and verify size
        myList.add(testData2);
        if (myList.size() != 3)
            failCount++;

        //TEST: Add testdata3 and verify size
        myList.add(testData3);
        if (myList.size() != 4)
            failCount++;

        // create an list if items that will be removed from myList
        EmptyArrayList removeListItem = new EmptyArrayList();
        removeListItem.add(testData2);
        removeListItem.add(testData3);

        // check count to verify two elements have been remove d
        myList.retainAll(removeListItem);
        if (myList.size() != 2)
            failCount++;

        if  (!myList.contains(testData2))
            failCount++;

        if  (!myList.contains(testData3))
            failCount++;

        if  (myList.contains(testData0))
            failCount++;

        if  (myList.contains(testData1))
            failCount++;



        if (failCount == 0)
        {
            System.out.println("All \"testRetainAll\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testRetainAll\" tests: " + failCount );

        return false;


    }


    public static boolean testAddAllByIndex(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData0 = "Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "Some test data 123123 58734583!@#$%^&*(+2";
        String testData3 = "Some test data 123123 58734583!@#$%^&*(+3";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;


        // TEST run all testGet tests
        if (!testGet(myList))
            failCount++;

        // TEST run all testSet tests
        if (!testGet(myList))
            failCount++;


        if (testClear(myList) == false)
            failCount++;



        // create an list of test items to be added
        EmptyArrayList TestData = new EmptyArrayList();
        TestData.add(testData0);
        TestData.add(testData1);
        TestData.add(testData2);
        TestData.add(testData3);


        // test addAll method starting at index 2
        if (!myList.addAll(0,TestData))
            failCount++;

        //check size
        myList.retainAll(TestData);
        if (myList.size() != 4)
            failCount++;

        // validate  data individually  pass = true
        if  (!myList.contains(testData0))
            failCount++;

        if  (!myList.contains(testData1))
            failCount++;

        if  (!myList.contains(testData2))
            failCount++;

        // pass = true
        if  (!myList.contains(testData3))
            failCount++;

        // check contains all method. pass = true
        if (!myList.containsAll(TestData))
            failCount++;




        if (failCount == 0)
        {
            System.out.println("All \"testAddAllByIndex\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testAddAllByIndex\" tests: " + failCount );

        return false;


    }


    static boolean testAddAll(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData0 = "Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "Some test data 123123 58734583!@#$%^&*(+2";
        String testData3 = "Some test data 123123 58734583!@#$%^&*(+3";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;


        // TEST run all testGet tests
        if (!testGet(myList))
            failCount++;

        // TEST run all testSet tests
        if (!testGet(myList))
            failCount++;


        if (testClear(myList) == false)
            failCount++;



        // create an list of test items to be added
        EmptyArrayList TestData = new EmptyArrayList();
        TestData.add(testData0);
        TestData.add(testData1);
        TestData.add(testData2);
        TestData.add(testData3);


        // test addAll method
        if (!myList.addAll(TestData))
            failCount++;

        //check size
        myList.retainAll(TestData);
        if (myList.size() != 4)
            failCount++;

        // validate  data individually  pass = true
        if  (!myList.contains(testData0))
            failCount++;

        if  (!myList.contains(testData1))
            failCount++;

        if  (!myList.contains(testData2))
            failCount++;

        // pass = true
        if  (!myList.contains(testData3))
            failCount++;

        // check contains all method. pass = true
        if (!myList.containsAll(TestData))
            failCount++;




        if (failCount == 0)
        {
            System.out.println("All \"testAddAll\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testAddAll\" tests: " + failCount );

        return false;


    }


    static boolean testSubListFromIndex(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData0 = "Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "Some test data 123123 58734583!@#$%^&*(+2";
        String testData3 = "Some test data 123123 58734583!@#$%^&*(+3";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;


        // TEST run all testGet tests
        if (!testGet(myList))
            failCount++;

        // TEST run all testSet tests
        if (!testGet(myList))
            failCount++;


        if (testClear(myList) == false)
            failCount++;



        // create an list of test items to be added
        EmptyArrayList TestData = new EmptyArrayList();
        TestData.add(testData0);
        TestData.add(testData1);
        TestData.add(testData2);
        TestData.add(testData3);



        // test addAll method
        if (!myList.addAll(TestData))
            failCount++;

        //check size
        myList.retainAll(TestData);
        if (myList.size() != 4)
            failCount++;

        EmptyArrayList sublist = myList.subList(1,2);


        if (sublist.size() != 1)
            failCount++;


        // validate  data individually  pass = true


        if  (!sublist.contains(testData1))
            failCount++;

        if  (!sublist.contains(testData3))
            failCount++;



        // check contains all method. pass = true
        if (!sublist.containsAll(TestData))
            failCount++;




        if (failCount == 0)
        {
            System.out.println("All \"testSubListFromIndex\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testSubListFromIndex\" tests: " + failCount );

        return false;


    }


    static boolean testtoArray(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData0 = "1 Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "2 Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "3 Some test data 123123 58734583!@#$%^&*(+2";
        String testData3 = "4 Some test data 123123 58734583!@#$%^&*(+3";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;


        // TEST run all testGet tests
        if (!testGet(myList))
            failCount++;

        // TEST run all testSet tests
        if (!testGet(myList))
            failCount++;


        if (testClear(myList) == false)
            failCount++;



        // create an list of test items to be added
        EmptyArrayList TestData = new EmptyArrayList();
        TestData.add(testData0);
        TestData.add(testData1);
        TestData.add(testData2);
        TestData.add(testData3);



        // test addAll method
        if (!myList.addAll(TestData))
            failCount++;

        //check size
        myList.retainAll(TestData);
        if (myList.size() != 4)
            failCount++;

        Object[] testArray = myList.toArray();

        if (testArray.length != 4)
            failCount++;

        if (testArray[0] !=  testData0)
            failCount++;

        if (testArray[1] !=  testData1)
            failCount++;

        if (testArray[2] !=  testData2)
            failCount++;

        if (testArray[3] !=  testData3)
            failCount++;





        // validate  data individually  pass = true


        if  (!myList.contains(testData2))
            failCount++;

        if  (!myList.contains(testData3))
            failCount++;



        // check contains all method. pass = true
        if (!myList.containsAll(TestData))
            failCount++;




        if (failCount == 0)
        {
            System.out.println("All \"testtoArray\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testtoArray\" tests: " + failCount );

        return false;


    }


    static boolean testFillToArray(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData0 = "1 Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "2 Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "3 Some test data 123123 58734583!@#$%^&*(+2";
        String testData3 = "4 Some test data 123123 58734583!@#$%^&*(+3";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;


        // TEST run all testGet tests
        if (!testGet(myList))
            failCount++;

        // TEST run all testSet tests
        if (!testGet(myList))
            failCount++;


        if (testClear(myList) == false)
            failCount++;



        // create an list of test items to be added
        EmptyArrayList TestData = new EmptyArrayList();
        TestData.add(testData0);
        TestData.add(testData1);
        TestData.add(testData2);
        TestData.add(testData3);



        // test addAll method
        if (!myList.addAll(TestData))
            failCount++;

        //check size
        myList.retainAll(TestData);
        if (myList.size() != 4)
            failCount++;

        String[] testArray = new String[4];
        myList.toArray(testArray);

        if (testArray.length != 4)
            failCount++;

        if (testArray[0] !=  testData0)
            failCount++;

        if (testArray[1] !=  testData1)
            failCount++;

        if (testArray[2] !=  testData2)
            failCount++;

        if (testArray[3] !=  testData3)
            failCount++;





        // validate  data individually  pass = true


        if  (!myList.contains(testData2))
            failCount++;

        if  (!myList.contains(testData3))
            failCount++;



        // check contains all method. pass = true
        if (!myList.containsAll(TestData))
            failCount++;




        if (failCount == 0)
        {
            System.out.println("All \"testFillToArray\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testFillToArray\" tests: " + failCount );

        return false;


    }


    static boolean testgetItorator(EmptyArrayList<String> myList)
    {
        boolean testpass = true;
        String testData0 = "1 Some test data 123123 58734583!@#$%^&*(+0";
        String testData1 = "2 Some test data 123123 58734583!@#$%^&*(+1";
        String testData2 = "3 Some test data 123123 58734583!@#$%^&*(+2";
        String testData3 = "4 Some test data 123123 58734583!@#$%^&*(+3";
        int failCount =  0;

        // TEST: Call testClear() to wipe existing data, verify list object has
        // been properly intialized, and method testClear() passes all tests
        if (testClear(myList) == false)
            failCount++;


        // TEST run all testGet tests
        if (!testGet(myList))
            failCount++;

        // TEST run all testSet tests
        if (!testGet(myList))
            failCount++;


        if (testClear(myList) == false)
            failCount++;



        // create an list of test items to be added
        EmptyArrayList TestData = new EmptyArrayList();
        TestData.add(testData0);
        TestData.add(testData1);
        TestData.add(testData2);
        TestData.add(testData3);



        // test addAll method
        if (!myList.addAll(TestData))
            failCount++;

        //check size
        myList.retainAll(TestData);
        if (myList.size() != 4)
            failCount++;


        Iterator<String> testIterator = myList.iterator();
        if(testIterator.hasNext()!= true)
            failCount++;

        if(testIterator.next()!= testData0)
            failCount++;

        if(testIterator.next()!= testData1)
            failCount++;

        if(testIterator.next()!= testData2)
            failCount++;

        if(testIterator.next()!= testData3)
            failCount++;

        if(testIterator.hasNext()!= false)
            failCount++;


        // check contains all method. pass = true
        if (!myList.containsAll(TestData))
            failCount++;




        if (failCount == 0)
        {
            System.out.println("All \"testgetItorator\" tests have passed");
            return true;
        }
        System.out.println("Failed \"testgetItorator\" tests: " + failCount );

        return false;


    }


}


