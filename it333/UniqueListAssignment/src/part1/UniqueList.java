/*
 * Neal Noble
 * April 2017
 * Assignment: Linked List (Part 1)
 * Instructor: Josh Archer
 */

package part1;

import java.util.*;

public class UniqueList <T> implements List<T>
{

	private int nodeCount = 0;
	public Node1 nodes = null;


	/**
	 * Add element to the end of linked List
	 * @param element is any object
	 * @return true if object has been added to the end of the linked list
     */
	@Override
	public boolean add(T element)
	{
		// execute this only when the first node is added
		// to list or when the list has been cleared
		if (nodes == null)
		{
			nodes = new Node1(element);
			nodeCount++;
			return true;
		}


		//Check to determine if element is already in list
		Node1 node1SearchgResults = nodes.findNode(element);
		if (node1SearchgResults != null) {
			return false;
		}

		Node1 lastNode1 = nodes.getLastNode();
		lastNode1.addNode(element);
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
		Node1 currentNode1 = nodes.getFirstNode();

			while (!currentNode1.isEqual(element))
            {
                if (!currentNode1.isLastNode())
                {
                    currentNode1 = currentNode1.getNextNode1();
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
		Node1 resultNode1 = nodes.findNode(element);

		if (resultNode1 == null)
		{
			return false ;
		}

		if (resultNode1.isLastNode() && resultNode1.isFirstNode())
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
		Node1 currentNode1 = nodes.getFirstNode();
		int count = nodeCount;
		Object[] collection = new Object[count];
		for (int i = 0; i < count ; i++)
		{
			collection[i] = currentNode1.getNodeValue();
			currentNode1 = currentNode1.getNextNode1();
		}

		return collection;
	}


	@Override
	public Iterator<T> iterator()
	{
		return null;
	}
	
	// ****** INDEX-BASED METHODS ******

	@Override
	public void add(int index, T element)
	{
		
	}

	@Override
	public T get(int index)
	{

		if  (index < 0 || index > this.nodeCount-1)
		{
			throw new IndexOutOfBoundsException("The index value is out of bounds");
		}


		Node1 currentNode1 = nodes.getFirstNode();
		int count = 0;
		while (count != index)
		{
			currentNode1 = currentNode1.getNextNode1();
			count++;
		}

		return (T) currentNode1.getNodeValue();

	}

	@Override
	public T set(int index, T element)
	{
		return null;
	}

	@Override
	public int indexOf(Object element)
	{
		return 0;
	}

	//@Override
	public T remove(int index)
	{

		if (index > nodeCount)
			return null;

		Node1 firstNode1 = nodes.getFirstNode();
		if (index == 0)
		{
			nodeCount--;
			return (T) firstNode1;

		}

		Node1 indexNode1 = null;
		for (int i = 1; i <=index ; i++)
		{
			indexNode1 = nodes.getNextNode1();
		}
		nodeCount--;
		return (T) indexNode1;
	}

	@Override
	public int lastIndexOf(Object element)
	{
		return 0;
	}
	
	// ****** SET METHODS ******

	@Override
	public boolean addAll(Collection<? extends T> other)
	{
		return false;
	}

	@Override
	public boolean addAll(int index, Collection<? extends T> other)
	{
		return false;
	}

	@Override
	public boolean containsAll(Collection<?> other)
	{
		return false;
	}

	@Override
	public boolean removeAll(Collection<?> other)
	{
		return false;
	}

	@Override
	public boolean retainAll(Collection<?> other)
	{
		return false;
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
