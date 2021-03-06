/*
 * Neal Noble
 * April 2017
 * Assignment: Linked List (Part 1)
 * Instructor: Josh Archer
 */

package part2;
import java.util.*;


public class UniqueList <T> implements List<T>, Iterable<T>
{

	private int nodeCount = 0;
	public Node<?> nodes = null;

    // returns true if debugger is active.
    // http://stackoverflow.com/questions/2755445/how-can-i-write-an-anonymous-function-in-java
    public static boolean debugging = java.lang.management.ManagementFactory.getRuntimeMXBean().
            getInputArguments().toString().indexOf("-agentlib:jdwp") > 0;

			
	/**
	 * Add element to the end of linked List
	 * @param element is any object of type T
	 * @return true if object has been added to the end of the linked list
	 */
	@Override
	public boolean add(T element)
	{
		// execute this only when the first node is added
		// to list or when the list has been cleared
		if (nodes == null)
		{
			nodes = new Node<Object>(element);
			nodeCount++;
			return true;
		}
		
		
		//Check to determine if element is already in list
		Node<?> nodeSearchgResults = nodes.findNode(element);
		if (nodeSearchgResults!= null) {
			return false;
		}

		Node<?> lastNode = nodes.getLastNode();
		lastNode.addNode(element);
		nodeCount++;
		return true;
	}



	/**
	 * Clear call data from list. Reset counter
	 */
	@Override
	public void clear()
	{
		nodes = null;
		nodeCount = 0;
	}


	
	/**
	 * Check if current element is already in list
	 * @param element value
	 * @return true if the element is already in list
	 */
	@Override
	public boolean contains(Object element)
	{
		Node currentNode = nodes.getFirstNode();

		while (!currentNode.isEqual(element))
		{
			if (!currentNode.isLastNode())
			{
				currentNode = currentNode.getNextNode();
			}
			else
			{
				return false;
			}
		}
		return true;
	}


	
	/**
	 * Check if the list has zero elements.
	 * @return true if there are no elements in list
	 */
	@Override
	public boolean isEmpty()
	{
		if (nodes == null)
			return true;

		return false;
	}

	

	/**
	 * remove and element by value from list
	 * @param element to be removed
	 * @return true if the element was removed
	 */
	@Override
	public boolean remove(Object element)
	{
		Node resultNode = nodes.findNode(element);

		if (resultNode == null)
		{
			return false ;
		}

		if (resultNode.isLastNode() && resultNode.isFirstNode())
		{
			this.clear();
			return true;
		}

		nodes.remove(element);
		nodeCount--;

		return true;
	}


	/**
	 * Get the number of elements in list
	 * @return number of elements in list
	 */
	@Override
	public int size()
	{
		return nodeCount;
	}


	/**
	 * Return the list as array of objects
	 * @return array of objects
	 */
	@Override
	public Object[] toArray()
	{
		Node<?> currentNode = nodes.getFirstNode();
		int count = nodeCount;
		Object[] collection = new Object[count];
		for (int i = 0; i < count ; i++)
		{
			collection[i] = currentNode.getNodeValue();
			currentNode = currentNode.getNextNode();
		}

		return collection;
	}


	/**
	 * Gets the Iterator of the list
	 * @return Interator
     */
	@Override
	public Iterator<T> iterator()
	{
		return (Iterator<T>) nodes.iterator();
	}


	// ****** INDEX-BASED METHODS ******


	/**
	 * Add a new elment at index location
	 * @param index where the new element is to be added
	 * @param element value
     */
	@Override
	public void add(int index, T element)
	{
		if (index < 0 || index > nodeCount)
		{
			throw new IndexOutOfBoundsException("Index is out of bounds");
		}

		Node currentNode = nodes.getNodeByIndex(index);
		Node insertedNode = nodes.addNode(currentNode,element);
		nodeCount++;

	}


	private Node<?> getNodeAtIndex(int index)
	{

		if  (index < 0 || index > this.nodeCount-1)
		{
			throw new IndexOutOfBoundsException("The index value is out of bounds");
		}


		Node<?> currentNode = nodes.getFirstNode();
		int count = 0;
		while (count != index)
		{
			currentNode = currentNode.getNextNode();
			count++;
		}

		return currentNode;
	}



	/**
	 * get element value at index
	 * @param index of value to be return
	 * @return element value located at index.
     */
	@SuppressWarnings("unchecked")
	@Override
	public T get(int index)
	{

		return (T) getNodeAtIndex(index).getNodeValue();

	}


	/**
	 * Set the value of element at index
	 * @param index value
	 * @param element value
     * @return element value
     */
	@Override
	public T set(int index, T element)
	{

		Node indexNode = getNodeAtIndex(index);
		indexNode.setNodeValue(element);
		return  element;
	}


    /**
     * Retreive the first index of the element
     * @param element
     * @return index of the element in the chain
     */
	@Override
	public int indexOf(Object element)
	{
		return nodes.getNodeIndex(element);
	}


