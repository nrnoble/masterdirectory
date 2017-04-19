/*
 * Neal Noble
 * April 2017
 * Assignment: Linked List (Part 1)
 * Instructor: Josh Archer
 */
package part2;

import part2.Node;
import part2.UniqueList;

import java.io.IOException;
import java.security.NoSuchAlgorithmException;
import java.util.Iterator;

import static javafx.scene.input.KeyCode.T;


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


        UniqueList<String> myList2= new UniqueList<String>();
        myList2.add("a"); // 0
        myList2.add("b"); // 1
        myList2.add("c"); // 2
        myList2.add("d");  // 3
        myList2.add("e");  // 4
        myList2.add("f");  // 5
        myList2.add("g");  // 6
        myList2.add("h");  // 7
        myList2.add("i");  // 8
        myList2.add("j");  // 9
        myList2.add("k");  // 10
        myList2.add("l");  // 11
        myList2.add("m");  // 12
        myList2.add("n");  // 13
        myList2.add("o");  // 14
        myList2.add("p");  // 15
        myList2.add("q");  // 16
        myList2.add("r");  // 17
        myList2.add("s");  // 18
        myList2.add("t");  // 19
        myList2.add("u");  // 20
        myList2.add("v");  // 21
        myList2.add("w");  // 22
        myList2.add("x");  // 23
        myList2.add("y");  // 24
        myList2.add("z");  // 25


        System.out.println();

        System.out.println("Size: " + myList2.size());
        alist = myList2.toArray();
        System.out.println("alist.length = " + alist.length);

        for (int i = 0; i < alist.length ; i++)
        {
            System.out.println("element[" + i + "]=" + alist[i]);
        }
//
//        int result = myList.get("a");
//        System.out.println("myList.get(3): " + result);
//        System.out.println("all done!");

        
        int index = myList2.lastIndexOf("a");
        System.out.println("index of a: " + index);

        index = myList2.lastIndexOf("z");
        System.out.println("index of z: " + index);

        index = myList2.lastIndexOf("l");
        System.out.println("index of l: " + index);

        index = myList2.lastIndexOf("~");
        System.out.println("index of ~: " + index);

        Iterator<String> alphList = myList2.iterator();

        while (alphList.hasNext())
        {
            System.out.print(alphList.next() + ", ");
        }
        System.out.println();

        System.out.println();
        System.out.println();

//        myList2.add("insert test");
//        myList2.add(3,"insert test2");

        alphList = myList2.iterator();


        while (alphList.hasNext())
        {
            System.out.print(alphList.next() + ", ");
        }
        System.out.println();



        System.out.println("All done");
    }

}

