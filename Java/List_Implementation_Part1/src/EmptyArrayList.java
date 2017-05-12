// Neal R Noble
// IT333
// April 2016
// Assignment - Assignment - List Implementation (Part one)

import java.util.*;
import java.util.function.Consumer;
;

public class EmptyArrayList<T> implements List<T>
{
    // part #1 methods below...
    private static final int MAX_ARRAY_SIZE = Integer.MAX_VALUE - 1;
    private Object[] listOfElements;
    private static final int DEFAULT_ARRAY_SIZE = 50;
    private int elementCount;
    public transient int modCount = 0;


    public EmptyArrayList()
    {
        this.listOfElements = new Object[DEFAULT_ARRAY_SIZE];
    }

    /**
     * adds newElement to the uppermost index in the list. You should be able to repeatedly
     * add listOfElements to the list (it should always resize itself to make room for new listOfElements).
     *
     * @param newElement is the new object to be added
     * @return true if element has been added.
     */
    @Override
    public boolean add(T newElement)
    {
        //arraySizeHandler(DEFAULT_ARRAY_SIZE);

        // TODO: this solutions is very inefficient. Need to rework it so
        // that is does not call add(index,element)
        add(this.elementCount, newElement);
        //this.listOfElements[this.elementCount++] = newElement;
        return true;
    }


    /**
     * inserts newElement at the given index. All existing listOfElements should still be present
     * in the list after your insert newElement. Similar to add(), you should be able to
     * repeatedly add listOfElements to the list (it should always resize itself to make room for new listOfElements).
     *
     * @param index      of where to insert element
     * @param newElement is the new object to be inserted into array
     */
    @Override
    public void add(int index, T newElement)
    {

        if (index > this.elementCount || index < 0)
            throw new IndexOutOfBoundsException("Array elementCount: " +
                    this.elementCount + " Current index: " + index);

        arraySizeHandler(this.elementCount + 1);
        System.arraycopy(listOfElements, index, this.listOfElements, index + 1, this.elementCount - index);
        this.listOfElements[index] = newElement;
        elementCount++;
    }


    /**
     * Check of List is empty
     *
     * @return true if your list is empty, otherwise false.
     */
    @Override
    public boolean isEmpty()
    {
        if (this.elementCount == 0)
            return true;

        return false;
    }


    /**
     * Size of List
     *
     * @return the number of listOfElements in the list.
     */
    @Override
    public int size()
    {
        return this.elementCount;
    }


    /**
     * removes all listOfElements in the list.
     */
    @Override
    public void clear()
    {
        elementCount = 0;
        this.listOfElements = new Object[DEFAULT_ARRAY_SIZE];
    }


    /**
     * returns the index of the first occurrence of search in the list.
     * If search is not found, then indexOf() should return -1.
     *
     * @param search element
     * @return index of element. -1 if element is not found
     */
    @Override
    public int indexOf(Object search)
    {
        // do a check of null to avoid throwing an exception
        if (search == null) {
            for (int index = 0; index < elementCount; index++)
                if (this.listOfElements[index] == null) {
                    return index;
                }
        } else {
            for (int index = 0; index < elementCount; index++)
                if (search.equals(this.listOfElements[index])) {
                    return index;
                }
        }
        return -1;
    }


    /**
     * Check if element is in list
     *
     * @param search element
     * @return true if element exists
     */
    @Override
    public boolean contains(Object search)
    {
        if (indexOf(search) >= 0)
            return true;

        return false;
    }


    /**
     * Get element from list
     *
     * @param index add element at index
     * @return element that has been added
     */
    @Override
    public T get(int index)
    {
        if (boundaryCheck(index))
            return (T) this.listOfElements[index];

        return null;
    }


    /**
     * @param index add element at index
     * @param value element to be added
     * @return element that has been added
     */
    @Override
    public T set(int index, T value)
    {
        if (this.boundaryCheck(index)) {
            this.listOfElements[index] = value;
            return value;
        }
        return value;
    }


    /**
     * removes the first occurrence of search in the list. Returns true if the listOfElements
     * was found, otherwise false.
     *
     * @param search is the element to be removed
     * @return true if element has been removed
     */
    @Override
    public boolean remove(Object search)
    {
        this.removeElement(indexOf(search));
        return true;
    }

