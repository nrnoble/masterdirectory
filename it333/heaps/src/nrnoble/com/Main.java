package nrnoble.com;

public class Main {

    public static void main(String[] args) {
	// write your code here
    }


    private static void swim(int k)
    {   while (k > 1 && less(k/2, k))
        {      exch(k/2, k);
            k = k/2;
        }
    }


    private void sink(int k)
    {
        while (2*k <= N)
        {      int j = 2*k;
            if (j < N && less(j, j+1)) j++;
            if (!less(k, j))
                break;
            exch(k, j);
            k = j;
        }
    }

    private boolean  less(int i, int j)
    {
        return pq[i].compareTo(pq[j]) < 0;
    }

    private void  exch(int i, int j)
    {
        Key t = pq[i];
        pq[i] = pq[j]; pq[j] = t;
    }




}
