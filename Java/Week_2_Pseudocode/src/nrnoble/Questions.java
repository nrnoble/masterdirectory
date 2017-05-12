package nrnoble;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Neal on 4/8/2016.
 */
public class Questions
{




    public static void reorder()
    {
        String[] letters = {"x", "y", "z"};
        String x = letters[0];
        letters[0] = letters[1];
        letters[1] = letters[2];
        letters[2] = x;
        for (int i = 0; i < letters.length; i++) {
            System.out.print(letters[i] );
            if (i < letters.length-1)
                System.out.print(",");

        }

    }
    
    public static void rotateLeft(String[] str)
    {
        String firstItem = str[0];
        int count = 1;
        int i = 0;
        while (i < str.length - 1) {
            str[i] = str[++i];
            count = count + 1;
            //System.out.println(str[i]);
        }
        //System.out.println(firstItem);
        str[str.length - 1] = firstItem;
        count++;
        for (int j = 0; j < str.length; j++) {
            System.out.println(str[j]);
        }
        System.out.println(count);

    }
        public static void sumArray(Integer[] nums)
        {

            Integer total = 0;
            int i = 0;
            while (i < nums.length)
            {
                total = total + nums[i++];
            }

            System.out.println(total);
        }


    public static void duplicateNumbers(int[] nums)
    {
        int prevNum = nums[0];
        int lastDup = nums[nums.length-1];
        List<Integer> dups = new ArrayList<Integer>();

        // if the array is zero or one, then there are no duplicate numbers. No point of going further
        if (nums.length == 0 || nums.length == 1 )
        {
            return;
        }

        // if first and last elements are equal, then all elements inbetween are the same number
        if (prevNum == lastDup) {
            dups.add(prevNum);
            return;
        }

        // check if current element match previous element, and then check if current element matches previously
        // added duplicate number
        for (int i = 1; i < nums.length; i++)
        {
            if (nums[i] == prevNum && nums[i] != lastDup)
            {
                dups.add(nums[i]);
                lastDup = nums[i];
            }
            prevNum = nums[i];

        }

        for (Integer dup : dups)
        {
            System.out.println(dup);
        }





    }



    public static int mode(int[] nums)
    {
        int dupCount = 0;
        int dupNumber = nums[0];
        int mostDupCount = 1;
        int mostDupNumber = nums[0];


        // if first and last elements are equal, then all elements inbetween are the same number
        // return full length of array. Exit
        if (nums[0] == nums[nums.length-1])
        {
            System.out.println(nums.length);
            System.out.println(nums[0]);
            return nums.length;
        }

        // if the array is one, then it is the largest. exit
        if (nums.length == 1 )
        {
            System.out.println(nums.length);
            System.out.println(nums[0]);
            return nums[0];
        }


        // check if current element match previous element, and then check if current element matches previously
        // then increment duplicate count
        for (int i = 1; i < nums.length; i++)
        {
            if (nums[i] == dupNumber)
            {
                dupCount++;
                // always continue except for the very last element, let last element fall through
                if (i < nums.length-1)
                {
                    continue;
                }
            }

            // update the most duplicate number and count if greater than previous duplicate count ceiling
            if (dupCount > mostDupCount)
            {
                mostDupCount = dupCount;
                mostDupNumber = dupNumber;
            }

            // reset duplicate count and number
            dupCount = 1;
            dupNumber = nums[i];
        }

        System.out.println(mostDupCount);
        System.out.println(mostDupNumber);
        return mostDupNumber;

    }


    public static int mode2(int[] n)
    {


        int count2 = 0;
        int count1 = 0;
        int pupular1 =0;
        int popular2 =0;


        for (int i = 0; i < n.length; i++)
        {
            pupular1 = n[i];
            count1 = 0;    //see edit

            for (int j = i + 1; j < n.length; j++)
            {
                if (pupular1 == n[j])
                    count1++;
            }

            if (count1 > count2)
            {
                popular2 = pupular1;
                count2 = count1;
            }

            else if(count1 == count2)
            {
                popular2 = Math.min(popular2, pupular1);
            }
        }

        System.out.println(popular2);
        return popular2;
    }


    public static int[] insert(int[] arrayOfIntegers, int insertNum)
    {

        int index = 0;
        int[] newArray = new int[arrayOfIntegers.length+1];

        while (arrayOfIntegers[index] <= insertNum)
        {
            newArray[index] = arrayOfIntegers[index];
            index++;
        }

        newArray[index] = insertNum;
        index++;

        while (index <= arrayOfIntegers.length)
        {
            newArray[index] = arrayOfIntegers[index-1];
            index++;
        }

        for (int i = 0; i <newArray.length ; i++) 
        {
            System.out.println(newArray[i]);
        }
        
        return newArray;
    }

}
