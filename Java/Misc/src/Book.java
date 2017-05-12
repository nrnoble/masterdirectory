import a.c.T;

public class Book implements Comparable<T>
{
    private String author;
    private String title;
    private int pageCount;

    @Override
    public int compareTo(T _book)
    {
        if (this.pageCount != pageCount)
            return -1;
        return 0;
    }
}
