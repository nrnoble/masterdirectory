package nrnoble.com;

import java.util.Arrays;

public class MarryHeap<T extends Comparable<T>>
{
    private static final int RESIZE_FACTOR = 2;
    private static final int maryNum = 3;
    private static final int INIT_SIZE = 10;
    //the m-ary tree is stored in this array
    private T[] data;
    private int size = 0;
    @SuppressWarnings("unchecked")
    public MarryHeap()
    {
        data = (T[]) new Comparable[INIT_SIZE];
    }
    public void insert(T element)
    {

    // check if we need to resize
        if (size >= data.length - 1)
        {
            resize();
        }
// ***********************************
//  Broken
//        size++;
//        data[size] = element;
//        swim(size);
// **********************************

        // add the new element
        // Fix

        data[size++] = element;
        swim(size -1);




    }
    public T peek()
    {
        // returns, but does NOT remove, the minimum element in the heap
        return data[0];
    }
    public T delMin()
    {
        if (isEmpty())
        {
            return null;
        }

        // save our result
        T result = data[0];
        data[0] = null;

        // move the top index to the root of the tree
        swap(0, size-1);
        size--;
        sink(0);

        return result;
    }


    public int size()
    {
        //returns the number of elements in the heap
        return size;
    }



    @SuppressWarnings("unchecked")
    private void resize()
    {
    // T[] newData = (T[])new Comparable[data.length * RESIZE_FACTOR];
    //
    // //copy across all elements
    // for (int i = 0; i < data.length; i++)
    // {
    // newData[i] = data[i];
    // }
        data = Arrays.copyOf(data, data.length * RESIZE_FACTOR);
    //data = newData;
    }



    public boolean isEmpty()
    {
//returns true if the heap is empty, otherwise false
        return size == 0;
    }
    public boolean contains(T element)
    {
        for(int index = 0; index < size; index++)
        {
            if(element.equals(data[index]))
            {
                return true;
            }
        }
        return false;
    }


    private void swim1(int index)
    {
//stop when we reach the root (index 1)
        while (index > 1)
        {
            //int parentIndex = (index + 1 )/maryNum;
            int parentIndex = getParentIndex(index);
            if (data[index].compareTo(data[parentIndex]) < 0)
            {
                swap(index, parentIndex);
            }
            index = parentIndex;
        }
    }


    private int getParentIndex (int childIndex)
    {
        return (childIndex - 1)/ maryNum;
    }


    private void swim2(int index)
    {
    // stop when we reach the root (index 1)
        while (index >0)
        {
            //int parentIndex = (index + 1 )/maryNum;
            int parentIndex = getParentIndex(index);
            if (data[index].compareTo(data[parentIndex]) < 0)
            {
                swap(index, parentIndex);
            }
            if (data[index].compareTo(data[parentIndex]) < 0)
            {
                //sink((int) data[index]);
                sink(index);
            }
            index = parentIndex;
        }
    }

    private void swim(int index)
    {
        while (index >0)
        {
            int parentIndex = getParentIndex(index);
            if (data[index].compareTo(data[parentIndex]) < 0)
            {
                swap(index, parentIndex);
            }
            if (data[index].compareTo(data[parentIndex]) < 0)
            {
                //sink((int) data[index]);
                sink(index);
            }
            index = parentIndex;
        }
    }


    public void sinkAll()
    {
        T[] data2  = (T[]) new Comparable[size];

        int index = 0;
        while (!this.isEmpty())
        {
            T result = delMin();
            data2[index] = result;
            index++;
//            System.out.print(String.format("%03d", ((String)result) )  + " ");
//            sink((Integer) result);
//            this.insert(result);
        }

        data = data2;
        size = data2.length;
        this.printHeap();

        index = 0;
        data2 = (T[]) new Comparable[size];
        while (!this.isEmpty())
        {
            T result = delMin();
            data2[index] = result;
            index++;
        }

        data = data2;
        size = data2.length;
        this.printHeap();


        this.printHeap();
    }


