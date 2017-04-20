/*
 * Neal Noble
 * April 2017
 * Assignment: Linked List (Part 1)
 * Instructor: Josh Archer
 */


package part1;


/**
  * The node class is used to help create various data structures
  *
  * @author Neal Noble
  * @version 1.0
  */
public class Node1 {

    private Object value;
    private boolean isFirstNode;
    private static Node1 firstNode1 = null;
    private static Node1 lastNode1 = null;
    private Node1 nextNode1 = null;
    private Node1 previousNode1 = null;
    private int nodeIndex = 0;
    private int nodeCount = 0;
    private String hash;
    private boolean isTheLastNode;
    public static int staticCounter =0;

    
    /**
     * Constructor
     * @param element any object
     */
    public Node1(Object element)
    {
        value = element;
        hash = ShaHash.getShaHash(value);
        isFirstNode = true;
        isTheLastNode = true;
        firstNode1 = this;
        lastNode1 = this;
        nodeIndex = 1;
        nodeCount = 1;

    }
    

    /**
     * Constuctor
     * @param _theLastNode1 that is currently the last node.
     * @param element value of new node
     */
    public Node1(Node1 _theLastNode1, Object element)
    {
        value = element;
        hash = ShaHash.getShaHash(element);
        this.setPreviousNode1(_theLastNode1);
        _theLastNode1.setNextNode1(this);
        _theLastNode1.setLastNode(this);
        _theLastNode1.setLastNode(false);
    }


    /**
     * Add a new node at the end of chain
     * @param element value
     * @return the node that has been created.
     */
    public Node1 addNode (Object element)
    {
        // check if nodes are equal, if true, skip adding.
        if (isEqual(element))
        {
            return null;
        }

        Node1 newNode1 = new Node1(this,element);
        this.setNextNode1(newNode1);
        newNode1.nodeIndex = ++nodeIndex;
        return newNode1;
    }
    

    /**
     * remove node from chain
     * @param element value
     * @return true if element was removed
     */
    public boolean remove(Object element)
    {
        Node1 searchNode1;
        searchNode1 = findNode(element);

        if (searchNode1.isFirstNode)
        {
            Node1 newFirstNode1 = searchNode1.getNextNode1();
            newFirstNode1.isFirstNode = true;
            firstNode1 = newFirstNode1;
            nodeCount--;
            return true;
        }


        if (searchNode1.isTheLastNode)
        {
            Node1 newFirstNode1 = searchNode1.getPreviousNode1();
            newFirstNode1.isTheLastNode = true;
            lastNode1 = newFirstNode1;
            nodeCount--;
            return true;
        }


        if (searchNode1 != null)
        {
            Node1 previousNode1 =  searchNode1.getPreviousNode1();
            Node1 nextNode1 =  searchNode1.getNextNode1();
            previousNode1.setNextNode1(nextNode1);
            nextNode1.setPreviousNode1(previousNode1);
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
        this.firstNode1 = null;
        this.lastNode1 = null;
    }


    /**
     * Find an element in chain by value
     * @param element value
     * @return node with the current element value
     */
    public Node1 findNode(Object element)
    {

        String elementHash = ShaHash.getShaHash(element);

        Node1 currentNode1 = this.firstNode1;
        while (!currentNode1.hash.equals(elementHash))
        {
            if (!currentNode1. isLastNode())
                currentNode1 = currentNode1.getNextNode1();
            else
            {
                return null;
            }
        }

        return currentNode1;
    }




    /**
     *
     * @param element any object
     * @return true of objects have the same hash code
     */
    public boolean isEqual (Object element)
    {
        String objHash = null;

            objHash = ShaHash.getShaHash(element);

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
    public void setLastNode(boolean _value)
    {
        isTheLastNode = _value;
    }

    
     /**
     * Check to deteremine if this is the last node in Linked List
     * @return True or false
     */
    public boolean isLastNode()
    {
        return isTheLastNode;
    }
    

    /**
     * Check to determine if the node is the first node in chain
     * @return true if the node is the first node in chain
     */
    public boolean isFirstNode ()
    {
        return isFirstNode;
    }


    /**
     * If not last Node1 in list, return the next node.
     * @return the next node
     */
    public Node1 getNextNode1()
    {
        if (!this.isTheLastNode)
            return this.nextNode1;

        return null;
    }


    /**
     * Is the first node in chain
     * @param _node1 first node in chain
     */
    public void setFirstNode(Node1 _node1)
    {
        _node1.isFirstNode = true;
        this.firstNode1 = _node1;
    }

    
    /**
     * Get the first node in chain
     * @return first node in chain
     */
    public Node1 getFirstNode()
    {
        return this.firstNode1;
    }


    /**
     * Set the last node in chain
     * @param _node1 is the last node in chain
     */
    public void setLastNode(Node1 _node1)
    {
        _node1.isTheLastNode = true;
        this.lastNode1 = _node1;
    }


    /**
     * Get the last node in chain
     * @return the last node in chain
     */
    public Node1 getLastNode()
    {
        return this.lastNode1;
    }


    /**
     * Get the prervious node in chain
     * @return previous node in chain
     */
    public Node1 getPreviousNode1()
    {
        return this.previousNode1;
    }



    /**
     * Set the prervious node in chain
     * @param _node1 node
     */
    public void setPreviousNode1(Node1 _node1)
    {
        this.previousNode1 = _node1;
    }


    /**
     * Set the next node in chain
     * @param _node1 next node in chain
     */
    public void setNextNode1(Node1 _node1)
    {
        this.nextNode1 = _node1;
    }


    /**
     * Return the value of current node
     * @return current node
     */
    public Object getNodeValue()
    {
        return this.value;
    }

    /**
     * Get the number of nodes.
     * @return the current number of nodes in chain
     */
    public int getNodeCount()
    {
        return this.nodeCount;
    }
}
