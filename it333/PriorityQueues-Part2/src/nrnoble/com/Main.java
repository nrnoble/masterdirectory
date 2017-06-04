package nrnoble.com;

import java.text.DecimalFormat;
import java.util.Map;


public class Main
{
    public static void main(String[] args)
    {
        Huffman huff =  showStats();
        MaryHeap<HuffmanNode> heap = new MaryHeap(10,2);

        Map map = huff.getMap();

//        HuffmanNode hNode2 = huff.huffNodes.delMax();
//        System.out.print("HuffmanNode hNode2 = huff.huffNodes.delMax() ");
//        System.out.println(hNode2.toString());

        while(!huff.huffNodes.isEmpty())
        {
            HuffmanNode hNode = huff.huffNodes.delMax();
//            HuffmanNode hNode = huff.huffNodes.delMin();
            System.out.println(hNode.toString());
        }

    }

    public static Huffman showStats()
    {
        DecimalFormat intFormat = new DecimalFormat("#000,000");
        DecimalFormat percentFormat = new DecimalFormat("#00.00");


        // byte[] fileBytes = FileIO.readFile ("E:\\Data\\Github\\it333\\PriorityQueues-Part2\\src\\nrnoble\\com\\war_and_peace.txt");
         byte[] fileBytes = FileIO.readFile ("E:\\Data\\Github\\it333\\PriorityQueues-Part2\\src\\nrnoble\\com\\war_and_peace_(short).txt");
        System.out.println("total raw bits loaded from file: " +   intFormat.format(fileBytes.length * 8));
        Huffman huff = new Huffman(fileBytes);
        System.out.println("total filtered bits loaded from file: " +  intFormat.format (huff.getCharacterCount() * 8));


        //2,969,955
        System.out.println("Total characters: " +  intFormat.format (huff.getCharacterCount()));
        System.out.println("Total bits: " +  intFormat.format ((huff.getCharacterCount() * 8)));
        Map map = huff.getMap();
        int[] characters = huff.getCharacters();

        Double value = (Double) map.get(" ");
        double percent = value / huff.getCharacterCount();
        double percentageTotal = percent;
        System.out.println(" space: " +  intFormat.format (map.get(" ")) + "   " +  percentFormat.format(percent * 100) +"%");

        value = (Double)map.get("rtn");
        percent = value / huff.getCharacterCount();
        percentageTotal = percentageTotal + percent;
        System.out.println("return: " +  intFormat.format(map.get("rtn")) + "   " + percentFormat.format(percent * 100) +"%");

        double total = characters[32];

        for (int i = 97; i <= 122 ; i++)
        {
            String key = Character.toString((char)i);
            value = (Double)map.get(key);
            percent = value / huff.getCharacterCount();
            percentageTotal = percentageTotal + percent;
          //  String ch = Strng.format ("%07d", characters[i]);
            Double keyValue = (Math.floor((Double) map.get(key)));

            // System.out.print(key + " ");
            // System.out.println(keyValue);
            // String ch = String.format ("%07d",  keyValue);

//            DecimalFormat intFormat = new DecimalFormat("#000,000");
            String ch = intFormat.format(keyValue);
            System.out.println("     " +key + ": " + ch + "   " + percentFormat.format(percent * 100) +"%");
            total = total + keyValue;

        }

        System.out.println();
         System.out.println("Total characters: " +  intFormat.format (total));
         System.out.println("Total percentage: " +  percentFormat.format (percentageTotal * 100) + "%");

        return huff;
    }


    public static void showSkippedExcludedCharacters(Huffman huff)
    {
        for (int item : huff.debugSkippedCharacters)
        {
            System.out.print(item + " ");
        }
    }

}


