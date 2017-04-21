/*
 * Neal Noble
 * April 2017
 * Assignment: Linked List (Part 1)
 * Instructor: Josh Archer
 */


package part2;


import part2.ShaHash;

import java.util.Iterator;
import java.util.NoSuchElementException;

import static javafx.scene.input.KeyCode.T;

/**
  * The node class is used to help create various data structures
  *
  * @author Neal Noble
  * @version 1.0
  */
@SuppressWarnings("unused")
public class Node<E> implements Iterable<E>
{


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

    // set to true when after removing an element.
    private static boolean resetIndex = false;

    
    /**
     * Constructor
     * @param element any object
     */
    public Node(Object element)
    {
        value = element;
        hash = ShaHash.getShaHash(value);
        isFirstNode = true;
        isTheLastNode = true;
        firstNode = this;
        lastNode = this;
        nodeIndex = 0;
        nodeCount = 0;
    }



    /**
     * Constuctor
     * @param currentNode that is currently the last node.
     * @param element value of new node
     */
    public Node(Node currentNode, Object element)
    {
        value = element;
        hash = ShaHash.getShaHash(element);
        this.setFirstNode(currentNode.getFirstNode());
        this.setLastNode(currentNode.getLastNode());

        if (currentNode.isLastNode())
        {
            this.setPreviousNode(currentNode);
            currentNode.setNextNode(this);
            currentNode.setLastNode(this);
            currentNode.setLastNode(false);
            resetIndex = true;
            return;
        }

        if (currentNode.isFirstNode())
        {
            this.setPreviousNode(currentNode);
            this.setLastNode(currentNode.getLastNode());
            this.setLastNode(currentNode.isTheLastNode);
            this.setNextNode(currentNode.getNextNode());

            currentNode.setNextNode(this);
            resetIndex = true;
            return;
        }


        Node previousNode = currentNode.getPreviousNode();
        Node nextNode = currentNode.getNextNode();

        this.setNextNode(currentNode);
        this.setPreviousNode(currentNode.getPreviousNode());
        previousNode.setNextNode(this);
        currentNode.setPreviousNode(this);
        resetIndex = true;
        return;

    }


    /**
     *
     * @param index location where to insert the new element
     * @param element value of new node
     */
    public Node(int index, Object element)
    {
        // find the node at the insert index
        // disconnect exiting node at index location
        // connect new node at index location
        // attach chain of nodes to new node.


        this.value = element;
        this.hash = ShaHash.getShaHash(element);
        Node currentIndexNode = lastNode.getNodeByIndex(index);


        Node previousNode = currentIndexNode.getPreviousNode();
       // Node nextNode = currentIndexNode.getNextNode();
        previousNode.setNextNode(this);
        this.setNextNode(currentIndexNode);
        currentIndexNode.setPreviousNode(this);

        if (index == firstNode.nodeIndex)
        {
            isFirstNode = true;
            firstNode = this;
        }

        if (index == firstNode.nodeIndex)
        {
            isFirstNode = true;
            lastNode = this;
        }

        this.nodeIndex = index;
        this.nodeCount = 0;

        // inserting a new value, thus chain needs to be reindexed
        resetIndex = true;

    }




    public Node addToLastNode (Object element)
    {

        Node newNode = new Node(lastNode,element);
        lastNode.setNextNode(newNode);
        newNode.nodeIndex = this.nodeIndex+1;
        return newNode;
    }



    /**
     * Add a new node at the end of chain
     * @param element value
     * @return the node that has been created.
     */
    public Node addNode (Object element)
    {
        // check if nodes are equal, if true, skip adding.
        if (isEqual(element))
        {
            return null;
        }

        Node newNode = new Node(this,element);
        this.setNextNode(newNode);
        newNode.nodeIndex = this.nodeIndex+1;
        return newNode;
    }



    public boolean isDuplicate(Object element)
    {
        Node currentNode = this.firstNode;
        if (currentNode.isEqual(element))
        {
            return true;
        }

        while (!currentNode.isTheLastNode)
        {
            currentNode  = currentNode.getNextNode();
            if (currentNode.isEqual(element))
            {
                return true;
            }
        }
        return false;

    }




    public Node addNode (Node insertNode, Object element)
    {
        // check if nodes are equal, if true, skip adding.
        if (isEqual(element))
        {
            return null;
        }

        Node newNode = new Node(insertNode,element);
        return newNode;
    }



    /**
     * remove node
     * @param node remove node from chain
     */
    public void remove (Node node)
    {
        if (node.isFirstNode)
        {
            Node newFirstNode = node.getNextNode();
            newFirstNode.isFirstNode = true;
            firstNode = newFirstNode;
            nodeCount--;
            resetIndex = true;
            return;
        }


        if (node.isTheLastNode)
        {
            Node newFirstNode = node.getPreviousNode();
            newFirstNode.isTheLastNode = true;
            lastNode = newFirstNode;
            nodeCount--;
            resetIndex = true;
            return;
        }


        if (node != null)
        {
            Node PreviousNode =  node.getPreviousNode();
            Node nextNode =  node.getNextNode();
            PreviousNode.setNextNode(nextNode);
            nextNode.setPreviousNode(PreviousNode);
            nodeCount--;
            resetIndex = true;
        }
    }



    /**
     * remove node from chain based on element value
     * @param element value
     * @return true if element was removed
     */
    public boolean remove(Object element)
    {
        Node searchNode;
        searchNode = findNode(element);
        remove(searchNode);
        return true;
    }


