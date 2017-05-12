// Neal R Noble
// IT333
// April 2016
// Exercises - Basic Data Structures

import java.util.ArrayList;
import java.util.BitSet;
import java.util.Collections;
import java.util.List;


public class Exercises extends java.awt.List
{

    // 1a. You are given a list, L, and another list, P, containing integers sorted in ascending order.
    // The operation printLots(L, P) will print the elements in L that are in positions specified by P.
    // For instance, if P = 1, 3, 4, 6, the elements in positions 1, 3, 4, and 6 in L are printed.
    // Write the procedure printLots(L, P) and test it thoroughly. You may use only the public Collections
    // API container operations.
    public static void printLots(List<Integer> _l, List<Integer> _p)
    {
        for (Integer index: _p)
        {
            System.out.println(_l.get(index-1));
        }
    }


    // Write a method that accepts a List object (using the List interface) and returns the list in
    // reverse order (your return type should be List). You should not create any other data structure
    // or array. You should write the routine only using methods from the List interface.
    public List<Integer> reverse (List<Integer> _list)
    {
        Collections.reverse(_list);
        return _list;

    }


    // The Josephus problem is the following game: N people, numbered 1 to N, are sitting in a circle.
    // Starting at person 1, a hot potato is passed. After M passes, the person holding the hot potato
    // is eliminated, the circle closes ranks, and the game continues with the person who was sitting
    // after the eliminated person picking up the hot potato. The last remaining person wins. Thus, if
    // M = 0 and N = 5, players are eliminated in order, and player 5 wins. If M = 1 and N = 5, the
    // order of elimination is 2, 4, 1, 5.
    public static int Josephus (int _people, int _passes)
    {
        int bitPosition = 0;
        int eliminated = 0;
        int passCounter = 1;
        BitSet positions  = new BitSet(_people);
        System.out.print("Elimination Order: ");
        int runcounter = 0;

        while (eliminated < _people)
        {
            runcounter++;
            if (passCounter == _passes)
            {
                if  (!positions.get(bitPosition % _people))
                {
                    int bit = (bitPosition % _people);
                    System.out.print((bit+1)+ " ");
                    positions.set(bit);
                    bitPosition++;
                    passCounter = 1;
                    eliminated++;
                    continue;
                }

                bitPosition++;
                continue;
            }

            passCounter++;

            if (positions.get(bitPosition % _people))
            {
                while (positions.get(bitPosition % _people))
                {
                    runcounter++;
                    bitPosition++;
                }
            }

            bitPosition++;
        }

        int winner = (bitPosition % _people);
        System.out.println("\n\r\r\rJosephus winner: " + winner);
        System.out.println("bitPosition counter: " + bitPosition);
        return winner;
    }









}
