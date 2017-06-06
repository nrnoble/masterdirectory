package nrnoble.com;

import java.util.*;


public class Huffman
{
    private String space = "00100000";
    private String rtn   = "00001010";
    private String a = "01100001";
    private String b = "01100010";
    private String c = "01100011";
    private String d = "01100100";
    private String e = "01100101";
    private String f = "01100110";
    private String g = "01100111";
    private String h = "01101000";
    private String i = "01101001";
    private String j = "01101010";
    private String k = "01101011";
    private String l = "01101100";
    private String m = "01101101";
    private String n = "01101110";
    private String o = "01101111";
    private String p = "01110000";
    private String q = "01110001";
    private String r = "01110010";
    private String s = "01110011";
    private String t = "01110100";
    private String u = "01110101";
    private String v = "01110110";
    private String w = "01110111";
    private String x = "01111000";
    private String y = "01111001";
    private String z = "01111010";

    Map<String, Double> rawDataStats = new HashMap<String,Double>();
    Map<String, String> asciiBitMap = new HashMap<>();
    Map<String,HuffmanNode> characterNodeMap = new HashMap<String,HuffmanNode>();
    Map<String,String> huffmanValues = new HashMap<>();


    private String[] ascii ={space,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z};
    private byte[] data;
    private byte[] filteredText;
    private int rawCharacterCount;
    public MaryHeap<HuffmanNode> huffNodes= new MaryHeap<HuffmanNode>(10,3);
    private String[] keys = new String[]{" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
    private final String NULL = "\\u000";
    private int characterCount = 0;
    private int totalHuffmanBits = 0;

    // debug variables
    // list of characters that have been filtered out because they are not part A-Z + space.
       protected List<Byte> debugSkippedCharacters = new ArrayList<>();



    /**
     * Huffman constructor
     * @param rawFileData the raw rawFileData from a file'
     */
    public Huffman(byte[] rawFileData)
    {
        this.createAsciiBitMap();
        this.data = rawFileData;
        this.resetCharMap();
        this.calcProbablity();
        this.createNodes();
        this.combineNodes();
        this.getTotalHuffmanBits();
        //this.createAsciiBitMap();
    }

    /**
     * Get array of ASCII characters has
     * @return
     */
    public String[] getASCIIBitConvertionTable()
    {
        return ascii;
    }

    /**
     * Get the bits for a specififc ascii character
     * @param key ascii character
     * @return string of 8 bits
     */
    public String asciiToBit (String key)
    {
        String result = this.asciiBitMap.get(key);

        // if there is a characters out of range,
        // make it a space.
        if (result == null)
        {
            result = "00100000";
        }
        return result;
    }

    public String HuffmanToAsscii(String huffString)
    {
        //String rtnStr = "";
        for (char ch: huffString.toCharArray())
        {
            //rtnStr += this.
        }

        return "";
    }

    // Create a hashMap that maps ascii characters to 8 bits.
    private void createAsciiBitMap()
    {
        for (int i = 0; i < this.ascii.length; i++)
        {
            this.asciiBitMap.put(keys[i],ascii[i]);
        }
    }


    /**
     * Used to build the Huffman tree. Takes the the two nodes with the lowest
     * frequency percentage and combines them into one node with the combined
     * frequency of the two nodes. The new node has the data value of Null.
     * See public method HuffmanNode combineTwoNodes(HuffmanNode leftNode, HuffmanNode righNode)
     */
    private void combineNodes()
    {
        while (this.huffNodes.size() > 1)
        {
            HuffmanNode  firstNode = this.huffNodes.delMin();
            HuffmanNode  secondNode = this.huffNodes.delMin();

            HuffmanNode combinedNode = this.combineTwoNodes(secondNode,firstNode);
            this.huffNodes.insert(combinedNode);
        }
    }


    // combines two Nodes into one
    // Remove the two lowest frequency nodes from the heap
    // Create a new parent node for the two nodes removed from the heap.
    // The parent node stores no character. You can represent this by storing the null character: '\u0000'
    // The parent node's frequency is the sum of both of the child node frequencies
    public HuffmanNode combineTwoNodes(HuffmanNode leftNode, HuffmanNode righNode)
    {
        String combinedKey = leftNode.getKey() + "." + righNode.getKey();
        double combinedFreq = leftNode.getProbability() + righNode.getProbability();
        double combinedCount = leftNode.getCharacterCount() + righNode.getCharacterCount();
        HuffmanNode combinedNode = new  HuffmanNode(NULL,combinedFreq,combinedCount,leftNode,righNode,null);
        leftNode.setParent(combinedNode);
        leftNode.setLeftRightBit("0");
        righNode.setParent(combinedNode);
        righNode.setLeftRightBit("1");
        return combinedNode;
    }

    /**
     * Returns the Map keys a-z. The keys are uses with Hashmaps to retreive
     * bit strings representing the key as either ASSCI or Huffman bits.
     * @return a string of 3-8 characters. such as 000 or101101
     */
    public String[] getKeys()
    {
        return keys;
    }

    public Map<String, Double> getRawDataStats()
    {
        return rawDataStats;
    }


    /**
     * Get all the characters
     * @return all the characters
     */
    public int[] getCharacters()
    {
        return filterCharacters;
    }


    private int[] filterCharacters =  new int[123];

    /**
     * Returns the original file bytes
     * @return an array of ASCII bytes
     */
    public byte[] getData()
    {
        return data;
    }


    private void setData(byte[] data)
    {
        this.data = data;
    }


    // Get the total number of characters
    public int getCharacterCount()
    {
        if (characterCount != 0)
            return characterCount;

        return getFilterCount();
    }


    public Map<String, HuffmanNode> getCharacterNodeMap()
    {
        return characterNodeMap;
    }

    // Calculate the probability of each character in the character rawDataStats
    // Characters no in the character rawDataStats are ingored.
    private void calcProbablity()
    {
        this.filteredText = new byte[getFilterCount()];
        characterCount = 0;
        for (int i = 0; i < this.data.length; i++)
        {
            String key = getKey(data[i]);
            Double value = rawDataStats.get(key);

//            if (data[i] == 10 || data[i] == 32 || (data[i] >= 97 && data[i] <= 122) || (data[i] >= 65 && data[i] <= 90))
            if (data[i] == 32 || (data[i] >= 97 && data[i] <= 122) || (data[i] >= 65 && data[i] <= 90))
            {
                rawDataStats.put(key, ++value);
                this.characterCount++;
              //  System.out.println("characterCount: " + characterCount);
            }
            else
            {
               // System.out.println("skipping: " +  data[i]);
                debugSkippedCharacters.add(data[i]);

            }

        }
    }


    // get the rawDataStats key for a specific characters.
    // includes spaces and return
    public String getKey(byte ch)
    {
        return  Character.toString((char)ch).toLowerCase();
    }


    // creates a single node and inserts into to the heap
    private void addNode(String key, double probablity, double characterCount, HuffmanNode leftNode, HuffmanNode rightNode)
    {
        HuffmanNode hNode = new HuffmanNode(key, probablity, characterCount, leftNode, rightNode,null);
        huffNodes.insert(hNode);
        characterNodeMap.put(key,hNode);
    }


    public int getTotalHuffmanBits()
    {
        if (totalHuffmanBits > 0)
        {
            return totalHuffmanBits;
        }

        Map charMap = this.getCharacterNodeMap();
        HuffmanNode node;
        String bits;

        for (String key: this.keys)
        {
            node = characterNodeMap.get(key);
            totalHuffmanBits += node.getHuffmanBitCount();
        }

        return this.totalHuffmanBits;
    }

    // creates all possible nodes bases on the character rawDataStats
    // A-Z is converted to lowercase so all alpha characters are lowercase
    // character rawDataStats also includes the space character and return control character.
    // All other characters are ignored, such as punctuation
    private void createNodes()
    {
        for (String key: this.keys)
        {
           // System.out.println("key: " + key);
            double value = this.rawDataStats.get(key);
            double probability = value / this.getCharacterCount();
            this.addNode(key, probability, value, null, null);
        }
    }


    // Init the character rawDataStats.
    // All values are set to zero.
    private void resetCharMap()
    {
        rawDataStats.put(Character.toString((char) 32), 0.0);
//        rawDataStats.put("rtn", 0.0);
        for (int i = 97; i <= 122; i++)
        {
            String key = Character.toString((char) i);
            this.rawDataStats.put(key, 0.0);
        }
    }


    // get the character counter of valid characters based character rawDataStats.
    // only characters in the character rawDataStats are counted, punctuation and
    // control characters are ignored, except for return
    private int getFilterCount()
    {

        // if already counted, just return the total
        if (characterCount != 0)
        {
            return characterCount;
        }

        characterCount = 0;
        for (int i = 0; i < this.data.length; i++)
        {
            if (data[i] == 32 || (data[i] >= 97 && data[i] <= 122) || (data[i] >= 65 && data[i] <= 90) )
            {
                characterCount++;
            }
        }
        return characterCount;
    }



}