    /**
     * remove element by index
     *
     * @param index of element to be removed from list
     * @return null
     */
    @Override
    public T remove(int index)
    {
        this.removeElement(index);
        return null;
    }


    private void increaseArray_size(int minArraySize)
    {

        int currentArrayLength = this.listOfElements.length;
        int increaseArraySize = currentArrayLength + (currentArrayLength >> 1);
        if (increaseArraySize - minArraySize < 0) {
            increaseArraySize = minArraySize;
        }

        if (increaseArraySize - this.MAX_ARRAY_SIZE > 0) {
            increaseArraySize = this.MAX_ARRAY_SIZE;
        }

        listOfElements = Arrays.copyOf(this.listOfElements, increaseArraySize);
    }


    private boolean boundaryCheck(int _index)
    {
        if (_index > this.elementCount || _index < 0)
            throw new IndexOutOfBoundsException("Array elementCount: " + elementCount + " Current index: " + _index);

        return true;
    }


    private void arraySizeHandler(int _min)
    {
        Object[] defaultSize = {};
        if (listOfElements == defaultSize) {
            _min = Math.max(this.DEFAULT_ARRAY_SIZE, _min);
        }

        listrSizeHandler(_min);
    }

    private void listrSizeHandler(int _min)
    {
        this.modCount++;

        if (_min - this.listOfElements.length > 0)
            this.increaseArray_size(_min);
    }

    private void removeElement(int index)
    {
        this.modCount++;
        int num = this.elementCount - index - 1;
        if (num > 0) {
            System.arraycopy(this.listOfElements,
                    index + 1,
                    this.listOfElements, index,
                    num);
        }

        this.listOfElements[--elementCount] = null;

    }


    // part #2 methods below...

    @Override
    public boolean addAll(Collection<? extends T> other)
        {

        return addAll(this.size(), other);
    }

    @Override
    public boolean addAll(int index, Collection<? extends T> other)
    {

        boundaryCheck(index);
        boolean modified = false;
        for (T element : other) {
            add(index++, element);
            modified = true;
        }
        return modified;
    }

    @Override
    public boolean containsAll(Collection<?> other)
    {

//        Iterator<?> elements = other.iterator();
//
//        while (elements.hasNext())
//
//            if(!contains(elements.next()))
//                return false;
//        return true;

        for (Object element: other)
        {
            if (this.contains(element))
            {
                continue;
            }
            else
            {
                return false;
            }
        }

       return true;
    }

    @Override
    public boolean removeAll(Collection<?> other)
    {
        return removeHelper(other, false);
    }


    @Override
    public boolean retainAll(Collection<?> other)
    {
        Objects.requireNonNull(other);
        return removeHelper(other, true);
    }

    @Override
    public EmptyArrayList<T> subList(int _start, int _end)
    {
        if (_start < 0)
            throw new IndexOutOfBoundsException("fromIndex = " + _start);
        if (_end > this.elementCount)
            throw new IndexOutOfBoundsException("toIndex = " + _end);
        if (_start > _end)
            throw new IllegalArgumentException("fromIndex(" + _start +
                    ") > toIndex(" + _end + ")");

        return new SubList(this, _start, _end);
    }

    @Override
    public Object[] toArray()
    {

//            Object[] r = new Object[internalSubList_size()];
//            Iterator<T> it = iterator();
//            for (int i = 0; i < r.length; i++)
//            {
//                if (! it.hasNext())
//                    return Arrays.copyOf(r, i);
//                      r[i] = it.next();
//            }
//             return it.hasNext() ? finishToArray(r, it) : r;

        return Arrays.copyOf(this.listOfElements, this.elementCount);
    }

    @Override
    public <T> T[] toArray(T[] toFill)
    {
        if (toFill.length < this.elementCount)
            return (T[]) Arrays.copyOf(this.listOfElements,this.elementCount, toFill.getClass());
        System.arraycopy(this.listOfElements, 0, toFill, 0, this.elementCount);
        if (toFill.length > elementCount)
            toFill[elementCount] = null;
        return toFill;
    }

