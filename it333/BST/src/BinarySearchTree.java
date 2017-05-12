import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Stack;





public class BinarySearchTree<T extends Comparable <T>> implements Iterable <T>
{
    private Node root;
    private int size;

    public BinarySearchTree() {
        // do nothing
    }

    public void add(T element) {
        if (root == null)
        {
            root = new Node(element);
            size++;
        } else
        {
            root = add(element, root);
        }
    }

    private Node add(T element, Node current)
    {
        if (current == null) {
            size++;
            return new Node(element);
        }

        int compare = current.data.compareTo(element);
        if (compare < 0) {
            current.right = add(element, current.right);

        } else if (compare > 0) {
            current.left = add(element, current.left);
        }

        return current;

    }


    public boolean contains(T element) {
        return contains(element, root);
    }

    public boolean contains(T element, Node current) {

        if (current == null)
        {
            return false;
        }

        int compare = current.data.compareTo(element);
        if (compare < 0)
        {
            return contains(element, current.right);

        }
        else if (compare > 0)
        {
            return contains(element, current.left);
        }
        else
        {
            return true;
        }
    }

    public void remove(T element) {
        root = remove(element, root);
    }

    private Node remove(T element, Node current)
    {
        if (current == null)
        {
            return null;
        }

        int compare = current.data.compareTo(element);

        if (compare < 0)
        {
            current.right = remove(element, current.right);
        }
        else if (compare > 0)
        {
            current.left = remove(element, current.left);
        }
        else
        {
            if (current.left != null && current.right != null)
            {
                Node maxLeft = findMax(current.left);
                current.data = maxLeft.data;
                current.left = remove(maxLeft.data, current.left);
            }
            else if (current.left != null)
            {
                current = current.left;
                size--;
            }
            else if (current.right != null)
            {
                current = current.right;
                size--;
            }
            else
            {
                size--;
                current = null;
            }



        }
        return current;
    }

    private Node findMax(Node current)
    {
        if (current.right != null)
        {
            return findMax(current.right);
        }
        return current;
    }



    public int size()
    {

        return size;
    }

    public boolean isEmpty()
    {
        return size == 0;
    }



    public void  clear()
    {
        root = null;
        size =0;
    }



    public  void inOrder()
    {
        inOrder(root);
    }

    private   void inOrder(Node current)
    {
        if (current != null)
        {
            inOrder(current.left);
            System.out.println(current.data);
            inOrder(current.right);
        }
    }



    public  void postOrder()
    {
        postOrder(root);
    }

    private   void postOrder(Node current)
    {
        if (current != null)
        {
            postOrder(current.left);
            postOrder(current.right);
            System.out.println(current.data);

        }
    }


    public  void preOrder()
    {
        preOrder(root);
    }

    private   void preOrder(Node current)
    {
        if (current != null)
        {
            System.out.println(current.data);
            preOrder(current.left);
            preOrder(current.right);
        }
    }


    public List<T> toList()
    {
        List<T> results = new ArrayList <>();
        toList(root, results);
        return results;
    }

    private void toList(Node current, List<T> results)
    {
        if (current != null)
        {
            inOrder(current.left);
            results.add(current.data);
            inOrder(current.right);
        }
    }


    @Override
    public Iterator<T> iterator()
    {
        return new BSTIterator(root);
    }


    private class BSTIterator implements Iterator<T>
    {
        private Stack<Node> stackOfNodes = new Stack<>();

        public BSTIterator (Node currentNode)
        {
            while (currentNode != null)
            {
                stackOfNodes.push(currentNode);
                currentNode= currentNode.left;
            }
        }

        @Override
        public boolean hasNext()
        {
            return !stackOfNodes.isEmpty();
        }

        @Override
        public T next()
        {
            Node next = stackOfNodes.pop();

            if(next.right!= null)
            {
                stackOfNodes.push(next.right);
                Node currentNode = next.right;
                while (currentNode.left != null)
                {
                    stackOfNodes.push(currentNode.left);
                    currentNode = currentNode.left;
                }
            }

            return next.data;
        }
    }


    // tree node
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

