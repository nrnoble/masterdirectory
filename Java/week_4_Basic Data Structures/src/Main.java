// Neal R Noble
// IT333
// April 2016
// Exercises - Basic Data Structures


import org.jetbrains.annotations.NotNull;

import java.util.*;

public class Main
{

    public static void main(String[] args)
    {
        System.out.println("Exercises - Basic Data Structures");

        List<Integer> randomListOfIntegers_L = Utils.getUniqueRandomNumbers(100,0,100000);
        //System.out.println("-------------------------------------------------------");
        List<Integer> randomListOfIntegers_P = Utils.getUniqueRandomNumbers(5,0,100);
        //System.out.println("-------------------------------------------------------");


        Collections.sort(randomListOfIntegers_P);
        Collections.sort(randomListOfIntegers_L);



        // Exercises.printLots(randomListOfIntegers_L, randomListOfIntegers_P );
        // Exercises.Josephus(51,7);

        xNode myNodeList = new xNode(1);

        myNodeList.add(2);
        myNodeList.add(3);
        myNodeList.add(4);
        myNodeList.add(5);
        myNodeList.add(6);
        myNodeList.add(7);
        myNodeList.remove(6);


        System.out.println("size: " + myNodeList.size());
        System.out.println("removing 6: " + myNodeList.remove(6));

        System.out.println("size: " + myNodeList.size());
        
        System.out.println("\n\r\r\rExiting.... ");
    }
}