    @Override
    public Iterator<T> iterator()
    {
        return new myIterator();
    }

    // extra credit below...

    @Override
    public ListIterator<T> listIterator(int index)
    {
        throw new UnsupportedOperationException("This method is not supported.");
    }


    @Override
    public int lastIndexOf(Object search)
    {
        throw new UnsupportedOperationException("This method is not supported.");
    }



    @Override
    public ListIterator<T> listIterator()
    {
        throw new UnsupportedOperationException("This method is not supported.");
    }

    private boolean removeHelper(Collection<?> c, boolean _comp)
    {
        final Object[] localListOfElements = this.listOfElements;
        int r = 0, w = 0;
        boolean modified = false;
        try {
            for (; r < this.elementCount; r++)
                if (c.contains(localListOfElements[r]) == _comp)
                    localListOfElements[w++] = localListOfElements[r];
        } finally {

            if (r != this.elementCount) {
                System.arraycopy(localListOfElements, r,
                        localListOfElements, w,
                        this.elementCount - r);
                w += this.elementCount - r;
            }
            if (w != this.elementCount) {

                for (int i = w; i < this.elementCount; i++)
                    localListOfElements[i] = null;
                modCount += this.elementCount - w;
                this.elementCount = w;
                modified = true;
            }
        }
        return modified;
    }


    private static <T> T[] finishToArray(T[] r, Iterator<?> it) {
        int i = r.length;
        while (it.hasNext()) {
            int cap = r.length;
            if (i == cap) {
                int newCap = ((cap / 2) + 1) * 3;
                if (newCap <= cap) { // integer overflow
                    if (cap == Integer.MAX_VALUE)
                        throw new OutOfMemoryError
                                ("Required array internalSubList_size too large");
                    newCap = Integer.MAX_VALUE;
                }
                r = Arrays.copyOf(r, newCap);
            }
            r[i++] = (T)it.next();
        }
        // trim if overallocated
        return (i == r.length) ? r : Arrays.copyOf(r, i);
    }




    private class myIterator implements Iterator<T>
    {
        int expectedCount = modCount;
        int csr; //cursor
        int lastRet = -1;


        public boolean hasNext()
        {
            return csr != EmptyArrayList.this.elementCount;
        }

        @SuppressWarnings("unchecked")
        public T next()
        {
            checkComodification(); //checkComodification
            int i = csr;
            if (i >= EmptyArrayList.this.elementCount)
                throw new NoSuchElementException();
            Object[] elements = EmptyArrayList.this.listOfElements;
            if (i >= elements.length)
                throw new ConcurrentModificationException();
            csr = i + 1;
            return (T) elements[lastRet = i];
        }

        public void remove()
        {
            if (lastRet < 0)
                throw new IllegalStateException();
            checkComodification();

            try {
                EmptyArrayList.this.remove(lastRet);
                csr = lastRet;
                lastRet = -1;
                expectedCount = modCount;
            } catch (IndexOutOfBoundsException ex) {
                throw new ConcurrentModificationException();
            }
        }

        @Override
        @SuppressWarnings("unchecked")
        public void forEachRemaining(Consumer<? super T> _consumer)
        {
            Objects.requireNonNull(_consumer);
            final int size = EmptyArrayList.this.size();
            int i = csr;
            if (i >= size)
            {
                return;
            }

            final Object[] elementData = EmptyArrayList.this.listOfElements;
            if (i >= elementData.length)
            {
                throw new ConcurrentModificationException();
            }
            while (i != size && modCount == expectedCount)
            {
                _consumer.accept((T) elementData[i++]);
            }

            csr = i;
            lastRet = i - 1;
            checkComodification();
        }

        final void checkComodification()
        {
            if (modCount != expectedCount)
                throw new ConcurrentModificationException();
        }
    }

}


class SubList<T> extends EmptyArrayList<T>
{
    private final EmptyArrayList<T> internalSubList;
    private final int offset;
    private int internalSubList_size;

