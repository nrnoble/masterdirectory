package nrnoble;

/**
 * This class is used for trying out code and ideas
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
