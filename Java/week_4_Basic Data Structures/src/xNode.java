// Neal R Noble
// IT333
// April 2016
// Exercises - Basic Data Structures


// Write routines to implement the standard linked list operations using lazy deletion.
// As a minimum you should write the add(x), remove(x), size(), isEmpty() and contains(x) methods.

public class xNode
{
    private boolean isDeleted = false;
    private xNode parent = null;
    private xNode child = null;
    private static int nodeCounter = 1;
    private Object item = null;

    public xNode (Object _item)
    {
        this.item = _item;
    }

    private xNode()
    {

    }


    public static xNode createNewNode (Object _item)
    {
        return new xNode(_item);
    }

    private boolean addNode (xNode _node)
    {

        this.parent = _node;
        _node.child = this;
        nodeCounter++;

        return true;
    }

    private boolean appendNode (xNode _node)
    {
        if (this.child == null)
        {
            this.child = _node;
            return true;
        }

        this.child.appendNode(_node);
        return  false;
    }

    public boolean add (Object _item)
    {
        xNode node  = createNewNode( _item);
        addNode(node);
        return true;
    }

    /**
     *
     * @return true if there are no child nodes
     */
    public boolean isEmpty()
    {
        if (nodeCounter  > 1 )
        {
            return false;
        }

        return true;
    }

    /**
     * size of list
     * @return number of nodes in list
     */
    public int size()
    {
        return nodeCounter;
    }


    /**
     * helper method. Find first object in list
     * @param _item object
     * @return xNode
     */
    private xNode findObject (Object _item)
    {
        if (this.item == _item && !this.isDeleted)
        {
            return this;
        }
        else if (this.child != null)
        {
            return this.child.findObject(_item);
        }

        return null;
    }


    /**
     * remove first item found in list
     * @param _item object
     * @return true if object is has been removed
     */
    public boolean remove (Object _item)
    {
        xNode node = findObject(_item);
        if (node!= null)
        {
            node.isDeleted = true;
            nodeCounter++;
            return true;
        }

        return false;
    }


    /**
     *
     * @param _item
     * @return
     */
    public boolean contains (Object _item)
    {
        xNode node = findObject(_item);
        if (node!= null)
        {
            return true;
        }

        return false;
    }





}
