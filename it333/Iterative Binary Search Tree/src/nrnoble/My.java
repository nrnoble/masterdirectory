package nrnoble;
/*
* Neal Noble
* May 2017
* Assignment: Trees Part2
* Instructor: Josh Archer
*/


/**
 * This class is used for developing and debugging small sections of code
 */
public class My
{

    public My()
    {

    }

    // A binary tree node
    class Node <T>
    {
        T NodeData;
        Node leftNode;
        Node rightNode;

        Node(T nodeData)
        {
            NodeData = nodeData;
            leftNode = null;
            rightNode = null;
        }
    }


    public Node bsTree(int arr[], int start, int end)
    {
        if (start > end)
        {
            return null;
        }
        int mid = (start + end) / 2;
        System.out.println("arr[" + mid + "]:" + arr[mid]);
        Node node = new Node(arr[mid]);
        node.leftNode = bsTree(arr, start, mid-1);
        node.rightNode = bsTree(arr, mid + 1, end);
        return node;
    }




}
