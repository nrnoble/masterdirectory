package nrnoble.com;

public class BinaryHeap<T extends Comparable<T>>
{
	private static final int RESIZE_FACTOR = 2;

	private static final int INITIAL_SIZE = 10;
	private static final int NUM_OF_CHILDREN = 2;

	private T[] data;
	private int size;
	
	@SuppressWarnings("unchecked")
	public BinaryHeap()
	{
		data = (T[])new Comparable[INITIAL_SIZE + 1];
	}
	
	@SuppressWarnings("unchecked")
	public BinaryHeap(T[] inputs)
	{
		//create an array of a similar size
		data = (T[])new Comparable[inputs.length + 1];
		
		//copy across my elements from the input to the array
		for (int i = 0; i < inputs.length; i++)
		{
			data[i + 1] = inputs[i];
		}
		size = inputs.length;
		
		//then build the heap
		buildHeap();
	}
	
	private void buildHeap()
	{
		for (int i = size / 2; i >= 1; i--)
		{
			sink(i);
		}
	}
	
	public void insert(T element)
	{
		//check if we need to resize
		if (size >= data.length - 1)
		{
			resize();
		}
		
		//add the new element
		size++;
		data[size] = element;
		swim(size);
	}
	
	public T delMin()
	{
		if (isEmpty())
		{
			return null;
		}
		
		//save our result
		T result = data[1];
		data[1] = null;
		
		//move the top index to the root of the tree
		swap(1, size);
		size--;
		sink(1);
		
		return result;
	}
	
	public int size()
	{
		return size;
	}
	
	public boolean isEmpty()
	{
		return size == 0;
	}
	
	public T peekMin()
	{
		return null;
	}
	
	@SuppressWarnings("unchecked")
	private void resize()
	{
		T[] newData = (T[])new Comparable[data.length * RESIZE_FACTOR];
		
		//copy across all elements
		for (int i = 0; i < data.length; i++)
		{
			newData[i] = data[i];
		}
		
		data = newData;
	}

//
//	private void swim1(int childInd)
//	{
//		T tmp = data[childInd];
//		while (childInd > 0 && tmp < data[parent(childInd)])
//		{
//			data[childInd] = data[ parent(childInd) ];
//			childInd = parent(childInd);
//		}
//		data[childInd] = tmp;
//	}




	private void swim(int index)
	{
		//stop when we reach the root (index 1)
		while (index > 1)
		{

			// D-ary calculate the number of children
			int parentIndex = (index)/NUM_OF_CHILDREN;

			if (data[index].compareTo(data[parentIndex]) < 0)
			{
				swap(index, parentIndex);
			}
			
			index = parentIndex;
		}
	}


	public void sink2(int index)
	{
		int numWays = 3;
		T lastElement = data [index];
		int parentIndex = (index-1)/2;
		while ((index > 0) && (parentIndex>0))
		//while ((index > 0))
		//while (index <= size / numWays)
		{
			data[index] = data[parentIndex];
			index = parentIndex;
			parentIndex = (parentIndex-1)/numWays;
		}
		data[index] = lastElement;
	}


	/** Function to get index of k th child of i **/
	private int childIndex(int i, int k)
	{
		return NUM_OF_CHILDREN * i + k;
	}



	private void sink(int index)
	{
		int child;
		T tmp = data[ index ];
		//while (getChildIndex(index, 1) < data.length)
		while (getChildIndex(index, 1) < this.size())
		{
			child = minChild(index);
			if (data[child].compareTo(tmp) < 0)
				data[index] = data[child];
			else
				break;
			index = child;
		}
		data[index] = tmp;
	}



	/** Function to get smallest child **/
	private int minChild(int index)
	{
		int bestChild = getChildIndex(index, 1);
		int k = 1;
		int pos = getChildIndex(index, k);
		while ((k <= NUM_OF_CHILDREN) && (pos < data.length))
		{
			if (data[pos].compareTo(data[bestChild]) < 0)
			{
				bestChild = pos;
			}

			pos = getChildIndex(index, k++);
		}
	//	System.out.println("MinChild returning: " + bestChild);
		return bestChild;
	}


	/** Function to get index of k th child of i **/
	private int getChildIndex(int heapIndex, int childIndexOfParent)
	{
		return NUM_OF_CHILDREN * heapIndex + childIndexOfParent;
	}



	private void sink3(int index)
	{
		while (index <= size / 3)
		{
			int left = 3 * index -1;
			int mid = 3 * index;
			int right = 3 * index + 1;

			int indexToCheck = left;

			//if there is a right child and it is the smaller child
			if (right < data.length && data[right] != null &&
					data[right].compareTo(data[mid]) < 0)
			{
				// indexToCheck = mid;
				swap(mid, right);
				break;
			}


			//if there is a middle child and it is the smaller child
			if (mid < data.length && data[mid] != null &&
					data[mid].compareTo(data[left]) > 0)

			{
				swap(mid, left);
				indexToCheck = mid;
				break;
			}


			//compare the parent with the smallest child
			if (data[indexToCheck].compareTo(data[index]) < 0)
			{
				swap(indexToCheck, index);
				index = indexToCheck;
			}



			else
			{
				break;
			}
		}
	}



	private void sinkgood(int index)
	{
		while (index <= size / NUM_OF_CHILDREN)
		{
			int left = NUM_OF_CHILDREN * index;
			int right = NUM_OF_CHILDREN * index + 1;

			int indexToCheck = left;

			//if there is a right child and it is the smaller child
			if (right < data.length && data[right] != null &&
					data[right].compareTo(data[left]) < 0)
			{
				indexToCheck = right;
			}

			//compare the parent with the smallest child
			if (data[indexToCheck].compareTo(data[index]) < 0)
			{
				swap(indexToCheck, index);
				index = indexToCheck;
			}
			else
			{
				break;
			}
		}
	}


	private void sink4(int index)
	{
		while (index <= size / 2)
		{
			int left = 2 * index;
			int right = 2 * index + 1;
			
			int indexToCheck = left;
			
			//if there is a right child and it is the smaller child
			if (right < data.length && data[right] != null && 
					data[right].compareTo(data[left]) < 0)
			{
				indexToCheck = right;
			}
			
			//compare the parent with the smallest child
			if (data[indexToCheck].compareTo(data[index]) < 0)
			{
				swap(indexToCheck, index);
				index = indexToCheck;
			}
			else
			{
				break;
			}
		}
	}
	
	private void swap(int first, int second)
	{
		System.out.println("Swapping data[" + first + "] " + data[first] + " <--> " + data[second] + " data[" + second + "]");
		T temp = data[first];
		data[first] = data[second];
		data[second] = temp;
	}
}









