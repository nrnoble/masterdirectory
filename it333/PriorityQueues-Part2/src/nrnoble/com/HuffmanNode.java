package nrnoble.com;

public class HuffmanNode implements Comparable<HuffmanNode>
{
    private final char data;
    private final int probability;
    private final HuffmanNode left;
    private final HuffmanNode right;

    HuffmanNode(char data, int probability, HuffmanNode left, HuffmanNode right)
    {
        this.data = data;
        this.probability = probability;
        this.left = left;
        this.right = right;
    }

    @Override
    public int compareTo(HuffmanNode o)
    {
        return 0;
    }
}