    private int getIndexOfSmallestChild(int parentIndex)
    {
        int childIndex1 = parentIndex + 1;
        int childIndex2 = parentIndex + 2;
        int childIndex3 = parentIndex + 3;

        T child1Value = null;
        T child2Value = null;
        T child3Value = null;

        int smallestChildIndex = parentIndex;
        T smallestValue = (T) data[parentIndex];

        // if parent is the last element, then parent has no children
        if (parentIndex == size-1)
        {
            return parentIndex;
        }

        // check if first childIndex is less than last index
        if (childIndex1 <= size-1)
        {
            child1Value = (T) data[childIndex1];
            if (child1Value == null)
            {
                return parentIndex;
            }

            if (child1Value.compareTo(smallestValue) < 0)
            {
                smallestChildIndex = childIndex1;
                smallestValue = child1Value;
            }
        }


        // check if second childIndex is less than last index
        if (childIndex2 <= size-1)
        {
            child2Value = (T) data[childIndex2];
            if (child2Value == null)
            {
                return smallestChildIndex;

            }
            if (child2Value.compareTo(smallestValue) < 0)
            {
                smallestChildIndex = childIndex2;
                smallestValue = child2Value;
            }


        }

        // check if third childIndex is less than last index
        if (childIndex3 <= size-1)
        {
            child3Value = (T) data[childIndex3];
            if (child3Value == null)
            {
                return smallestChildIndex;
            }
            if (child3Value.compareTo(smallestValue) < 0)
            {
                smallestChildIndex = childIndex3;
                smallestValue = child3Value;
            }
        }

        return smallestChildIndex;
    }



    private void sink(int index)
    {
        while (index <= size / maryNum)
        {
          //  System.out.print(index + " ");

//            int left = maryNum * index - 1;
//            int mid = maryNum * index;
//            int right = maryNum * index + 1;

            int left = maryNum  * index + 1 ;
            int mid = maryNum   * index + 2;
            int right = maryNum * index + 3;
            int indexToCheck = left;

            int smallestChildIndex = getIndexOfSmallestChild(index);

            if (index != smallestChildIndex)
            {
                swap(index,smallestChildIndex);
                index = smallestChildIndex;

            }
            else
            {
                break;
            }

//            if(mid < data.length && data[mid] != null && data[mid].compareTo(data[left]) < 0)
//            {
//                indexToCheck = mid;
//            }
//            // if there is a right child and it is the smaller child
//            else if (right < data.length && data[right] != null &&
//                    data[right].compareTo(data[left]) < 0)
//            {
//                indexToCheck = right;
//            }
//
//            // compare the parent with the smallest child
//            if (data[indexToCheck].compareTo(data[index])  < 0 )
//            {
//                swap(indexToCheck, index);
//                index = indexToCheck;
//            }
//            else
//            {
//                break;
//            }
        }
    }
//    private void sink1(int index)
//    {
//        while (index <= size / maryNum)
//        {
//          //  System.out.print(index + " ");
//
////            int left = maryNum * index - 1;
////            int mid = maryNum * index;
////            int right = maryNum * index + 1;
//
//            int left = maryNum * index + 1 ;
//            int mid = maryNum * index + 2;
//            int right = maryNum * index + 3;
//            int indexToCheck = left;
//            if(mid < data.length && data[mid] != null && data[mid].compareTo(data[left]) < 0)
//            {
//                indexToCheck = mid;
//            }
//            // if there is a right child and it is the smaller child
//            else if (right < data.length && data[right] != null &&
//                    data[right].compareTo(data[left]) < 0)
//            {
//                indexToCheck = right;
//            }
//
//            // compare the parent with the smallest child
//            if (data[indexToCheck].compareTo(data[index])  < 0 )
//            {
//                swap(indexToCheck, index);
//                index = indexToCheck;
//            }
//            else
//            {
//                break;
//            }
//        }
//    }


    private void swap(int first, int second)
    {
        T temp = data[first];
        data[first] = data[second];
        data[second] = temp;
    }


//    /**  print data **/
//    public void printHeap1()
//    {
//        System.out.print("MarryHeap Order: ");
//        for (int index = 0; index < size; index++)
//        {
//            System.out.print("[" + String.format ("%02d", index) + "]:" + String.format ("%02d", data[index])  + ", ");
//        }
//        System.out.print("[" + (String.format ("%02d", size)) + "]:" + data[size-1]);
//        System.out.println();
//        return;
//    }


    public void printHeap()
    {
        if (this.isEmpty())
        {
            System.out.println("heap size : " + this.size());
            return;
        }

        System.out.print("MaryHeap Order: ");
        for (int index = 0; index < size-1; index++)
        {
            System.out.print("[" + String.format ("%03d", index) + "]:" + String.format ("%03d", data[index])  + ", ");
        }
        System.out.print("[" + (String.format ("%03d", size-1)) + "]:" + String.format ("%03d",  data[size-1] )  + ", ");
        System.out.println();
        return;
    }
}





