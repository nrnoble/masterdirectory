package nrnoble.com;

import java.text.DecimalFormat;

public class HuffmanNode implements Comparable<HuffmanNode>
{

    private final String key;
    private double characterCount;
    private final double probability;
    private String HuffmanCharacterBitString ="";
    private String leftRightBit = "";
    private double totalHuffmanBits = 0;
    private final HuffmanNode left;
    private final HuffmanNode right;
    private HuffmanNode parent;

    HuffmanNode(String key, double probability, double characterCount, HuffmanNode left, HuffmanNode right, HuffmanNode parent)
    {

        this.key = key;
        this.probability = probability;
        this.characterCount = characterCount;
        this.left = left;
        this.right = right;
        this.parent = parent;
    }

    @Override
    public int compareTo(HuffmanNode hHode)
    {
        if (this.probability == hHode.probability)
        {
            return 0;
        }

        if (this.probability < hHode.probability)
        {
            return -1;
        }

        return 1;
    }


    public HuffmanNode getParent()
    {
        return parent;
    }

    public void setParent(HuffmanNode parent)
    {
        this.parent = parent;
    }

    public String getKey()
    {
        return key;
    }

    public double getCharacterCount()
    {
        return characterCount;
    }

    public void setCharacterCount(double characterCount)
    {
        this.characterCount = characterCount;
    }

    public double getProbability()
    {
        return probability;
    }

    public HuffmanNode getLeft()
    {
        return left;
    }

    public HuffmanNode getRight()
    {
        return right;
    }

    public String getHuffmanCharacterBitString()
    {
        return HuffmanCharacterBitString;
    }

    public void setHuffmanCharacterBitString(String huffmanCharacterBitString)
    {
        this.HuffmanCharacterBitString = huffmanCharacterBitString;
    }

    public String getLeftRightBit()
    {
        return leftRightBit;
    }

    public void setLeftRightBit(String leftRightBit)
    {
        this.leftRightBit = leftRightBit;
    }

    public String getHuffmanBitString()
    {
        if (this.HuffmanCharacterBitString.length() >0)
        {
            return  this.HuffmanCharacterBitString;
        }
        if (parent !=  null)
        {
            HuffmanCharacterBitString =  parent.getHuffmanBitString();
        }
        this.HuffmanCharacterBitString = HuffmanCharacterBitString + leftRightBit;
        return this.HuffmanCharacterBitString;
    }

    public double getHuffmanBitCount()
    {
        if (this.totalHuffmanBits > 0)
        {
            return this.totalHuffmanBits;
        }
        getHuffmanBitString();
        totalHuffmanBits = this.characterCount * this.HuffmanCharacterBitString.length();
        return totalHuffmanBits;
    }

    @Override
    public String toString()
    {
        DecimalFormat intFormat = new DecimalFormat("#000,000");
        DecimalFormat percentFormat = new DecimalFormat("#00.00%");

        return this.key + ": " + percentFormat.format (this.probability);
    }
}