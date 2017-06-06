package nrnoble.com;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


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

    Map<String, Double> map = new HashMap<String,Double>();
    Map<String, String> asciiBitMap = new HashMap<>();
    Map<String,HuffmanNode> characterNodeMap = new HashMap<String,HuffmanNode>();
//    private byte[] ascii ={space,rtn,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z};
    private String[] ascii ={space,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z};
    private byte[] data;
    private byte[] filteredText;
    private int rawCharacterCount;
    public MaryHeap<HuffmanNode> huffNodes= new MaryHeap<HuffmanNode>(10,3);
    //private String[] keys = new String[]{" ","rtn","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
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

    // Create a hashMap that maps ascii characters to 8 bits.
    private void createAsciiBitMap()
    {
        for (int i = 0; i < this.ascii.length; i++)
        {
            this.asciiBitMap.put(keys[i],ascii[i]);
        }
    }


    public void combineNodes()
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


    public String[] getKeys()
    {
        return keys;
    }

    public Map<String, Double> getMap()
    {
        return map;
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


    public byte[] getData()
    {
        return data;
    }


    public void setData(byte[] data)
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

    // Calculate the probability of each character in the character map
    // Characters no in the character map are ingored.
    private void calcProbablity()
    {
        this.filteredText = new byte[getFilterCount()];
        characterCount = 0;
        for (int i = 0; i < this.data.length; i++)
        {
            String key = getKey(data[i]);
            Double value = map.get(key);

//            if (data[i] == 10 || data[i] == 32 || (data[i] >= 97 && data[i] <= 122) || (data[i] >= 65 && data[i] <= 90))
            if (data[i] == 32 || (data[i] >= 97 && data[i] <= 122) || (data[i] >= 65 && data[i] <= 90))
            {
                map.put(key, ++value);
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


    // get the map key for a specific characters.
    // includes spaces and return
    public String getKey(byte ch)
    {
//        // Handle carriage return
//        if (ch == 10)
//        {
//            return "rtn";
//        }

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

    // creates all possible nodes bases on the character map
    // A-Z is converted to lowercase so all alpha characters are lowercase
    // character map also includes the space character and return control character.
    // All other characters are ignored, such as punctuation
    private void createNodes()
    {
        for (String key: this.keys)
        {
           // System.out.println("key: " + key);
            double value = this.map.get(key);
            double probability = value / this.getCharacterCount();
            this.addNode(key, probability, value, null, null);
        }
    }


    // Init the character map.
    // All values are set to zero.
    private void resetCharMap()
    {
        map.put(Character.toString((char) 32), 0.0);
//        map.put("rtn", 0.0);
        for (int i = 97; i <= 122; i++)
        {
            String key = Character.toString((char) i);
            this.map.put(key, 0.0);
        }
    }


    // get the character counter of valid characters based character map.
    // only characters in the character map are counted, punctuation and
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