    SubList(EmptyArrayList<T> _list, int _fromIndex, int _toIndex)
    {
        if (_fromIndex < 0)
            throw new IndexOutOfBoundsException("fromIndex = " + _fromIndex);
        if (_toIndex > _list.size())
            throw new IndexOutOfBoundsException("toIndex = " + _toIndex);
        if (_fromIndex > _toIndex)
            throw new IllegalArgumentException("fromIndex(" + _fromIndex +
                    ") > toIndex(" + _toIndex + ")");
        internalSubList = _list;
        offset = _fromIndex;
        internalSubList_size = _toIndex - _fromIndex;
        this.modCount = internalSubList.modCount;

        for (int i = _fromIndex; i <= _fromIndex ; i++)
        {
                this.add(_list.get(i));
        }

    }

    public T set(int _index, T _element)
    {
        rangeCheck(_index);
        checkForComodification();
        return internalSubList.set(_index+offset, _element);
    }

    public T get(int _index)
    {
        rangeCheck(_index);
        checkForComodification();
        return internalSubList.get(_index+offset);
    }

    public int size()
    {
        checkForComodification();
        return internalSubList_size;
    }

    public void add(int _index, T _element) {
        rangeCheckForAdd(_index);
        checkForComodification();
        internalSubList.add(_index+offset, _element);
        this.modCount = internalSubList.modCount;
        internalSubList_size++;
    }

    public T remove(int _index)
    {
        rangeCheck(_index);
        checkForComodification();
        T result = internalSubList.remove(_index+offset);
        this.modCount = internalSubList.modCount;
        internalSubList_size--;
        return result;
    }


    public boolean addAll(Collection<? extends T> _addCollection)
    {
        return addAll(internalSubList_size, _addCollection);
    }

    public boolean addAll(int _index, Collection<? extends T> _collection)
    {
        rangeCheckForAdd(_index);
        int collectionSize = _collection.size();
        if (collectionSize==0)
            return false;

        checkForComodification();
        internalSubList.addAll(offset+_index, _collection);
        this.modCount = internalSubList.modCount;
        internalSubList_size += collectionSize;
        return true;
    }

    public Iterator<T> iterator()
    {
        return listIterator();
    }

    public ListIterator<T> listIterator(final int _index)
    {
        checkForComodification();
        rangeCheckForAdd(_index);

        return new ListIterator<T>() {
            private final ListIterator<T> i = internalSubList.listIterator(_index+offset);

            public boolean hasNext() {
                return nextIndex() < internalSubList_size;
            }

            public T next() {
                if (hasNext())
                    return i.next();
                else
                    throw new NoSuchElementException();
            }

            public boolean hasPrevious() {
                return previousIndex() >= 0;
            }

            public T previous() {
                if (hasPrevious())
                    return i.previous();
                else
                    throw new NoSuchElementException();
            }

            public int nextIndex() {
                return i.nextIndex() - offset;
            }

            public int previousIndex() {
                return i.previousIndex() - offset;
            }

            public void remove() {
                i.remove();
                SubList.this.modCount = internalSubList.modCount;
                internalSubList_size--;
            }

            public void set(T e) {
                i.set(e);
            }

            public void add(T e) {
                i.add(e);
                SubList.this.modCount = internalSubList.modCount;
                internalSubList_size++;
            }
        };
    }

    public EmptyArrayList<T> subList(int _start, int _end) {
        return new SubList<>(this, _start, _end);
    }

    private void rangeCheck(int index)
    {
        if (index < 0 || index >= internalSubList_size)
            throw new IndexOutOfBoundsException(outOfBoundsMsg(index));
    }

    private void rangeCheckForAdd(int _index)
    {
        if (_index < 0 || _index > internalSubList_size)
            throw new IndexOutOfBoundsException(outOfBoundsMsg(_index));
    }

    private String outOfBoundsMsg(int _index)
    {
        return "Index: "+_index+", Size: "+ internalSubList_size;
    }

    private void checkForComodification()
    {
        if (this.modCount != internalSubList.modCount)
            throw new ConcurrentModificationException();
    }
}

class RandomAccessSubList<T> extends SubList<T> implements RandomAccess
{
    RandomAccessSubList(EmptyArrayList<T> list, int _start, int _end)
    {
        super(list, _start, _end);
    }


    public EmptyArrayList<T> subList(int _start, int _end)
    {
        return new RandomAccessSubList<>(this, _start, _end);
    }
}
