package nrnoble;
/*
* Neal Noble
* May 2017
* Assignment: Trees Part2
* Instructor: Josh Archer
*/


import java.io.IOException;
import java.util.Scanner;
import static nrnoble.Utilities.getWords;


public class Main
{

    public static String dictionaryPath = nrnoble.Utilities.getPath2() + "\\nrnoble\\dictionary.txt";

    public static void main(String[] args) throws IOException
    {
        userLoop();
    }

    // main loop for application
    private static void userLoop() throws IOException
    {
        boolean exit = false;
        Scanner textscanner = new Scanner(System.in);
        Dictionary dictionary = new Dictionary(getWords(1, dictionaryPath));
        dictionary.clear();

        assignmentHeader();

        while(exit == false)
        {

            // Get user selection
            int selection = userInput();


            // Handle user selection Load dictionary
            if (selection == 1)
            {
                //List<Entry> dictionaryData = getDictionaryData();
                System.out.print("loading....");
                dictionary = new Dictionary(getWords(-1, dictionaryPath));
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

    
    // Handle user input
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


    //
    public static void assignmentHeader()
    {
        System.out.println();
        System.out.println("    Neal Noble");
        System.out.println("    May 2017  ");
        System.out.println("    Assignment: Trees Part2");
        System.out.println("    Instructor: Josh Archer");
        System.out.println();
    }


}
