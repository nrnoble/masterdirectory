package part2;

import java.util.Iterator;

/**
 * Created by Neal on 4/20/2017.
 */
public class Utils
{
    public static boolean debugging = java.lang.management.ManagementFactory.getRuntimeMXBean().
            getInputArguments().toString().indexOf("-agentlib:jdwp") > 0;

    public static void debugPrintln(String str)
    {
        if(!debugging)
        {
            return;
        }

        System.out.println(str);
    }

    /**
     * Prints blank line only when debugger is active
     */
    public static void debugPrintln()
    {
        debugPrintln("");
    }


    /**
     * Prints only when debugger is active
     * @param str to print to console when debugger is active
     */
    public static void debugPrint(String str)
    {
        if(!debugging)
        {
            return;
        }

        System.out.print(str);
    }

    /**
     * for debugging, print out list of all noodes with their index and value
     * @param nodes list
     */
    public static void debugPrintNodes(Node nodes, String label)
    {
        if (!debugging)
        {
            return;
        }

        int count = 0;
        Iterator nodeIterator = nodes.iterator();
        while (nodeIterator.hasNext())
        {
            System.out.println(label + "-node[" + count++ + "] = " + nodeIterator.next());
        }




    }


    // use strictly for debugging
    public static void printNodeList(Node listofNodes)
    {
        if(!debugging)
            return;

        Node currentnode = listofNodes.getFirstNode();
        System.out.print(currentnode.getNodeValue() + ", ");
        while (!currentnode.isLastNode())
        {
            currentnode = currentnode.getNextNode();
            System.out.print(currentnode.getNodeValue() + ", ");
        }
        System.out.println();
    }

}
