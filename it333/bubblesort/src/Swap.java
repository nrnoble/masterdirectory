/**
 * Created by Neal on 4/6/2017.
 */

public class Swap
{

    public static void main(String[] args)
    {
        int[] deck = {13,7,4,12,10,11,5,8,9,1,3,6,2};

        System.out.print("Unsorted: ");
        printDeck(deck);
        sort (deck);
        System.out.print("  sorted: ");
        printDeck(deck);


    }
    public static void sort ( int[] input)
    {
        boolean sorted = false;
        int left, right;
        int looplength = input.length;

        while (!sorted)
        {
            sorted = true;
            for(int i=1; i< looplength; i++){
                left = input[i-1];
                right = input[i];
                if (right < left)
                {
                    input[i] = left;
                    input [i-1] = right;
                    sorted = false;
                }
            }
            looplength--;

        }

    }

    public static void printDeck (int[] deck)
    {
        for(int i=0; i< deck.length; i++)
        {
            System.out.print(String.format("%02d", deck[i]) + ", ");
        }
        System.out.println();
    }
}