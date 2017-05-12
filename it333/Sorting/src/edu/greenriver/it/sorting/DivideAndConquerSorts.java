
package edu.greenriver.it.sorting;
/*
 * Neal Noble
 * April 2017
 * Assignment: Merge Sort
 * Instructor: Josh Archer
 */



import java.util.Arrays;



public class DivideAndConquerSorts 
{

    private static int[] temp;

    public static void main (String[] args)
    {
        int[] testArray = {13,1,46,-10,20,100,33,84,2,15};
        mergeSort(testArray);
        System.out.println(Arrays.toString(testArray));

    }

    public static void mergeSort(int[] array)
    {
        if (array.length == 0 || array.length==1)
        {
            return;
        }

        temp = new int[array.length];

        mergeSort(array,0,array.length -1);
    }

    private static void mergeSort (int[] array, int low, int high)
    {
        if (high - low == 0)
        {
            return;
        }

        int mid = (low + high) /2;
        mergeSort (array, low,mid);
        mergeSort (array, mid +1 ,high);

        merge(array, low, mid, mid+1, high);

    }

    private static void merge (int[] array, int lowLeft, int highLeft,int lowRight, int highRight)
    {
        int left = lowLeft;
        int right = lowRight;
        int count = highRight - lowLeft + 1;

        for (int i = 0; i < count; i++)
        {
            if (left >highLeft)
            {
                temp[lowLeft+i] = array[right++];
            }
            else if(right > highRight)
            {
                temp[lowLeft+i] = array[left++];

            }
            else if (array[left] < array[right])
            {
                temp[lowLeft+i] = array[left++];

            }

            else if (array[right] <= array[left])
            {
                temp[lowLeft+i] = array[right++];
            }

        }

        for (int i = 0; i < count; i++)
        {
            array[lowLeft+i] = temp[lowLeft+i];
        }
    }


}
