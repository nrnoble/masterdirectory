//package edu.greenriver.it.heaps;

import java.util.*;

public class EmptyHeap<T> implements Queue<T>
{
    private static final int DEFAULT_INITIAL_CAPACITY = 11;
    private transient Object[] queue;

    // The number of elements in the priority queue.
    private int size = 0;

    //The number of times this priority queue has been structurally modified.
    private transient int modCount = 0;


    /**
     * The comparator, or null if priority queue uses elements'
     * natural ordering.
     */
    private final Comparator<? super T> comparator;


    /**
     * The index of the element at the head of the deque (which is the
     * element that would be removed by remove() or pop()); or an
     * arbitrary number equal to tail if the deque is empty.
     */
    transient int head;

    /**
     * The index at which the next element would be added to the tail
     * of the deque (via addLast(E), add(E), or push(E)).
     */
    transient int tail;



    public EmptyHeap()
    {
        this(DEFAULT_INITIAL_CAPACITY,null);
    }


    public EmptyHeap(int initialCapacity,
                     Comparator<? super T> comparator)
    {

        if (initialCapacity < 1)
            throw new IllegalArgumentException();
        this.queue = new Object[initialCapacity];
        this.comparator = comparator;
    }


    @Override
    public boolean add(T newElement)
    {
        if (newElement == null)
            throw new NullPointerException();
        modCount++;
        int i = size;
        if (i >= queue.length)
            grow(i + 1);
        size = i + 1;
        if (i == 0)
            queue[0] = newElement;
        else
            siftUp(i, newElement);
        return true;
    }


    @Override
    public T peek() //findMin() operation
    {
        if (size == 0)
            return null;
        return (T) queue[0];
    }

    @Override
    public T remove() //deleteMin() operation
    {
        removeAt(0);

//        int i = indexOf(o);
//        if (i == -1)
//            return false;
//        else {
//            removeAt(i);
//            return true;

        return (T) queue[0];

    }

    @Override
    public int size()
    {
        return 0;
    }

    @Override
    public boolean isEmpty()
    {

        return head == tail;
    }

    @Override
    public void clear()
    {
        modCount++;
        for (int i = 0; i < size; i++)
            queue[i] = null;
        size = 0;
    }


    private T removeAt(int i)
    {
        assert i >= 0 && i < size;
        modCount++;
        int s = --size;
        if (s == i)
            queue[i] = null;
        else {
            T moved = (T) queue[s];
            queue[s] = null;
            siftDown(i, moved);
            if (queue[i] == moved) {
                siftUp(i, moved);
                if (queue[i] != moved)
                    return moved;
            }
        }
        return null;
    }




    private int indexOf(Object o) {
        if (o != null) {
            for (int i = 0; i < size; i++)
                if (o.equals(queue[i]))
                    return i;
        }
        return -1;
    }

    private void grow(int minCapacity)
    {
        if (minCapacity < 0)
            throw new OutOfMemoryError();
        int oldCapacity = queue.length;

        int newCapacity = ((oldCapacity < 64)?
                ((oldCapacity + 1) * 2):
                ((oldCapacity / 2) * 3));
        if (newCapacity < 0)
            newCapacity = Integer.MAX_VALUE;
        if (newCapacity < minCapacity)
            newCapacity = minCapacity;
        queue = Arrays.copyOf(queue, newCapacity);
    }




        private void siftUp(int k, T x)
        {
            if (comparator != null)
                siftUpUsingComparator(k, x);
            else
                siftUpComparable(k, x);
        }

        private void siftUpComparable(int k, T x)
        {
            Comparable<? super T> key = (Comparable<? super T>) x;
            while (k > 0)
            {
                int parent = (k - 1) >>> 1;
                Object e = queue[parent];
                if (key.compareTo((T) e) >= 0)
                    break;
                queue[k] = e;
                k = parent;
            }
            queue[k] = key;
        }

        private void siftUpUsingComparator(int k, T x)
        {
            while (k > 0)
            {
                int parent = (k - 1) >>> 1;
                Object e = queue[parent];
                if (comparator.compare(x, (T) e) >= 0)
                    break;
                queue[k] = e;
                k = parent;
            }
            queue[k] = x;
        }

        /**
         * Inserts item x at position k, maintaining heap invariant by
         * demoting x down the tree repeatedly until it is less than or
         * equal to its children or is a leaf.
         *
         * @param k the position to fill
         * @param x the item to insert
         */
        private void siftDown(int k, T x)
        {
            if (comparator != null)
                siftDownUsingComparator(k, x);
            else
                siftDownComparable(k, x);
        }

        private void siftDownComparable(int k, T x)
        {
            Comparable<? super T> key = (Comparable<? super T>)x;
            int half = size >>> 1;
            while (k < half) {
                int child = (k << 1) + 1;
                Object c = queue[child];
                int right = child + 1;
                if (right < size &&
                        ((Comparable<? super T>) c).compareTo((T) queue[right]) > 0)
                    c = queue[child = right];
                if (key.compareTo((T) c) <= 0)
                    break;
                queue[k] = c;
                k = child;
            }
            queue[k] = key;
        }

        private void siftDownUsingComparator(int k, T x)
        {
            int half = size >>> 1;
            while (k < half) {
                int child = (k << 1) + 1;
                Object c = queue[child];
                int right = child + 1;
                if (right < size &&
                        comparator.compare((T) c, (T) queue[right]) > 0)
                    c = queue[child = right];
                if (comparator.compare(x, (T) c) <= 0)
                    break;
                queue[k] = c;
                k = child;
            }
            queue[k] = x;
        }



    //ignore methods below this
    //ignore methods below this
    //ignore methods below this
    //ignore methods below this
    //ignore methods below this
    //ignore methods below this
    //ignore methods below this

    @Override
    public boolean remove(Object search)
    {
        throw new UnsupportedOperationException("Method not supported.");
    }

    @Override
    public boolean contains(Object search)
    {
        throw new UnsupportedOperationException("Method not supported.");
    }

    @Override
    public T poll()
    {
        throw new UnsupportedOperationException("Method not supported.");
    }

    @Override
    public T element()
    {
        throw new UnsupportedOperationException("Method not supported.");
    }

    @Override
    public boolean offer(T e)
    {
        throw new UnsupportedOperationException("Method not supported.");
    }

    @Override
    public boolean addAll(Collection<? extends T> c)
    {
        throw new UnsupportedOperationException("Method not supported.");
    }

    @Override
    public boolean containsAll(Collection<?> c)
    {
        throw new UnsupportedOperationException("Method not supported.");
    }

    @Override
    public boolean removeAll(Collection<?> c)
    {
        throw new UnsupportedOperationException("Method not supported.");
    }

    @Override
    public boolean retainAll(Collection<?> c)
    {
        throw new UnsupportedOperationException("Method not supported.");
    }

    @Override
    public Iterator<T> iterator()
    {
        throw new UnsupportedOperationException("Method not supported.");
    }

    @Override
    public Object[] toArray()
    {
        throw new UnsupportedOperationException("Method not supported.");
    }

    @Override
    public <T> T[] toArray(T[] a)
    {
        throw new UnsupportedOperationException("Method not supported.");
    }
}
