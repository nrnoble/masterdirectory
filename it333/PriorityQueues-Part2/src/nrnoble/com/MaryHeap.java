package nrnoble.com;

import java.util.Arrays;
import java.util.NoSuchElementException;

/*
* Neal Noble
* May 2017
* Assignment: Priority queue
* Instructor: Josh Archer
*/

/**
 * Priority Queue
 * @param <T> NA
 */
public class MaryHeap<T extends Comparable<T>>
{

    private static final int RESIZE_FACTOR = 2;
    private static final int INITIAL_SIZE = 10;
    private static final int NUM_OF_CHILDREN = 3;
    private int numberOfChildren = NUM_OF_CHILDREN;
    private int heapSize = INITIAL_SIZE;
    private T[] data;


    // Constructor
    public MaryHeap(int heapCapacity, int numChild)
    {
    	// if number of children is less than two, set to default
        if (numChild < 2)
        {
            numChild = NUM_OF_CHILDREN;
        }

        // Ensure that heap size no smaller than default
        if (heapCapacity < INITIAL_SIZE)
        {
            heapCapacity = INITIAL_SIZE;
        }

        heapSize = 0;
        numberOfChildren = numChild;
        data = (T[])new Comparable[heapCapacity + 1];
        Arrays.fill(data, null);
    }



    /** Check if data is full **/
    private boolean isFull( )
    {
        return heapSize == data.length;
    }

    
    private MaryHeap()
    {
        // Do nothing
    }

    
    /**
     * Clear the Heap
     */
    public void clear( )
    {
        heapSize = 0;
    }

    
    /**
     *  Insert element into Heap
     * @param element to be inserted into the heap
     */
    public void insert(T element)
    {
        if (isFull( ) )
        {
            //throw new NoSuchElementException("Overflow Exception");
            resize();
        }
        data[heapSize++] = element;
        swim(heapSize - 1);
    }


    /**
     *  returns, but does NOT remove, the minimum element in the heap
     * @return the minimum element in the heap
     */
    public T peek()
    {
        if (this.size() == 0)
        {
            return null;

        }
        return data[0];
    }

    
    /**
     * Delete and return the top most element in the heap
     * @return T element  top most element
     */
    public T delMin()
    {
        // delete and return the top most item in the heap
        return delete(0);
    }


    /**
     * Get the number of elements in the heap
     * @return the number of elements in the heap
     */
    public int size()
    {
        return heapSize;
    }



    /* Check if the empty has no elements
    * @return true if data is empty
    */
    public boolean isEmpty( )
    {
        return heapSize == 0;
    }


    /**
     * Searches for a specific element in the heap.
     * @param  element to be searched
     * @return true if element is found
     */
    //TODO: Needs to be written to be significantly faster.
    public boolean contains(T element)
    {
        for (int i = 0; i < this.heapSize ; i++)
        {
            if (element.compareTo(data[i]) == 0)
            {
                return true;
            }
        }
        return false;
    }


    /**
     * Searches for a specific element in the heap.
     * @param  element to be searched
     * @return index of element is found
     */
    //TODO: Needs to be written to be significantly faster.
    public int findElementIndex(T element)
    {
        for (int i = 0; i < this.heapSize ; i++)
        {
            if (element.compareTo(data[i]) == 0)
            {
                return i;
            }
        }
        return -1;
    }


    /*
     *  find least smallest element
     * @return the element at the top of the data
     */
    public T findMin( )
    {
        if (isEmpty() )
        {
            throw new NoSuchElementException("Overflow Exception");
        }
        return data[0];
    }


    /**
     * Find the largest element in heapp
     * @return the largest element
     */
    public T findMax()
    {
        return data[this.heapSize-1];
    }


    /**
     * Delete the largest element in heap
     * @return the largest element in heap
     */
    public T delMax()
    {
        return delete(this.heapSize-1);
    }



    /**
     * Delete element at a specific index. Heap will reorder itself
     * @param index of the element to be deleted
     * @return T element
     */
    public T delete(int index)
    {
        if (isEmpty() )
        {
            return null;
        }
        T element = data[index];
        data[index] = data[heapSize - 1];
        heapSize--;
        sink(index);
        return element;
    }





    // element will swim up the heap until it finds the correct location
    private void swim(int childIndex)
    {
        T currentChild = data[childIndex];
        T currentParent = data[getParentIndex (childIndex)];
        while (childIndex > 0 && currentChild.compareTo(currentParent) < 0)
        {
            data[childIndex] = data[ getParentIndex (childIndex) ];
            childIndex = getParentIndex (childIndex);
        }
        data[childIndex] = currentChild;
    }



     /**
     * element will sink down the heap until it finds the correct location
     * between elements that where the parent is larger, and elements below are smaller.
     */
    private void sink(int sinkIndex)
    {
        int smallestChildIndex;
        T currenentElement = data[ sinkIndex ];
        while (getChildIndex(sinkIndex, 0) < heapSize)
        {
            smallestChildIndex = getIndexOfSmallestChild(sinkIndex);
            if (data[smallestChildIndex].compareTo(currenentElement) < 0)
                data[sinkIndex] = data[smallestChildIndex];
            else
                break;
            sinkIndex = smallestChildIndex;
        }
        data[sinkIndex] = currenentElement;
    }



    /**
     * Get index smallest child of the parent.
     *
     * **/
    private int getIndexOfSmallestChild(int index)
    {
        int childIndex1 =  getChildIndex(index, 0);
        int childPosition = 1;
        int childIndex2 = getChildIndex(index, childPosition);
        while ((childPosition <= numberOfChildren) && (childIndex2 < heapSize))
        {
         // System.out.println("while ((childPosition[" + childPosition +"] <= numberOfChildren [" + numberOfChildren + "]) && (childIndex2[" + childIndex2 + "] < heapSize[" + heapSize+"]))");
            if (data[childIndex2].compareTo(data[childIndex1]) < 0)
            {
                childIndex1 = childIndex2;
            }
            childIndex2 = getChildIndex(index, childPosition++);
         // System.out.println("returning: " + childIndex1);
        }
         // System.out.println("returning: " + childIndex1);
         // printHeap();
        return childIndex1;
    }


    /**
     * resize internal array when called
     */
    private void resize()
    {
        // data = Arrays.copyOf(data, data.length * RESIZE_FACTOR);

        T[] newData = (T[])new Comparable[data.length * RESIZE_FACTOR];

        //copy across all elements
        for (int i = 0; i < data.length; i++)
        {
            newData[i] = data[i];
        }

        data = newData;


    }

    
// TODO: Remove 
//    private void swap(int first, int second)
//    {
//    //  System.out.println("Swapping data[" + first + "] " + data[first] + " <--> " + data[second] + " data[" + second + "]");
//        T temp = data[first];
//        data[first] = data[second];
//        data[second] = temp;
//    }

    /**
     * Get the parent index of child
     * parent -1 / number of children
     */
    private int getParentIndex (int childIndex)
    {
        return (childIndex - 1)/ numberOfChildren;
    }


    /**
     * Get the child index in heap
     * Number of children under parent / Parent Index + child position under parent
     */
    private int getChildIndex(int parentIndex, int childnum)
    {
        return numberOfChildren * parentIndex + childnum;
    }


    /**  print data **/

    public void printHeap()
    {
        System.out.print("MaryHeap Order: ");
        for (int index = 0; index < heapSize-1; index++)
        {
            System.out.print("[" + index + "]:" + data[index] + ", ");
        }
        System.out.print("[" + (heapSize-1) + "]:" + data[heapSize-1]);
        System.out.println();
        return;
    }
}
