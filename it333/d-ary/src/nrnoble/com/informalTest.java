package nrnoble.com;

import java.util.Arrays;
import java.util.Arrays;

public class informalTest
{

    public static void main(String[] args)
    {
        MarryHeap<Integer> mary = new MarryHeap<>();
//add a few items
//int[] input = {20,19,18,17,16,14,13,12,11,10,9,8,7,6,5,4,3,2,1};
//int[] input = {20,19,18,17,16,14,13,12,11,10,9,8,7,6,5,4,3,2,1};
        int[] input = {25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1};
        for (int i = 0; i < input.length; i++)
        {
            mary.insert(input[i]);
        }
        System.out.println(mary.peek());
        System.out.println(mary.contains(20));
        int[] nums = new int[input.length];
        for(int i = 0; i < nums.length; i++)
        {
            nums[i] = mary.delMin();
        }
        System.out.println(Arrays.toString(nums));
    }

}