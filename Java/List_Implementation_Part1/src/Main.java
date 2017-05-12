public class Main {

    public static void main(String[] args)
    {
        EmptyArrayList<String> testList = new EmptyArrayList<String>();

        // Part I tests
        ListTester.testAdd(testList);
        ListTester.testClear(testList);
        ListTester.testIsEmpty(testList);
        ListTester.testInsert(testList);

        ListTester.testContains(testList);
        ListTester.testGet(testList);
        ListTester.testIndexOf(testList);

        ListTester.testRemoveElement(testList);
        ListTester.testRemoveIndex(testList);
        ListTester.testSet(testList);
        ListTester.testSize(testList);


        // Part II tests
        ListTester.testAddAll(testList);
        ListTester.testAddAllByIndex(testList);
        ListTester.testContainsAll(testList);
        ListTester.testRemoveAll(testList);
        ListTester.testRetainAll(testList);
       // ListTester.testSubListFromIndex(testList); //Broken
        ListTester.testtoArray(testList);
        ListTester.testFillToArray(testList);
        ListTester.testgetItorator(testList);






    }
}
