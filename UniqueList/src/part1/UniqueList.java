package part1;

import java.io.IOException;
import java.security.NoSuchAlgorithmException;
import java.util.*;

public class UniqueList <T> implements List<T>
{

	private int nodeCount = 0;
	public Node nodes = null;

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
			nodes = new Node(element);
			nodeCount++;
			return true;
		}

		//Check to determine if element is already in list

		Node nodeSearchgResults = nodes.findNode(element);
		if (nodeSearchgResults!= null) {
			return false;
		}

		// If not in list, continue

		Node lastNode = nodes.getLastNode();

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
	 * @param element
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
		Node searchNode = nodes.findNode(element);

		if (searchNode == null)
		{
			return false ;
		}

		if (searchNode.isLastNode() && searchNode.isFirstNode())
		{
			this.clear();
			return true;
		}

		boolean status = nodes.remove(element);
		nodeCount--;

		return status;
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
		Node currentNode = nodes.getFirstNode();
		//System.out.println("currentNode.getNodeValue():" + currentNode.getNodeValue());
		int count = nodeCount;
		Object[] collection = new Object[count];
		for (int i = 0; i < count ; i++)
		{

			collection[i] = currentNode.getNodeValue();
			System.out.println(collection[i]);
			currentNode = currentNode.getNextNode();
		}

		// System.out.println("currentNode.getNodeValue():" + currentNode.getNodeValue());
		// collection[count] = currentNode.getNodeValue();

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
		if (index > this.nodeCount  || index < 0)
			return null;


		Node currentNode = nodes.getFirstNode();
		int count = 0;
		while (count != index)
		{
			currentNode = currentNode.getNextNode();
			count++;
		}

		return (T)currentNode.getNodeValue();

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

		Node firstNode = nodes.getFirstNode();
		if (index == 0)
		{
			nodeCount--;
			return (T) firstNode;

		}

		Node indexNode = null;
		for (int i = 1; i <=index ; i++)
		{
			indexNode = nodes.getNextNode();
		}
		nodeCount--;
		return (T) indexNode;
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
