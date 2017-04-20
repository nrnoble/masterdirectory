/*
 * Neal Noble
 * April 2017
 * Assignment: Linked List (Part 1)
 * Instructor: Josh Archer
 */

package part2;

import javax.rmi.CORBA.Util;
import java.util.*;

import static part2.Utils.debugPrintNodes;
import static part2.Utils.debugPrintln;

public class UniqueList <T> implements List<T>, Iterable<T>
{

	private int nodeCount = 0;
	public Node nodes = null;
	public static boolean debugging = java.lang.management.ManagementFactory.getRuntimeMXBean().
			getInputArguments().toString().indexOf("-agentlib:jdwp") > 0;

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
		Node currentNode = nodes.getFirstNode();
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
		return nodes.iterator();
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
		//IndexOutOfBoundsException (Links to an external site.) - if the index is out of range (index < 0 || index > size())
		if (index < 0 || index > nodeCount)
		{
			throw new IndexOutOfBoundsException("Index is out of bounds");
		}

		Node currentNodeTest = getNodeAtIndex(index);

		Node currentNode = nodes.getNodeByIndex(index);
		Node insertedNode = nodes.addNode(currentNode,element);
		nodeCount++;





	}


	private Node getNodeAtIndex(int index)
	{
		//return (T) nodes.getNodeByIndex(index).getNodeValue();

		if  (index < 0 || index > this.nodeCount-1)
		{
			throw new IndexOutOfBoundsException("The index value is out of bounds");
		}


		Node currentNode = nodes.getFirstNode();
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
//				System.out.println("nodeCount:" + nodeCount + " Node=" + node);
				nodes.addToLastNode(node);
				this.nodeCount++;
				result = true;
			}

		}

		return result;
	}



	private void printNodeList(Node listofNodes)
	{
		if(!debugging)
			return;

		Node currentnode = listofNodes.getFirstNode();
		System.out.print(currentnode.getNodeValue() + ", ");
		while (!currentnode.isLastNode())
		{
			currentnode = currentnode.getNextNode();
			System.out.print(currentnode.getNodeValue() + ", ");
		}
		System.out.println();

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

		debugPrintNodes(nodes,"main");
		debugPrintln();
		Node InsertNode = nodes.getNodeByIndex(index);
		debugPrintln("Value at index: " + InsertNode.getNodeValue());
		Node previousNode = InsertNode.getPreviousNode();
		Node nextNode = InsertNode.getNextNode();
		debugPrintln("Value at previousNode: " + previousNode.getNodeValue());
		debugPrintln("Value at firstNode: " + nodes.getFirstNode().getNodeValue());
		debugPrintln("Value at lastNode: " + nodes.getLastNode().getNodeValue());

		Iterator<T> addListiterator1 = (Iterator<T>) other.iterator();

		Node currentNode = nodes.getFirstNode();
		Utils.debugPrint(currentNode.getNodeValue() + ", ");
		while (!currentNode.isLastNode())
		{
			currentNode = currentNode.getNextNode();
			Utils.debugPrint(currentNode.getNodeValue() + ", ");
		}
		System.out.println();
		


		while (addListiterator1.hasNext())
		{
			Utils.debugPrint(addListiterator1.next() + ", ");
		}
		
		System.out.println();
		System.out.println();

		Iterator<T> addListiterator = (Iterator<T>) other.iterator();

		boolean result = false;
		Node newNode = null;
		while (addListiterator.hasNext())
		{
			T node  =  addListiterator.next();

			if (!nodes.isDuplicate(node))
			{
				debugPrintln("nodeCount:" + nodeCount + " Adding Node=" + node);
				newNode = nodes.addNode(InsertNode,node);
				InsertNode = newNode;
				this.nodeCount++;
				result = true;
				printNodeList(nodes);
			}
			else
			{
				if (debugging)
				{
					System.out.println("nodeCount: " + nodeCount + " Node=" + node);
					printNodeList(nodes);
				}
			}

		}
		newNode.setNextNode(InsertNode);
		InsertNode.setPreviousNode(newNode);


		currentNode = nodes.getFirstNode();
		printNodeList(nodes);



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

		Iterator<T> removIterator = (Iterator<T>) other.iterator();

		boolean result = false;
		while (removIterator.hasNext())
		{
				T node  =  removIterator.next();
				//System.out.println(node);
				nodes.remove(node);
				nodeCount--;
				result = true;
		}

		return result;
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
