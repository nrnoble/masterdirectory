package part2;

import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

public class UniqueList <T> implements List<T>
{

	@Override
	public boolean add(T element)
	{
		return false;
	}

	@Override
	public void clear()
	{
		
	}

	@Override
	public boolean contains(Object element)
	{
		return false;
	}

	@Override
	public boolean isEmpty()
	{
		return false;
	}

	@Override
	public boolean remove(Object element)
	{
		return false;
	}

	@Override
	public int size()
	{
		return 0;
	}

	@Override
	public Object[] toArray()
	{
		return null;
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
		return null;
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

	@Override
	public T remove(int index)
	{
		return null;
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
