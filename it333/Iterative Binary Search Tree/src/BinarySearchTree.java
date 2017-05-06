import sun.plugin2.applet.context.NoopExecutionContext;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Stack;

// Done - The addUpdate() method adds a new element to your tree or updates an existing element.
// Done - The size(), isEmpty() and clear() methods correctly track or remove elements in the BST.
// Done - The inOrder() method returns an ordered list of unique elements from the BST.
// Done - Your informal tests on the BST test each of the listed scenarios.


public class BinarySearchTree<T extends Comparable<T>>
{
    private Node root;
    private int size;

    public BinarySearchTree()
    {

    }

    /**
     * Adds or updates an element in the binary search tree.
     * @param element to be added or updated.
     * @return  true when a new element is added and false if an update occurred.
     */
    public boolean addUpdate(T element)
    {
        Node node = new Node(element);

        if (this.root == null)
        {
            this.root = node;
            size++;
            return true;
        }

        Node currentNode = this.root;

        while (true)
        {
            int compare = currentNode.data.compareTo(element);
            if (compare > 0)
            {
                if (currentNode.left != null)
                    currentNode = currentNode.left;
                else
                {
                    currentNode.left = node;
                    size++;
                    break;
                }
            }
            else if (compare < 0)
            {
                if (currentNode.right != null)
                    currentNode = currentNode.right;
                else
                {
                    currentNode.right = node;
                    size++;
                    break;
                }
            }
            else
            {
                currentNode.data = node.data;
                size++;
                break;
            }
        }
        return true;
    }


    /**
     * Searches Binary tree for an element.
     * @param element that is to be searched for in tree
     * @return
     */
    public boolean contains(T element)
    {
        Node currentNode;
        currentNode = this.root;

        while (currentNode != null)
        {
            int compare = currentNode.data.compareTo(element);
            if (compare > 0)
            {
                if (currentNode.left != element)
                    currentNode = currentNode.left;
            }
            else if (compare < 0)
            {
                if (currentNode.right != element)
                    currentNode = currentNode.right;
            }
            else
            {
                return true;
            }
        }
        return false;
    }


    /**
     * Gets the value associated with the input element key. If no key is found this method will return null.
     * @param element key pair
     * @return the value associated with the input key. If no key is found this method will return null.
     */
    public T get(T element)
    {
        Node currentNode;
        currentNode = this.root;

        while (currentNode != null)
        {
            int compare = currentNode.data.compareTo(element);
            if (compare > 0)
            {
                if (currentNode.left != element)
                    currentNode = currentNode.left;
            }
            else if (compare < 0)
            {
                if (currentNode.right != element)
                    currentNode = currentNode.right;
            }
            else
            {
                return currentNode.data;
            }
        }
        return null;
    }


    /**
     * 	The number of elements in the tree.
     * @return 	the number of elements in the tree.
     */
    public int size()
    {
        return size;
    }


    /**
     * This returns true if there are no elements in the tree, but otherwise returns false.
     * @return true if there are not elements, otherwise false.
     */
    public boolean isEmpty()
    {
        return size == 0;
    }


    /**
     * This removes all elements in the tree. Sets size to zero
     */
    public void clear()
    {
        root = null;
        size = 0;
    }


    /**
     * Returns a sorted list of all elements in the tree, using the In-Order tree traversal of the underlying structure.
     * @return a sorted list of all elements
     */
    public  List<T> postOrder()
    {
        List<T> elementList = new ArrayList<T>();
       return postOrder(this.root, elementList);
    }


    private  List<T> postOrder(Node currentNode, List<T> list)
    {
        Stack<Node> stackOfNodes = new Stack<>();

        while (true)
        {
            while (currentNode != null)
            {
                stackOfNodes.push(currentNode);
                currentNode = currentNode.right;
            }

            if (stackOfNodes.isEmpty())
            {
                return list;
            }
            
            currentNode = stackOfNodes.pop();
            list.add(currentNode.data);
            currentNode = currentNode.left;
        }
    }


    /**
     * Returns a Post order sorted list of all elements in the tree, using the post-Order tree traversal of the underlying structure.
     * @return order list of items
     */
    public  List<T> inOrder()
    {
        List<T> elementList = new ArrayList<T>();
        return inOrder(this.root, elementList);
    }

    private  List<T> inOrder(Node currentNode, List<T> list)
    {
        Stack<Node> stackOfNodes = new Stack<>();

        while (true)
        {
            while (currentNode != null)
            {
                stackOfNodes.push(currentNode);
                currentNode = currentNode.left;
            }

            if (stackOfNodes.isEmpty())
            {
                return list;
            }

            currentNode = stackOfNodes.pop();
            list.add(currentNode.data);
            currentNode = currentNode.right;
        }
    }

    /**
     * Returns a pre order sorted list of all elements in the tree, using the pre-Order tree traversal of the underlying structure.
     * @return List<T> of elements sorted in pre-order
     */
    public  List<T> preOrder()
    {
        List<T> elementList = new ArrayList<T>();
        return preOrder(this.root, elementList);
    }

    private  List<T> preOrder(Node currentNode, List<T> list)
    {
        Stack<Node> stackOfNodes = new Stack<>();
        stackOfNodes.push(currentNode);

        while (stackOfNodes.empty() == false)
        {
            currentNode = stackOfNodes.peek();
            list.add(currentNode.data);

            stackOfNodes.pop();

            if (currentNode.right != null)
            {
                stackOfNodes.push(currentNode.right);
            }

            if (currentNode.left != null)
            {
                stackOfNodes.push(currentNode.left);
            }
        }
            return list;
    }


    /**
     * create the iterator for the class
     * @return the iterator
     */
    public Iterator<T> iterator()
    {
        return new BSTIterator(root);
    }


    private class BSTIterator implements Iterator<T>
    {
        private Stack<Node> nodeStack = new Stack<>();

        public BSTIterator (Node current)
        {
            while (current != null)
            {
                nodeStack.push(current);
                current= current.left;
            }
        }

        @Override
        public boolean hasNext()
        {
            return !nodeStack.isEmpty();
        }


        @Override
        public T next()
        {
            Node next = nodeStack.pop();
            if(next.right!= null)
            {
                nodeStack.push(next.right);
                Node currentNode = next.right;
                while (currentNode.left != null)
                {
                    nodeStack.push(currentNode.left);
                    currentNode = currentNode.left;
                }
            }
            return next.data;
        }
    }


    private class Node
    {
        private T data;
        private Node left;
        private Node right;

        public Node (T data)
        {
            this.data=data;
        }

        public String toString()
        {
            String dataString = (data == null) ? "null": data.toString();
            String leftChild = (left == null) ? "null": left.data.toString();
            String rightChild = (right == null) ? "null": right.data.toString();

            return leftChild + " <--" + dataString + " --> " + rightChild;
        }
    }
}