package nrnoble.com;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class Huffman
{
    private byte space = 0b00100000;
    private byte rtn   = 0b00001010;
    private byte a = 0b01100001;
    private byte b = 0b01100010;
    private byte c = 0b01100011;
    private byte d = 0b01100100;
    private byte e = 0b01100101;
    private byte f = 0b01100110;
    private byte g = 0b01100111;
    private byte h = 0b01101000;
    private byte i = 0b01101001;
    private byte j = 0b01101010;
    private byte k = 0b01101011;
    private byte l = 0b01101100;
    private byte m = 0b01101101;
    private byte n = 0b01101110;
    private byte o = 0b01101111;
    private byte p = 0b01110000;
    private byte q = 0b01110001;
    private byte r = 0b01110010;
    private byte s = 0b01110011;
    private byte t = 0b01110100;
    private byte u = 0b01110101;
    private byte v = 0b01110110;
    private byte w = 0b01110111;
    private byte x = 0b01111000;
    private byte y = 0b01111001;
    private byte z = 0b01111010;

    Map<String, Double> map = new HashMap<String,Double>();
    Map<String,HuffmanNode> characterNodeMap = new HashMap<String,HuffmanNode>();
    private byte[] ascii ={space,rtn,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z};
    private byte[] data;
    private byte[] filteredText;
    private int rawCharacterCount;
    public MaryHeap<HuffmanNode> huffNodes= new MaryHeap<HuffmanNode>(10,3);
    private String[] keys = new String[]{" ","rtn","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
    private final String NULL = "\\u000";
    private int characterCount = 0;

    // debug variables
    // list of characters that have been filtered out because they are not part A-Z + space.
    protected List<Byte> debugSkippedCharacters = new ArrayList<>();



    /**
     * Huffman constructor
     * @param rawFileData the raw rawFileData from a file'
     */
    public Huffman(byte[] rawFileData)
    {
        this.data = rawFileData;
        this.resetCharMap();
        this.calcProbablity();
        this.createNodes();
        this.combineNodes();
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
    public HuffmanNode combineTwoNodes(HuffmanNode hNode1, HuffmanNode hNode2)
    {
        String combinedKey = hNode1.getKey() + "." + hNode2.getKey();
        double combinedFreq = hNode1.getProbability() + hNode2.getProbability();
        double combinedCount = hNode1.getCharacterCount() + hNode2.getCharacterCount();
        HuffmanNode combinedNode = new  HuffmanNode(NULL,combinedFreq,combinedCount,hNode1,hNode2,null);
        hNode1.setParent(combinedNode);
        hNode2.setParent(combinedNode);
        return combinedNode;
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

            if (data[i] == 10 || data[i] == 32 || (data[i] >= 97 && data[i] <= 122) || (data[i] >= 65 && data[i] <= 90))
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
    private String getKey(byte ch)
    {
        // Handle carriage return
        if (ch == 10)
        {
            return "rtn";
        }

        return  Character.toString((char)ch).toLowerCase();
    }


    // creates a single node and inserts into to the heap
    private void addNode(String key, double probablity, double characterCount, HuffmanNode leftNode, HuffmanNode rightNode)
    {
        HuffmanNode hNode = new HuffmanNode(key, probablity, characterCount, leftNode, rightNode,null);
        huffNodes.insert(hNode);
        characterNodeMap.put(key,hNode);
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
        map.put("rtn", 0.0);
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

