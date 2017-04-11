package part1;

import java.io.IOException;
import java.security.NoSuchAlgorithmException;
import java.util.*;

/**
 * Created by Neal on 4/9/2017.
 */
public class Main
{
    public static void main(String[] args) throws IOException, NoSuchAlgorithmException {

        UniqueList<Integer> myList= new UniqueList<Integer>();

        for (int i = 1; i <=5 ; i++)
        {
            myList.add(i);
            //System.out.print(i +", ");
        }
        System.out.println();

        System.out.println("Size: " + myList.size());


        Object[] alist = myList.toArray();
        System.out.println("alist.length = " + alist.length);

        for (int i = 0; i < alist.length ; i++)
        {
            System.out.println("element[" + i + "]=" + alist[i]);
        }



        Node foundNode = myList.nodes.findNode(5);
        System.out.println("Found Node Value: " + foundNode.getNodeValue());


        myList.clear();
        System.out.println("Cleared List");
        System.out.println("Size: " + myList.size());
        System.out.println("isEmpty: " + myList.isEmpty());


//        for (int i = 1; i <=10 ; i++)
//        {
//            myList.add(i);
//            System.out.print(i +", ");
//        }

        myList.add(12); // 1
        myList.add(11); // 2
        myList.add(10); // 3
        myList.add(9);  // 4
        myList.add(8);  // 5
        myList.add(7);  // 6
        myList.add(6);  // 7
        myList.add(5);  // 8
        myList.add(4);  // 9
        myList.add(3);  // 10
        myList.add(2);  // 11
        myList.add(1);  // 12
        myList.add(13);  // 13
        myList.add(10);  // 14


        myList.remove(new Integer(13));
        myList.remove(new Integer(11));
        myList.remove(new Integer(12));
        myList.remove(new Integer(1));
        myList.remove(new Integer(2));
        myList.remove(new Integer(3));
        myList.remove(new Integer(4));
        myList.remove(new Integer(5));
        myList.remove(new Integer(6));
        myList.remove(new Integer(7));
        myList.remove(new Integer(8));
        myList.remove(new Integer(9));

        myList.add(1);
        myList.remove(new Integer(10));
        myList.remove(new Integer(01));

        //myList.remove(1);



        myList.add(12); // 1
        myList.add(11); // 2
        myList.add(10); // 3
        myList.add(9);  // 4
        myList.add(8);  // 5
        myList.add(7);  // 6
        myList.add(6);  // 7
        myList.add(5);  // 8
        myList.add(4);  // 9
        myList.add(3);  // 10
        myList.add(2);  // 11
        myList.add(1);  // 12
        myList.add(13);  // 13
        myList.add(10);  // 14

        System.out.println();

        System.out.println("Size: " + myList.size());
        alist = myList.toArray();
        System.out.println("alist.length = " + alist.length);

        for (int i = 0; i < alist.length ; i++)
        {
            System.out.println("element[" + i + "]=" + alist[i]);
        }

        int result = myList.get(-1);
        System.out.println("myList.get(-1): " + result);
        System.out.println("all done!");



        System.out.println("All done");
    }

}

