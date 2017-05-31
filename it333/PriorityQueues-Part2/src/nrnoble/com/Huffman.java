package nrnoble.com;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by Neal on 5/29/2017.
 */
public class Huffman
{
    private byte space = 0b00100000;
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

    Map<String, Float> map = new HashMap<String,Float>();


    private byte[] ascii ={space,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z};
    private byte[] data;
    private byte[] filteredText;

    private int characterCount = 0;


    public Map<String, Float> getMap()
    {
        return map;
    }

    public int[] getFilterCharacters()
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

    public int getCharacterCount()
    {
        return characterCount;
    }

    public Huffman(byte[] data)
    {
        this.data = data;
        initMap();
        filter();
    }


    private void filter()
    {
        this.filteredText = new byte[getFilterCount()];

       // characterCount = 0;
        for (int i = 0; i < this.data.length; i++)
        {
            if (data[i] == 32 || (data[i] >= 97 && data[i] <= 122) || (data[i] >= 65 && data[i] <= 90))
            {
                int toLowerCase = 0;
                if ((data[i] >= 65 && data[i] <= 90))
                {
                    toLowerCase = 32;
                }
                //filteredText[characterCount++] = data[i] + toLowerCase;
                String key1 =  Character.toString((char) (data[i] + toLowerCase));
                String key2 =  Character.toString((char)data[i]);
         //       System.out.println("key: " + key1 + "  " + key2 + "  " + (data[i]+toLowerCase));
         //     System.out.print( key );
                float value = map.get(key1);
                map.put(key1,++value);
                this.characterCount++;
                // Track the occurence of each character;
               // filterCharacters[data[i]]++;

            }
        }
    }

    private void initMap()
    {
        map.put(Character.toString((char) 32), (float)0);
        for (int i = 97; i <= 122; i++)
        {
            String key = Character.toString((char) i);
            this.map.put(key, (float)0);
        }
    }

    private int getFilterCount()
    {

        // if already counted, just return the total
        if (characterCount != 0)
        {
            return characterCount;
        }

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
