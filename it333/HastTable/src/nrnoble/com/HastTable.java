package nrnoble.com;

import java.util.*;

public class HastTable<T> implements Set<T>
{

    private static  final int DEFAULT_SIZE = 10;
    private static final double DEFAULT_LOAD_FACTOR = .6;

    private HashTableElement[] table;

    private double loadFactor;
    private int initialSize;

    private int size;
    private int usedSpace;
    private int modCount = 0;



    public HastTable()
    {
        this(DEFAULT_SIZE, DEFAULT_LOAD_FACTOR);
    }

    public HastTable(int initialSize, Double loadFactor)
    {
        table = new HashTableElement[initialSize];
        this.loadFactor = loadFactor;
        this.initialSize = initialSize;
    }



    @Override
    public boolean add(T element)
    {

        if ((double)usedSpace / table.length >= loadFactor )
        {
            rehash();
        }


        int index = Math.abs(element.hashCode()) % table.length;

        HashTableElement current = table[index];

        while (current != null)
        {
            if(current.element.equals(element) && !current.isEmpty)
            {
                return false;
            }

            index = (index +1) % table.length;
            current = table[index];
        }

        table[index] = new HashTableElement(element, false);
        size++;
        usedSpace++;
        modCount++;
        return false;

    }

    private void rehash()
    {
        HashTableElement[] oldTable = table;
        table = new HashTableElement[oldTable.length * 2];
        size = 0;

        for (int i = 0; i <oldTable.length ; i++)
        {
            if (oldTable[i] != null && !oldTable[i].isEmpty)
            {
                add((T)oldTable[i].element);
            }
        }
    }


    @Override
    public boolean remove(Object element)
    {

        int index = Math.abs(element.hashCode()) % table.length;

        HashTableElement current = table[index];

        while (current != null)
        {
            if(current.element.equals(element) && !current.isEmpty)
            {
                // delete
                current.isEmpty = true;
                size--;
                modCount++;
                return true;
            }

            index = (index +1) % table.length;
            current = table[index];
        }
        return false;
    }

    @Override
    public int size()
    {
        return size;
    }

    @Override
    public boolean isEmpty()
    {
        return size == 0;
    }

    @Override
    public boolean contains(Object element)
    {
        int index = Math.abs(element.hashCode()) % table.length;

        HashTableElement current = table[index];

        while (current != null)
        {
            if(current.element.equals(element) && !current.isEmpty)
            {

                return true;
            }

            index = (index +1) % table.length;
            current = table[index];
        }

        return false;
    }

    @Override
    public Iterator<T> iterator()
    {
        return new HashTableInterator(table, modCount);
    }


    private class HashTableInterator implements Iterator<T>
    {

        private HashTableElement[] table;
        private int nextIndex = -1;
        private int modCountSnapshot;


        public HashTableInterator(HashTableElement[] table , int modCountSnapshot)
        {
            this.table = table;
            this.modCountSnapshot = modCountSnapshot;
            findNextIndex();
        }

        @Override
        public boolean hasNext()
        {
            if (modCountSnapshot != HastTable.this.modCount)
            {
                throw new ConcurrentModificationException("Can not change your hashtable while using an iterator");
            }
            return nextIndex != -1;
        }

        @Override
        public T next()
        {
            if (!hasNext())
            {
                throw new NoSuchElementException("There is no element to return");
            }

            Object nextElement = table[nextIndex].element;
            findNextIndex();
            return (T)nextElement;
        }


        private void findNextIndex()
        {
            for (int i = nextIndex +1 ; i <table.length ; i++)
            {
                if (table[i] != null && !table[i].isEmpty)
                {
                    nextIndex = i;
                    return;

                }
            }
            nextIndex = -1;
    }



    }



    @Override
    public Object[] toArray()
    {
        return new Object[0];
    }

    @Override
    public <T1> T1[] toArray(T1[] a)
    {
        return null;
    }


    @Override
    public boolean containsAll(Collection<?> c)
    {
        return false;
    }

    @Override
    public boolean addAll(Collection<? extends T> c)
    {
        return false;
    }

    @Override
    public boolean retainAll(Collection<?> c)
    {
        return false;
    }

    @Override
    public boolean removeAll(Collection<?> c)
    {
        return false;
    }

    @Override
    public void clear()
    {
        size = 0;
        table = new HashTableElement[initialSize];
        modCount++;
    }

    @Override
    public String toString()
    {
        String result = "";
        for (int i = 0; i < table.length ; i++)
        {
            if (i !=0)
            {
                result +=", ";
            }

            if (table[i] != null)
            {
                result+= table[i].toString();
            }
            else
            {
                result+= "null";
            }
        }


        return  result;
    }

    private static class HashTableElement
    {
        private Object element;
        private boolean isEmpty;

        public HashTableElement(Object element, boolean isEmpty)
        {
            this.element = element;
            this.isEmpty = isEmpty;
        }

        public String toString()
        {
            if (isEmpty)
            {
                return "empty";
            }
            return element.toString();
        }
    }

}