	/**
	 * Remove element from list list at index
	 * @param index location
	 * @return value of element that that was removed.
     */
	//@Override
	public T remove(int index)
	{

		if (index < 0 || index >= size())
		{
			throw new IndexOutOfBoundsException  ("Index out of bounds");
		}

		Node firstNode = nodes.getFirstNode();
		if (index == 0)
		{
			T firstNodeValue = (T) nodes.getFirstNode();
			nodes.remove(nodes.getFirstNode());
			nodeCount--;
			return firstNodeValue;
		}

		if (index == nodeCount-1)
		{
			T lastNodeValue = (T) nodes.getLastNode();
			nodes.remove(nodes.getLastNode());
			nodeCount--;
			return lastNodeValue;
		}

		Node indexNode = null;
		indexNode = nodes.getFirstNode();
		for (int i = 0; i <=index ; i++)
		{
			if (index == i)
			{
				T value = (T) indexNode;
				nodes.remove (indexNode);
				nodeCount--;
				return value;
			}
			indexNode = indexNode.getNextNode();
		}
		return  null;
	}


	/**
	 * Get the last index of element in list
	 * @param element value
	 * @return true if element is in list.
     */
	@Override
	public int lastIndexOf(Object element)
	{
		return nodes.getNodeIndex(element);
	}






	// ****** SET METHODS ******


	/**
	 * Add all items in collection to existing list
	 * @param other elements
	 * @return
     */
	@Override
	public boolean addAll(Collection<? extends T> other)
	{
		if (nodeCount == 0 && other.size() == 0)
		{
			return false;
		}

		Iterator<T> addListiterator = (Iterator<T>) other.iterator();

		boolean result = false;
		while (addListiterator.hasNext())
		{
			T node  =  addListiterator.next();

			if (!nodes.isDuplicate(node))
			{
				nodes.addToLastNode(node);
				this.nodeCount++;
				result = true;
			}

		}
		return result;
	}



    /**
	 * Add all elements from collection to list at index
	 * @param index location
	 * @param other collection
     * @return true if list has been updated with one or more new element. No duplicates
     */
	@Override
	public boolean addAll(int index, Collection<? extends T> other)
	{

        Node InsertNode = nodes.getNodeByIndex(index);
		@SuppressWarnings("unchecked")
		Iterator<T> addListiterator = (Iterator<T>) other.iterator();
		boolean result = false;
		Node newNode = null;
		
		while (addListiterator.hasNext())
		{
			T node  =  addListiterator.next();

			if (!nodes.isDuplicate(node))
			{
				newNode = nodes.addNode(InsertNode,node);
				this.nodeCount++;
				result = true;
			}
		}

        // reconnect remaining nodes
		newNode.setNextNode(InsertNode);
		InsertNode.setPreviousNode(newNode);

		return false;
	}

    /**
     * The list verifies that it contains a collection of elements
     * @param other a collection of elements
     * @return true if list contains all elements in the collection
     */
	@Override
	public boolean containsAll(Collection<?> other)
	{

        Iterator<T> containsList = (Iterator<T>) other.iterator();

        while (containsList.hasNext())
        {
            Object element = containsList.next();
            boolean result = this.contains(element);
            if (!result)
            {
                return false;
            }
        }
            return true;
	}


    /**
     * Remove a collection of elements from list
     * @param other collection of elements
     * @return true if list has changed
     */
	@SuppressWarnings("unchecked")
	@Override
	public boolean removeAll(Collection<?> other)
	{

		Iterator<T> removIterator = (Iterator<T>) other.iterator();

		boolean result = false;
		while (removIterator.hasNext())
		{
				T node  =  removIterator.next();
				nodes.remove(node);
				nodeCount--;
				result = true;
		}

		return result;
	}


    /**
     * Keep only the elements in the collection parameter
     * @param other the elements collect that will remain in list
     * @return true if list has changed
     */
	@SuppressWarnings({ "unchecked", "rawtypes" })
	@Override
	public boolean retainAll(Collection<?> other)
	{
        Iterator<T> mainListIterator = (Iterator<T>) nodes.iterator();
        Iterator<T> otherIterator = (Iterator<T>) other.iterator();
        boolean listHasChanged = false;

        while (mainListIterator.hasNext())
        {
            boolean removeElement = true;
            Object element = mainListIterator.next();
            otherIterator = (Iterator<T>) other.iterator();
            while (otherIterator.hasNext())
            {
                T nextElement = otherIterator.next();
                if (nextElement == element)
                {
                    removeElement = false;
                    break;
                }
            }

            if (removeElement)
            {
                this.remove(element);
                removeElement = true;
                listHasChanged = true;
            }

        }

		return listHasChanged;
	}











	// ****** DO NOT IMPLEMENT ******

	@Override
	public List<T> subList(int start, int end)
	{
		throw new UnsupportedOperationException("subList() is not supported");
	}

	@SuppressWarnings("hiding")
	@Override
	public <T> T[] toArray(T[] arrayToFill)
	{
		throw new UnsupportedOperationException("toArray() is not supported");
	}

	@Override
	public ListIterator<T> listIterator()
	{
		throw new UnsupportedOperationException("listIterator() is not supported");
	}

	@Override
	public ListIterator<T> listIterator(int index)
	{
		throw new UnsupportedOperationException("listIterator() is not supported");
	}
}
