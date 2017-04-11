package part1;

import java.io.IOException;
import java.security.NoSuchAlgorithmException;
import java.util.*;

/**
 * Created by Neal on 4/8/2017.
 */
public class Node {

    private Object value;
    private boolean isFirstNode;
    private static Node firstNode = null;
    private static Node lastNode = null;
    private Node nextNode = null;
    private Node PreviousNode = null;
    private int nodeIndex = 0;
    private int nodeCount = 0;
    private String hash;
    private boolean isTheLastNode;
    public static int staticCounter =0;

    /**
     *
     * @param _value any object
     * @throws IOException
     * @throws NoSuchAlgorithmException
     */
    public Node (Object _value)
    {
        value = _value;
        hash = ShaHash.getShaHash(value);
        isFirstNode = true;
        isTheLastNode = true;
        firstNode = this;
        lastNode = this;
        nodeIndex = 1;
       // nodeCount = 1;

    }

    public Node (Node _theLastNode, Object element)
    {

        value = element;
        hash = ShaHash.getShaHash(element);
        this.setPreviousNode(_theLastNode);
        _theLastNode.setNextNode (this);
        _theLastNode.setLastNode(this);
        _theLastNode.isLastNode(false);

    }



    /**
     *
     * @param obj any object
     * @throws IOException
     * @throws NoSuchAlgorithmException
     */
    public Node addNode (Object obj)
    {


        // check if nodes are equal, if true, skip adding.
        if (isEqual(obj))
        {
            return null;
        }





        Node newNode = new Node(this,obj);
        this.setNextNode(newNode);
        //newNode.setPreviousNode(lastNode);
        //lastNode.nextNode = newNode;
       // this.setLastNode(newNode);


//        this.nextNode = newNode;
 //       newNode.PreviousNode = this;
   //     this.isTheLastNode = false; // clear last node
        newNode.nodeIndex = ++nodeIndex;

        return newNode;
    }

    /**
     * remove node from chain
     * @param element value
     * @return true if element was removed
     */
    public boolean remove(Object element)
    {
        Node searchNode;
        searchNode = findNode(element);

        if (searchNode.isFirstNode)
        {
            Node newFirstNode = searchNode.getNextNode();
            newFirstNode.isFirstNode = true;
            firstNode = newFirstNode;
            nodeCount--;
            return true;
        }


        if (searchNode.isTheLastNode)
        {
            Node newFirstNode = searchNode.getPreviousNode();
            newFirstNode.isTheLastNode = true;
            lastNode = newFirstNode;
            nodeCount--;
            return true;
        }


        if (searchNode != null)
        {
            Node PreviousNode =  searchNode.getPreviousNode();
            Node nextNode =  searchNode.getNextNode();
            PreviousNode.setNextNode(nextNode);
            nextNode.setPreviousNode(PreviousNode);
            nodeCount--;
            return true;
        }

        return false;
    }




    /**
     * Reset the the node chain
     */
    public void clear()
    {
        this.nodeIndex = 0;
        this.firstNode = null;
        this.lastNode = null;
    }


    /**
     * Find an element in chain by value
     * @param element value
     * @return node with the current element value
     */
    public Node findNode(Object element)
    {

        String elementHash = ShaHash.getShaHash(element);

        Node currentNode = this.firstNode;
        while (!currentNode.hash.equals(elementHash))
        {
            if (!currentNode.isLastNode())
                currentNode = currentNode.getNextNode();
            else
            {
                return null;
            }
        }

        return currentNode;
    }




    /**
     *
     * @param obj any object
     * @return true of objects have the same hash code
     * @throws IOException
     * @throws NoSuchAlgorithmException
     */
    public boolean isEqual (Object obj)
    {
        String objHash = null;

            objHash = ShaHash.getShaHash(obj);

        if (this.hash.equals(objHash))
        {
            return true;
        }

        return false;
    }

    /**
     * Set value to return if this is the last node in linked list
     * @param _value Set to true if this is the last node in linked list
     */
    public void isLastNode (boolean _value)
    {
        isTheLastNode = _value;
    }

     /**
     * Check to deteremine if this is the last node in Linked List
     * @return True or false
     */
    public boolean isLastNode ()
    {
        return isTheLastNode;
    }


    public boolean isFirstNode ()
    {
        return isFirstNode;
    }



    /**
     * If not last Node in list, return the next node.
     * @return the next node
     */
    public Node getNextNode()
    {
        if (!this.isTheLastNode)
            return this.nextNode;

        return null;
    }


    /**
     * Is the first node in chain
     * @param _node first node in chain
     */
    public void setFirstNode(Node _node)
    {
        _node.isFirstNode = true;
        this.firstNode = _node;
    }


    public Node getFirstNode()
    {
        return this.firstNode;
    }


    /**
     * Set the last node in chain
     * @param _node is the last node in chain
     */
    public void setLastNode(Node _node)
    {
        _node.isTheLastNode = true;
        this.lastNode = _node;
    }


    /**
     * Get the last node in chain
     * @return the last node in chain
     */
    public Node getLastNode()
    {

        return this.lastNode;
    }


    /**
     * Get the prervious node in chain
     * @return previous node in chain
     */
    public Node getPreviousNode()
    {
        return this.PreviousNode;
    }


    /**
     * Set the prervious node in chain
     * @return previous node in chain
     */
    public Node setPreviousNode(Node _node)
    {
        return this.PreviousNode = _node;
    }


    /**
     * Set the next node in chain
     * @return next node in chain
     */
    public Node setNextNode(Node _node)
    {
        return this.nextNode = _node;
    }




    /**
     * Return the value of current node
     * @return current node
     */
    public Object getNodeValue()
    {
        return this.value;
    }


//    public int getNodeCount()
//    {
//        return this.nodeCount;
//    }
}
