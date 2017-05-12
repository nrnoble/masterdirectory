import java.util.*;

/**
 * Created by Neal on 3/28/2016.
 */

public class fibonacci
{


    /**
     * Get an array of fibonacci numbers
     * @param _n is the number fibonacci numbers to get
     * @return Integer array of fibonacci numbers
     */
    public static Integer[] fibonacci_sequence (int _n)
    {
        Integer[] sequence = new Integer[_n+2];
        sequence[0] = 0;
        sequence[1] = 1;
        for (int i = 2; i <_n + 2; i++)
        {
            sequence[i] = sequence[i-1] + sequence[i-2];
        }

        return sequence;
    }

    
    /**
     * Not fully implemented. Do not use
     * @param _n
     * @return
     */
    public static Integer[] fibonacci_sequence_22 (int _n)
    {

        Integer[] sequence = new Integer[_n+2];
        sequence[0] = 0;
        sequence[1] = 1;
        for (int i = 2; i <_n + 2; i++)
        {
            PriorityQueue<Integer> fibQueue = fibonacci.fibonacciNumber(i);
            sequence[i] = fibQueue.poll() +  fibQueue.poll();
        }

        return sequence;
    }



    /**
     * Get the n'th fibonacci number
     * @param _n the n'th fibonacci number
     * @return fibonacci number
     */
    public static PriorityQueue fibonacciNumber (int _n)
    {

        PriorityQueue <Integer> fibQueue = new PriorityQueue<Integer>();

        fibQueue.add(0);
        fibQueue.add(1);

        for (int i = 3; i <= _n ; i++)
        {
            fibQueue.add(fibQueue.poll() + fibQueue.peek());
        }

        return fibQueue;
    }


}

