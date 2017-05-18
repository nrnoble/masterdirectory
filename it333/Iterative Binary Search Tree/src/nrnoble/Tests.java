package nrnoble;
/*
* Neal Noble
* May 2017
* Assignment: Trees Part2
* Instructor: Josh Archer
*/

import java.util.ArrayList;
import java.util.List;

import static nrnoble.Utilities.getDictionaryData;

/**
 * Manual and automated tests for the BSTSymbolTable class, Binary Search Tree ckass and Bdictionary class
 */
public class Tests
{
    private static  String indent = "      ";
    private static int[] testArray = new int[]{13,20,31,33,44,57,61,90,95,100,120,141,160,180};


    /**
     * Tests for the BinarySearch Tree class
     */
    public static void bstTests()
    {

        List<Entry> dictionaryData = getDictionaryData();

        BinarySearchTree<String> bst = new BinarySearchTree<String>();
        System.out.println("TEST: Method AddingUpdate()");
        bst.addUpdate("Jared");
        bst.addUpdate("Carey");
        bst.addUpdate("Alvin");
        bst.addUpdate("Sarah");
        bst.addUpdate("Emma");
        bst.addUpdate("Jack");
        bst.addUpdate("Teri");

        System.out.println();
        System.out.println("TEST: Method size()");
        System.out.println("Size: " + bst.size());


        System.out.println();
        System.out.println("--------------------------------------");
        System.out.println();

        System.out.println("TEST: in Order");

        List<String> inOrderlist = bst.inOrder();

        System.out.print(indent + "inOrder: ");

        for(String i: inOrderlist)
        {
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println();

        System.out.println("TEST: Post Order");
        List<String> postOrderlist = bst.postOrder();
        System.out.print(indent + "PostOrder: ");

        for(String i: postOrderlist)
        {
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println();


        System.out.println("TEST: Pre Order");
        List<String> preOrderlist = bst.preOrder();
        System.out.print(indent + "preOrder: ");

        for(String i: preOrderlist)
        {
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println();
    }


    public static void Part2Tests()
    {

        List<Entry> dictionaryData = getDictionaryData();

        Entry entry = dictionaryData.get(0);
        System.out.println(entry.toString());
        entry = dictionaryData.get(1);
        System.out.println(entry.toString());

    }


    /**
     * Tests for the BSTSymbolTable class
     */
    public static void bstSymTableTests2()
    {

        String indent = "      ";

        // Test NodeData
        List<String> names = new ArrayList<>();
        names.add("Auburn");
        names.add("Kent");
        names.add("Seattle");
        names.add("Bellevue");
        names.add("Wenatchee");
        names.add("Spokane");
        names.add("Sumner");
        names.add("Tacoma");
        names.add("Olympia");
        names.add("Issaquah");


        BSTSymbolTable<String,Integer> bstSym = new BSTSymbolTable<>();
        bstSym.put ("Auburn",98002);
        bstSym.put ("Kent",98032);
        bstSym.put ("Seattle",98178);
        bstSym.put ("Bellevue",98004);
        bstSym.put ("Wenatchee",98801);
        bstSym.put ("Spokane",99208);
        bstSym.put ("Sumner",98390);
        bstSym.put ("Tacoma",98402);
        bstSym.put ("Olympia",98501);
        bstSym.put ("Issaquah",98027);



        System.out.println("TEST: " + "Adding several key/value pairs to the table (names/ages, objects/colors, website/ratings, or any other examples you can think up)");

        for (String name: names)
        {
            System.out.println(indent + "bstSym.get (" + name + "):" + bstSym.get (name));
        }

        String name1 = "bob";
        System.out.println(indent + "bstSym.get (" + name1 + "):" + bstSym.get (name1));


        System.out.println();
        System.out.println("TEST: " + "Verify that keys or values are within the table using containsKey() & containsValue()");
        for (String name: names)
        {
            System.out.println(indent + "bstSym.contains (" + name + "):" + bstSym.containsKey (name));
        }


        System.out.println();
        System.out.println("TEST: Verify that you can print out the keys in the table in sorted order");
        List<String> keys = bstSym.keys();
        System.out.print(indent + "keys: ");

        for(String i: keys)
        {
            System.out.print(i + " ");
        }
        System.out.println();

        System.out.println();
        System.out.println("TEST: Verify that you can print out the values in the table");
        List<Integer> values = bstSym.values();
        System.out.print(indent + "Values: ");

        for(Integer i: values)
        {
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println();

        System.out.println("TEST: verify that the number of key/value pairs in the tree are tracked correctly using size(), isEmpty() & clear()");

        System.out.println(indent + "bstSym.isEmpty(): " + bstSym.isEmpty());
        System.out.println(indent + "bstSym.size(): " + bstSym.size());
        System.out.println(indent + "Calling bstSym.clear()");
        bstSym.clear();
        System.out.println(indent + "bstSym.size(): " + bstSym.size());
        System.out.println(indent + "bstSym.isEmpty(): " + bstSym.isEmpty());
        System.out.println();

    }

    /**
     * Tests for the BSTSymbolTable class
     */
    public static void bstSymTableTests()
    {

        // Test NodeData
        List<String>names = new ArrayList<>();
        names.add("Jared");
        names.add("Carey");
        names.add("Sarah");
        names.add("Alvin");
        names.add("Emma");
        names.add("Jack");
        names.add("Teri");
        names.add("Neal");
        names.add("Zoe");
        names.add("Fred");

        // These three items will return false to validate some tests because NodeData
        // will not be added to the tree. Example contains() will return false
        names.add("Red");
        names.add("Green");
        names.add("Blue");


        BSTSymbolTable <String,Integer> bstSym = new BSTSymbolTable<>();
        bstSym.put ("Jared",10);
        bstSym.put ("Carey",22);
        bstSym.put ("Sarah",20);
        bstSym.put ("Alvin",25);
        bstSym.put ("Emma",15);
        bstSym.put ("Jack",8);
        bstSym.put ("Teri",35);
        bstSym.put ("Neal",32);
        bstSym.put ("Zoe",12);
        bstSym.put ("Fred",56);


        System.out.println("TEST: " + "Adding several key/value pairs to the table (names/ages, objects/colors, website/ratings, or any other examples you can think up)");

        for (String name: names)
        {
            System.out.println(indent + "bstSym.get (" + name + "):" + bstSym.get (name));
        }

        String name1 = "bob";
        System.out.println(indent + "bstSym.get (" + name1 + "):" + bstSym.get (name1));


        System.out.println();
        System.out.println("TEST: " + "Verify that keys or values are within the table using containsKey() & containsValue()");
        for (String name: names)
        {
            System.out.println(indent + "bstSym.contains (" + name + "):" + bstSym.containsKey (name));
        }

        String name = "bob";
        System.out.println(indent + "bstSym.contains (" + name + "):" + bstSym.containsKey (name));


        System.out.println();
        System.out.println("TEST: Verify that you can print out the keys in the table in sorted order");
        List<String> keys = bstSym.keys();
        System.out.print(indent + "keys: ");

        for(String i: keys)
        {
            System.out.print(i + " ");
        }
        System.out.println();

        System.out.println();
        System.out.println("TEST: Verify that you can print out the values in the table");
        List<Integer> values = bstSym.values();
        System.out.print(indent + "Values: ");

        for(Integer i: values)
        {
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println();

        System.out.println("TEST: verify that the number of key/value pairs in the tree are tracked correctly using size(), isEmpty() & clear()");

        System.out.println(indent + "bstSym.isEmpty(): " + bstSym.isEmpty());
        System.out.println(indent + "bstSym.size(): " + bstSym.size());
        System.out.println(indent + "Calling bstSym.clear()");
        bstSym.clear();
        System.out.println(indent + "bstSym.size(): " + bstSym.size());
        System.out.println(indent + "bstSym.isEmpty(): " + bstSym.isEmpty());
        System.out.println();
    }


}
