/**
 * Created by Neal on 3/28/2016.
 */
public class Node
{
    private Node right = null;
    private Node left = null;
    private Node parent = null;
    private Integer value = null;
    private Boolean isTopNode = null;
    private int duplicateValueCount = 1;
    protected int totalNodes  = 0;

    public Node(int _value)
    {
        this.value = _value;
    }

    public void newNode(Integer _value)
    {
        Node node = new Node(_value);
        addNode(node);
    }

    private void addNode(Node _node)
    {
        if (this.value == _node.getValue())
        {
            this.duplicateValueCount++;
            return;
        }


        if (this.value > _node.getValue())
        {
            if (this.getLeft() != null)
            {
                this.addNode(_node);
            }
            else
            {
                this.setLeft(_node);
                return;
            }
        }


        if (this.value < _node.getValue())
        {
            if (this.getRight() != null)
            {
                this.addNode(_node);
            }
            else
            {
                this.setRight(_node);
                return;
            }
        }

    }

    public Node(Node _right, Node _left, Node _parent, Integer _value)
    {
        this.right      = _right;
        this.left       = _left;
        this.parent     = _parent;
        this.value      = _value;
    }




    public Node getRight()
    {
        return right;
    }

    public void setRight(Node right)
    {
        this.right = right;
    }

    private Node getLeft()
    {
        return left;
    }

    private void setLeft(Node left)
    {
        this.left.setParent(this);
        this.left = left;
    }

    public Node getParent()
    {
        return parent;
    }

    private void setParent(Node parent)
    {
        this.parent = parent;
    }

    public int getValue()
    {
        return value;
    }

    public void setValue(int value)
    {
        this.value = value;
    }

    public void traverseDown()
    {
        if (this.getRight() != null)
        {
            this.getRight().traverseDown();
        }

        if (this.getLeft() != null)
        {
            this.getLeft().traverseDown();
        }

        System.out.println(this.value);
    }

    public void traverseUp()
    {
        if (this.getParent().getLeft() == null)
        {
            System.out.println(this.value);
            this.getParent().traverseUp();
        }

        this.traverseDown();


    }





}
