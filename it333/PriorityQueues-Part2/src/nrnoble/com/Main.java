package nrnoble.com;

import java.util.Map;


public class Main
{
    public static void main(String[] args)
    {
        Huffman huff =  showStats();
        Map map = huff.getMap();

    }

    public static Huffman showStats()
    {
        //  byte[] fileBytes = FileIO.readFile ("E:\\Data\\Github\\it333\\PriorityQueues-Part2\\src\\nrnoble\\com\\war_and_peace.txt");
        byte[] fileBytes = FileIO.readFile ("E:\\Data\\Github\\it333\\PriorityQueues-Part2\\src\\nrnoble\\com\\war_and_peace_(short).txt");
        Huffman huff = new Huffman(fileBytes);

        //2,969,955
        System.out.println("Total characters: " + huff.getCharacterCount());
        System.out.println("Total bits: " + (huff.getCharacterCount() * 8));
        Map map = huff.getMap();
        int[] characters = huff.getFilterCharacters();

        float value = (float)map.get(" ");
        float percent = value / huff.getCharacterCount();
        float percentageTotal = percent;
        System.out.println("space: " + map.get(" ") + "  " +  percent * 100 +"%");

        int total = characters[32];

        for (int i = 97; i <= 122 ; i++)
        {
            String key = Character.toString((char) i);
            value = (float)map.get(key);
            percent = value / huff.getCharacterCount();
            percentageTotal = percentageTotal + percent;
          //  String ch = Strng.format ("%07d", characters[i]);
            String ch = String.format ("%07d", map.get(key));

            System.out.println( key + ": " + ch + "   " + percent * 100 +"%");
            total = total + characters[i];

        }

        System.out.println();
         System.out.println("Total characters: " + total);
         System.out.println("Total percentage: " + percentageTotal * 100 + "%");

        return huff;
    }


}


