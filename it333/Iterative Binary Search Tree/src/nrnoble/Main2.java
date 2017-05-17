package nrnoble;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


import static nrnoble.Utilities.getDictionaryData;
import static nrnoble.Utilities.getWords;


/**
 * Created by Neal on 5/16/2017.
 */
public class Main2
{
    private static  String indent = "      ";



    public static void main(String[] args) throws IOException
    {
 ///      System.out.println("Verification Tests");
//        bstTests();
//        bstSymTableTests();
//        bstSymTableTests2();
//        Part2Tests();

//        PartII();

        userLoop();


    }
    
    private static void userLoop() throws IOException
    {
        boolean exit = false;
        Scanner textscanner = new Scanner(System.in);
        Dictionary dictionary = new Dictionary(getWords(1,"E:\\Data\\Github\\it333\\Iterative Binary Search Tree\\src\\nrnoble\\dictionary.txt"));
        dictionary.clear();

        while(exit == false)
        {

            // Get user selection
            int selection = userInput();


            // Handle user selection Load dictionary
            if (selection == 1)
            {
                //List<Entry> dictionaryData = getDictionaryData();
                System.out.print("loading....");
                dictionary = new Dictionary(getWords(10000,"E:\\Data\\Github\\it333\\Iterative Binary Search Tree\\src\\nrnoble\\dictionary.txt"));
                System.out.println("Done");

                System.out.println("dictionary size(): " + dictionary.size() + " word definitions");
                System.out.println();

            }

            // Handle user selection Word Lookup
            if (selection == 2)
            {
                if (dictionary.isEmpty())
                {
                    System.out.println("ERROR: Please load dictionary first");
                    System.out.println();
                }
                else
                {
                    System.out.println("Please enter a word: ");
                    String word =  textscanner.next();
                    if (dictionary.hasWord(word))
                    {
                        System.out.println("Definition: " + dictionary.define(word)) ;
                        System.out.println();
                        System.out.println();
                    }
                    else
                    {
                        System.out.println("Please enter a definition for \"" + word + "\": ");
                        String definition =  textscanner.next();
                        dictionary.updateDictionary(word,definition);
                    }
                }

            }


            if (selection == 3)
            {
                System.out.println("Thanks for viewing my dictionary!");
                break;
            }
        }
    }

    
    
    private static int userInput() throws IOException
    {
        while (true)
        {
            try
            {
                System.out.println("1. Load dictionary");
                System.out.println("2. Lookup Word");
                System.out.println("3. Exit");
                System.out.println("---------------------");
                Scanner scan = new Scanner(System.in);
                int choice = scan.nextInt();
                if (choice == 1 || choice == 2 || choice == 3)
                {
                    return choice;
                }

            }
            catch (Exception err)
            {

            }
            System.out.println("Select 1, 2, or 3");
            System.out.println();
        }

    }


    private static void PartII() throws IOException
    {

            //List<Entry> dictionaryData = getDictionaryData();
            Dictionary dictionary = new Dictionary(getWords(10000,"E:\\Data\\Github\\it333\\Iterative Binary Search Tree\\src\\nrnoble\\dictionary.txt"));
            System.out.println("dictionary size(): " + dictionary.size());
            System.out.println("dictionary size(): " + dictionary.size());
            System.out.println("dictionary.hasWord(\"abhorrible\"): " + dictionary.hasWord("abhorrible"));
            System.out.println("dictionary.define(\"abhorrible\"): " + dictionary.define("abhorrible"));
            System.out.println("dictionary.define(\"store\"): " + dictionary.hasWord("store"));
            System.out.println("dictionary.updateDictionary(\"store\", \"to keep in reserve\"): " + dictionary.updateDictionary("store", "to keep in reserve"));
            System.out.println("dictionary.define(\"store\"): " + dictionary.hasWord("store"));
            System.out.println("dictionary.define(\"store\"): " + dictionary.define("store"));
            System.out.println("dictionary.size(): " + dictionary.size());
            System.out.println("dictionary.isEmpty(): " + dictionary.isEmpty());
            System.out.println("dictionary.clear()");
            dictionary.clear();
            System.out.println("dictionary.isEmpty(): " + dictionary.isEmpty());
            System.out.println("dictionary.size(): " + dictionary.size());
            System.out.println("dictionary.define(\"store\"): " + dictionary.hasWord("store"));
            System.out.println("dictionary.updateDictionary(\"store\", \"to keep in reserve\"): " + dictionary.updateDictionary("store", "to keep in reserve"));
            System.out.println("dictionary.size(): " + dictionary.size());
            System.out.println("dictionary.updateDictionary(\"store\",  \"to keep in reserve for future use\"): " + dictionary.updateDictionary("store", "to keep in reserve for future use"));
            System.out.println("dictionary.define(\"store\"): " + dictionary.define("store"));
            System.out.println("dictionary.size(): " + dictionary.size());
            System.out.println("dictionary.updateDictionary(\"store\",  \"a business that sells goods\"): " + dictionary.updateDictionary("store", "a business that sells goods"));
            System.out.println("dictionary.define(\"store\"): " + dictionary.define("store"));
            System.out.println("dictionary.size(): " + dictionary.size());
            System.out.println("dictionary.updateDictionary(\"Basketball\",  \"a sport\"): " + dictionary.updateDictionary("Basketball", "a sport"));
            System.out.println("dictionary.size(): " + dictionary.size());
            System.out.println("dictionary.updateDictionary(\"BASKETBALL\",  \"an american sport\"): " + dictionary.updateDictionary("BASKETBALL", "an american sport"));
            System.out.println("dictionary.size(): " + dictionary.size());
            System.out.println("dictionary.define(\"Basketball\"): " + dictionary.define("Basketball"));
            System.out.println("dictionary.define(\"BASKETBALL\"): " + dictionary.define("BASKETBALL"));
            System.out.println("dictionary.updateDictionary(\"   BASKETBALL    \",  \"an american sport\"): " + dictionary.updateDictionary("   BASKETBALL   ", "an american sport that was first played December 21, 1891"));
            System.out.println("dictionary.define(\"Basketball\"): " + dictionary.define("Basketball"));
            System.out.println("dictionary.define(\"BASKETBALL\"): " + dictionary.define("BASKETBALL"));
            System.out.println("dictionary.size(): " + dictionary.size());
            System.out.println("dictionary.define(\"store\"): " + dictionary.hasWord("store"));
            System.out.println("dictionary.define(\"Store\"): " + dictionary.hasWord("Store"));
            System.out.println("dictionary.define(\"StORe\"): " + dictionary.hasWord("StORe"));
            System.out.println("dictionary.define(\"StORe!\"): " + dictionary.hasWord("StORe!"));
            System.out.println("dictionary.define(\"  store    \"): " + dictionary.hasWord("   store   "));
            System.out.println("dictionary.define(\"store    \"): " + dictionary.hasWord("store   "));
            System.out.println("dictionary.define(\"store\\r\\n    \"): " + dictionary.hasWord("store\r\n   "));
            System.out.println("dictionary.define(\"   store\"): " + dictionary.hasWord("    store"));
            System.out.println("dictionary.define(\"\"): " + dictionary.hasWord(""));
            System.out.println("dictionary.define(\"\"): " + dictionary.hasWord(""));












    }




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

        // Test data
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

        // Test data
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

        // These three items will return false to validate some tests because data
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
