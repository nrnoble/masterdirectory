package com.nrnoble;

//BinarySearchTree<T extends Comparable<T>>
public class Entry<T extends Comparable<T>>
{
    private String key;
    private String value;

    public Entry(String key, String value)
    {
        this.key = key;
        this.value = value;
    }


    public int compareTo(Entry entry)
    {
        return this.key.compareTo(entry.key);
    }
}