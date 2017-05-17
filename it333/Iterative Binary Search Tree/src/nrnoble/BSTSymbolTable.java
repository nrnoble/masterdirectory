package nrnoble;
import java.util.ArrayList;
import java.util.List;


/*
* Neal Noble
* May 2017
* Assignment: Trees Part1
* Instructor: Josh Archer
*/



    /*
         Completed - Your symbol table correctly stores Entry objects.
         Completed - The put() and get() methods of your symbol table allow you to store and retrieve key/value pairs.
         Completed - The containsKey() and containsValue() methods allow you to query for keys or values in the symbol table.
         Completed - The keys() and values() methods correctly return lists of keys or values.
         Completed - The size(), isEmpty() and clear() methods allow you to track or remove elements in the symbol table.
         Completed - Your informal tests on the symbol table test each of the listed scenarios.
         Completed - Styles: naming conventions, brace placement, spacing, commented code, redundancy, packages and magic numbers.
         Completed - Formal documentation: full Javadocs & comment block header.
    */

/**
 * Binary Search Tree SymbolTable
 * @author Neal Noble
 * @param <K> Key identifier for key pair
 * @param <V> Value element for key pair
 */
public class BSTSymbolTable<K extends Comparable<K>, V>
{
    private BinarySearchTree<Entry> bst;

    public BSTSymbolTable()
    {
        this.bst = new BinarySearchTree<Entry>();
    }


    /**
     * Adds a key/value pair to the map if none is present, otherwise this replaces any existing entry in the map with the same key.
     * @param key identifier
     * @param value of key pair
     * @return  true if a new key/value pair was added to the map, otherwise false.
     */
    public boolean put(K key, V value)
    {
        Entry entry = new Entry(key, value);
        bst.addUpdate(entry);
        return true;
    }


    /**
     * Returns the value associated with the input key. If no key is found this method will return null.
     * @param key identifier
     * @return the value associated with the input key. If no key is found this method will return null.
     */
    public V get(K key)
    {
        if (this.containsKey(key))
        {
            Entry keyEntry = new Entry(key, null);
            Entry result = this.bst.get(keyEntry);
            return result.value;
        }
        return null;
    }


    /**
     * Returns true if the input key is located in the map, otherwise false.
     * @param key identifier
     * @return 	 true if the input key is located in the map, otherwise false.
     */
    public boolean containsKey(K key)
    {
        return this.bst.contains(new Entry(key,null));
    }


    /**
     * 	Returns true if the input value is located in the map, otherwise false.
     * @param value of key pair
     * @return  true if the input value is located in the map, otherwise false.
     */
    public boolean containsValue(V value)
    {
        return true;
    }


    /**
     * 	Returns an ordered list of keys contained in the map.
     *  @return an ordered list of keys contained in the map.
     */
    public List<K> keys()
    {
        List<K> list = new ArrayList<>();

        List<Entry> entries = bst.inOrder();
        for (Entry entry: entries)
        {
            list.add(entry.key);
        }
        return list;
    }


    /**
     * 	Returns an unordered list of values contained in the map.
     * @return an unordered list of values contained in the map.
     */
    public List<V> values()
    {
        List<V> list = new ArrayList<>();

        List<Entry> preOrderList = bst.preOrder();
        for (Entry entry: preOrderList)
        {
            list.add(entry.value);
        }
        return list;
    }


    /**
     * This returns the number of key/value pairs in the table.
     * @return the number of key/value pairs in the table.
     */
    public int size()
    {
       return bst.size();
    }


    /**
     * This returns true if there are no key/value pairs in the table, but otherwise returns false.
     * @return true if there are no key/value pairs in the table, but otherwise returns false.
     */
    public boolean isEmpty()
    {
        return bst.isEmpty();
    }


    /**
     * 	This removes all key/value pairs in the table.
     */
    public void clear()
    {
        bst.clear();
    }


    private class Entry implements Comparable<Entry>
    {
        private K key;
        private V value;

        public Entry(K key, V value)
        {
            this.key = key;
            this.value = value;
        }


        @Override
        public int compareTo(Entry entry)
        {
            return this.key.compareTo(entry.key);
        }
    }
}