    /**
     * Reset the the node chain
     */
    public void clear()
    {
        this.nodeIndex = 0;
        this.firstNode = null;
        this.lastNode = null;
        this.resetIndex = true;

    }


    /**
     * Find an element in chain by value
     * @param element value
     * @return node with the current element value
     */
    public Node findNode(Object element)
    {

        String elementHash = ShaHash.getShaHash(element);

        Node currentNode = firstNode;
        while (!currentNode.hash.equals(elementHash))
        {
            if (!currentNode. isLastNode())
                currentNode = currentNode.getNextNode();
            else
            {
                return null;
            }
        }

        return currentNode;
    }



    /**
     * Find the node as a specific index
     * @param index of the node
     * @return
     */
    public Node getNodeByIndex(int index) {

        reIndex(true);

        if (index == 0)
        {
            return firstNode;
        }

            //TODO This is broken, causes problems when nodes are 3 or less
//        if (index == firstNode.nodeCount-1)
//        {
//            return lastNode;
//        }

        if (index >= firstNode.nodeCount)
        {
            return null;
        }

        Node  currentNode = firstNode;
        while (!currentNode.isLastNode())
        {
            currentNode = currentNode.getNextNode();
            if (currentNode.nodeIndex == index)
                return currentNode;
        }
            return null;
    }



    /**
     * Remove Node at a specific index
     * @param index of the node that will be removed
     */
    public void removeAtIndex(int index)
    {
        this.reIndex();
        Node  findResultNode = this.getNodeByIndex(index);
        remove(findResultNode);
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



    // Reindex occurs after a node has been added or removed, and then the
    // index value is accessed through getNodeIndex. Adding\removing sets
    // resetIndex to true. When get call getNodeIdex, it will reindex the
    // chain of node if resetIndex = true, or return the index value when
    // has been nodes added\removed.
    private void reIndex()
    {

        reIndex(resetIndex);
    }


    /**
     * reindex all elements in the chain
     * @param forceReindex if true force reindexing, otherwise only index when 'resetIndex' is true
     */
    private void reIndex(boolean forceReindex)
    {
        if (forceReindex)
        {
           // continue with a full re-indexing of all nodes;
        }
        else
        {
            // check if one or more nodes has been removed
            if (!resetIndex)
            {
                // if no nodes have been added\removed.
                return;
            }
        }

        int index = 0;
        Node currentNode = firstNode;
        firstNode.nodeCount++;
        currentNode.nodeIndex = index;
        while (!currentNode.isLastNode())
        {
            currentNode = currentNode.getNextNode();
            currentNode.nodeIndex = ++index;
            firstNode.nodeCount++;
        }
        resetIndex = false;
    }



    /**
     * Return the index of a specific element
     * @param element value
     * @return index of a specific element
     */
    public int getNodeIndex(Object element)
    {
        // do a reindex if nodes have been added\removed.
        this.reIndex();

        Node foundNode = this.findNode(element);

        if (foundNode == null)
        {
            return -1;
        }
        return this.getNodeIndex(foundNode);
    }



    /**
     * Return the index of a specific Node
     * @param node
     * @return index of node
     */
    public int getNodeIndex(Node node)
    {
        // do a reindex if nodes have been added\remove
        this.reIndex();
        return node.nodeIndex;
    }




    
    
    /**
     * Set value to return if this is the last node in linked list
     * @param _value Set to true if this is the last node in linked list
     */
    public void setLastNode(boolean _value)
    {
        resetIndex = true;
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
        resetIndex = true;
        _node.isFirstNode = true;
        this.firstNode = _node;
    }

    
    /**
     * Get the first node in chain
     * @return first node in chain
     */
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
        resetIndex = true;
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
     * @param _node node
     */
    public void  setPreviousNode(Node _node)
    {
        resetIndex = true;
        this.PreviousNode = _node;
    }


    /**
     * Set the next node in chain
     * @param _node next node in chain
     */
    public void setNextNode(Node _node)
    {
        resetIndex = true;
        this.nextNode = _node;
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
     * Set the value of node
     * @param element value
     */
    public void setNodeValue (Object element)
    {
        resetIndex = true;
        this.value = element;
    }


    /**
     * Get the number of nodes.
     * @return the current number of nodes in chain
     */
    public int getNodeCount()
    {
        firstNode.reIndex();
        return firstNode.nodeCount;
    }


    @Override
    public Iterator<E> iterator()
    {

        return new NodeIterator<>();
    }




    // Inner class example
    private class NodeIterator <T> implements Iterator<T>
    {

        private Node iNode;

        public NodeIterator()
        {
            this.iNode = firstNode;
        }




        public boolean hasNext()
        {
            if (iNode!=null)
            {
                return true;
            }
            return false;
        }

        public T next()
        {

            Object value1 =null;
            if (iNode.isLastNode())
            {
                value1 = iNode.getNodeValue();
                iNode = null;
                return (T)value1;
            }
            else
            {
                value1 = iNode.getNodeValue();
                iNode = iNode.getNextNode();
                return (T)value1;
            }

        }


        public T previous()
        {
            if(!iNode.isFirstNode)
            {
                iNode = iNode.getPreviousNode();
                return (T)iNode;
            }

            throw new NoSuchElementException();
        }

        public void remove()
        {
            Node rNode = iNode;
                    iNode.remove(rNode);

            //throw new UnsupportedOperationException();
        }
    }



}
