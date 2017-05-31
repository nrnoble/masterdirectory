package nrnoble.com;

import java.util.Random;

public class TestQueues 
{
	public static void main(String[] args) 
	{
		//create our queue
		BinaryHeap<Integer> queue = new BinaryHeap<>();
		
		//add a few items
		int[] input = {6, 22, 5, 77, 12, 11, 42, 150, 11, 11, 11};
		//int[] input = {11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
		for (int i = 0; i < input.length; i++)
		{
			System.out.println("inserting input[" + i + "]: " + input[i]);
			queue.insert(input[i]);
		}
		System.out.println();
		System.out.println();
		System.out.println("delMin");
		//remove all elements and print them in order
		while (!queue.isEmpty())
		{
			System.out.println(queue.delMin());
		}
//
//		//generate a large random input array
//		Random random = new Random();
//		Integer[] largeInput = new Integer[1000];
//		for (int i = 0; i < largeInput.length; i++)
//		{
//			largeInput[i] = random.nextInt(1000);
//		}
//
//		queue = new BinaryHeap<>(largeInput);
//		while (!queue.isEmpty())
//		{
//			System.out.println(queue.delMin());
//		}
	}
}







