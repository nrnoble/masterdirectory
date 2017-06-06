package nrnoble.com;

import java.io.IOException;
import java.text.DecimalFormat;
import java.util.*;


public class Main
{
    static private byte[] fileBytes;
    static private String fileName = "";
    static private String path = FileIO.getPath();
    static private Huffman huff = null;
    static private byte[] longVersion, shortVersion;
    static private Huffman huffLongVersion, huffShortVersion = null;
    static private int huffmanBitCount = 0;
    static private DecimalFormat intFormat = new DecimalFormat("#000,000");
    static private DecimalFormat percentFormat = new DecimalFormat("#00.00");

    public static void main(String[] args) throws IOException
    {
//        Huffman huff =  frequencyChart();
//        MaryHeap<HuffmanNode> heap = new MaryHeap(10,2);

 //       Map rawDataStats = huff.getRawDataStats();
  ///      showHuffValues(huff);

      //  System.out.println("path: " + path);
        userLoop();


    }


    public static void showHuffValues(Huffman huff)
    {

        System.out.println("Huffman Values");
        System.out.println();
    String[] keys = huff.getKeys();
    String[] longVersionkeys = huff.getKeys();
        Map charMap = huff.getCharacterNodeMap();
        HuffmanNode node;
        String bits;

        for (String key: keys)
        {
            node = (HuffmanNode)charMap.get(key);
            bits = node.getHuffmanBitString();
            System.out.println(key + ": " + bits);
        }
        System.out.println();
        System.out.println("Total Huffman bits: " + huff.getTotalHuffmanBits());
    }


    private static void comparison()
    {
        System.out.println();
        System.out.println("comparison Bit Output for: " + "\"" + fileName.substring(12) + "\"");
        System.out.println();
        int charCounter = 0;
        String chars = "";
        String bits = "";
        int bitCount = 0;
        
        List<String> linesOfASCIIBits = getaSCIIOutput();
        List<String> linesOfHuffBits = gethuffmanOutput();

        Object[] hufflines = linesOfHuffBits.toArray();
        Object[] asciilines = linesOfASCIIBits.toArray();

        for (int i = 0; i < asciilines.length ; i++)
        {
            System.out.println("  Ascii: " + asciilines[i]);
            System.out.println("Huffman: " + hufflines[i]);
            System.out.println();
        }


        System.out.println();

        double percentage = huff.getTotalHuffmanBits() / huff.getData().length*8;
        System.out.println("  Total ASCII bits: " + huff.getData().length*8);
        System.out.println("Total Huffman bits: " + huff.getTotalHuffmanBits() + "  reduction: " + percentage);
    }

    private static void aSCIIOutput()
    {
        System.out.println();
        System.out.println("ASCII Bit Output for: " + "\"" + fileName.substring(12) + "\"");
        System.out.println();
        int charCounter = 0;
        String chars = "";
        String bits = "";
        int bitCount = 0;

        List<String> linesOfASCIIBits = getaSCIIOutput();

        for (String line: linesOfASCIIBits)
        {
            System.out.println(line);
        }

        System.out.println();
        System.out.println("Total bits: " + huff.getData().length*8);


        System.out.println("");
        huffLongVersion.getTotalHuffmanBits();

    
    }

    private static List<String> getaSCIIOutput()
    {
        List<String> result = new ArrayList<String>();
        int charCounter = 0;
        String chars = "";
        String bits = "";
        String lineOfBits = "";
        int bitCount = 0;
        fileBytes = huff.getData();
        for (byte bite: fileBytes)
        {
            if (bite < 65)
            {
                bite = 32;
            }
            chars = chars + Character.toString((char)bite);

            bits =  huff.asciiToBit(huff.getKey(bite));
            // System.out.print(bits);
            lineOfBits += bits;
            charCounter++;
            bitCount += 8;
            if (charCounter % 10 == 0)
            {
//                System.out.println(" ... " + chars);
                result.add(lineOfBits + " ... " + chars);
                charCounter = 0;
                chars = "";
                lineOfBits = "";
            }
        }
        String  padding = String.join("", Collections.nCopies((80 - lineOfBits.length()), " "));
       // System.out.println(padding + " ... " + chars);
        result.add(lineOfBits + padding + " ... " + chars);
//        System.out.println();
//        System.out.println("Total bits: " + bitCount);

        return result;
    }


    private static void huffmanOutput()
    {
        System.out.println();
        System.out.println("Huffman Bit Output for: " + "\"" + fileName.substring(12) + "\"");
        System.out.println();

        List<String> lines = gethuffmanOutput();

        for (String line:lines)
        {
            System.out.println(line);
        }
        
        System.out.println();
        System.out.println("Total bits: " + huff.getTotalHuffmanBits());
    }


    private static List<String> gethuffmanOutput()
    {
        List<String> returnResults = new ArrayList<>();
        int charCounter = 0;
        String chars = "";
        String bits = "";
        int bitCount = 0;
        fileBytes = huff.getData();
        Map huffNodes =  huff.getCharacterNodeMap();
        int bitsPerLine = 0;
        String lineOfBits = "";
        for (byte bite: fileBytes)
        {
            if (bite < 65)
            {
                bite = 32;
            }

            // create a string to be displayed after bits
            chars = chars + Character.toString((char)bite);

            String str = Character.toString((char)bite).toLowerCase();
            HuffmanNode node  = (HuffmanNode)huffNodes.get(Character.toString((char)bite).toLowerCase());
            bits = node.getHuffmanBitString();
            bitsPerLine += bits.length();
        //    System.out.print(bits);
            lineOfBits += bits; // this is cleared at the end of each line.
            huffmanBitCount += bits.length(); // keep a running total
            charCounter++;
            bitCount += bits.length();
            if (charCounter % 10 == 0)
            {
                String  padding1 = String.join("", Collections.nCopies((80 - bitsPerLine), " "));
               // System.out.println(padding1 + " ... " + chars);
                lineOfBits += padding1 + " ... " + chars;
                returnResults.add(lineOfBits);
                charCounter = 0;
                bitsPerLine = 0;
                chars = "";
                lineOfBits = "";
            }
        }
        String  padding = String.join("", Collections.nCopies((80 - bitsPerLine), " "));
       // System.out.println(padding + " ... " + chars);
        lineOfBits += padding + " ... " + chars;
        returnResults.add(lineOfBits);
       // System.out.println();
       // System.out.println("Total bits: " + huffmanBitCount);

        return returnResults;
    }


    public static Huffman frequencyChart()
    {

        huff = frequencyChartShortVersion();
        System.out.println();
        frequencyChartFullVersion();
        System.out.println();

        return huff;
    }    
    
    
    public static Huffman frequencyChartShortVersion()
    {
//        DecimalFormat intFormat = new DecimalFormat("#000,000");
//        DecimalFormat percentFormat = new DecimalFormat("#00.00");


        //byte[] fileBytes = FileIO.readFile ("E:\\Data\\Github\\it333\\PriorityQueues-Part2\\src\\nrnoble\\com\\war_and_peace.txt");
        //byte[] fileBytes = FileIO.readFile ("E:\\Data\\Github\\it333\\PriorityQueues-Part2\\src\\nrnoble\\com\\war_and_peace_(short).txt");

        System.out.println();
        System.out.println();
        System.out.println("Frequencies for 'war_and_peace_(short).txt'");
        System.out.println("---------------------------------------------");

        //2,969,955
       // System.out.println("        Total characters: " +  intFormat.format (huff.getCharacterCount()));
        // System.out.println("              Total bits: " +  intFormat.format ((huff.getCharacterCount() * 8)));

        huff = huffShortVersion;
        Map map = huff.getRawDataStats();
        int[] characters = huffShortVersion.getCharacters();

        Double value = (Double) map.get(" ");
        double percent = value / huff.getCharacterCount();
        double percentageTotal = percent;
        System.out.println("space: " +  intFormat.format (map.get(" ")) + "   " +  percentFormat.format(percent * 100) +"%");


        double total = characters[32];

        for (int i = 97; i <= 122 ; i++)
        {
            String key = Character.toString((char)i);
            value = (Double)map.get(key);
            percent = value / huff.getCharacterCount();
            percentageTotal = percentageTotal + percent;
            Double keyValue = (Math.floor((Double) map.get(key)));
            String ch = intFormat.format(keyValue);
        System.out.println("    " + key + ": " + ch + "   " + percentFormat.format(percent * 100) +"%");
            total = total + keyValue;

        }

        System.out.println();
        System.out.println("           ASCII characters: " +  intFormat.format (total));
        System.out.println("            ASCII frequency: " +  percentFormat.format (percentageTotal * 100) + "%");
        System.out.println("      Raw ASCII bits loaded: " +   intFormat.format(huff.getData().length * 8));
        System.out.println("Valid bits loaded from file: " +  intFormat.format (huff.getCharacterCount() * 8) + " (invalid bits are new line control characters)");

        System.out.println();
        System.out.println();
        return huff;
    }


    public static Huffman frequencyChartFullVersion()
    {
        DecimalFormat intFormat = new DecimalFormat("#000,000");
        DecimalFormat percentFormat = new DecimalFormat("#00.00%");

        huff = huffLongVersion;
        Map map = huffLongVersion.getRawDataStats();
        int[] characters = huff.getCharacters();

        System.out.println();
        System.out.println();
        System.out.println("Frequencies for 'war_and_peace.txt'");
        System.out.println("---------------------------------------------");



        Double value = (Double) map.get(" ");
        double percent = value / huff.getCharacterCount();
        double percentageTotal = percent;
       // System.out.println("                   space: " +  intFormat.format (rawDataStats.get(" ")) + "   " +  percentFormat.format(percent * 100) +"%");
        System.out.println("space: " +  intFormat.format (map.get(" ")) + "   " +  percentFormat.format(percent));

        double total = characters[32];

        for (int i = 97; i <= 122 ; i++)
        {
            String key = Character.toString((char)i);
            value = (Double)map.get(key);
            percent = value / huff.getCharacterCount();
            percentageTotal = percentageTotal + percent;
            Double keyValue = (Math.floor((Double) map.get(key)));
            String ch = intFormat.format(keyValue);
            //System.out.println("                 " +key + ": " + ch + "   " + percentFormat.format(percent * 100) +"%");
            System.out.println("    " + key + ": " + ch + "   " + percentFormat.format(percent));
            total = total + keyValue;

        }

        System.out.println();
        System.out.println("           ASCII characters: " +  intFormat.format (total));
        System.out.println("            ASCII frequency: " +  percentFormat.format (percentageTotal));
        System.out.println("      Raw ASCII bits loaded: " +   intFormat.format(fileBytes.length * 8));
        System.out.println("Valid bits loaded from file: " +  intFormat.format (huff.getCharacterCount() * 8) + " (invalid bits are new line control characters)");

        System.out.println();
        System.out.println();
        return huff;
    }


    private static void userLoop() throws IOException
    {
        boolean exit = false;
        Scanner textscanner = new Scanner(System.in);
        // Dictionary dictionary = new Dictionary(getWords(1, dictionaryPath));
        // dictionary.clear();

        assignmentHeader();

//        // Get user selection
//        int selection = userInput();

        fileName = "nrnoble/com/war_and_peace.txt";
        longVersion = FileIO.readFile(path + fileName);

        fileName = "nrnoble/com/war_and_peace_(short).txt";
        shortVersion = FileIO.readFile(path + fileName);


        fileName = "nrnoble/com/war_and_peace.txt";
        huffLongVersion = new Huffman(FileIO.readFile(path + fileName));
        fileName = "nrnoble/com/war_and_peace_(short).txt";
        huffShortVersion = new Huffman(FileIO.readFile(path + fileName));

        huff = huffShortVersion;


        while (exit == false)
        {

            // Get user selection
               int selection = userInput();


            // Handle loading of data
            if (selection == 1)
            {
                fileName = "nrnoble/com/war_and_peace.txt";
                fileBytes = FileIO.readFile(path + fileName);
                huff = new Huffman(fileBytes);

            }

            // Handle loading of short version of War and Peace
            if (selection == 2)
            {
                fileName = "nrnoble/com/war_and_peace_(short).txt";
                fileBytes = FileIO.readFile(path + fileName);
                huff = new Huffman(fileBytes);
                //  fileBytes = FileIO.readFile ("E:\\Data\\Github\\it333\\PriorityQueues-Part2\\src\\nrnoble\\com\\war_and_peace_(short).txt");
            }

            if (selection == 1)
            {
                frequencyChart();
            }

            if (selection == 2)
            {
                showHuffValues(huff);
            }

            if (selection == 3)
            {
                aSCIIOutput();
            }

            if (selection == 4)
            {
                huffmanOutput();
            }

            if (selection == 5)
            {
                comparison();
            }

            if (selection == 6)
            {
                frequencyChart();
                showHuffValues(huff);
                aSCIIOutput();
                huffmanOutput();
                comparison();
            }


            if (selection == 8)
            {
                assignment();
            }


            if (selection == 7)
            {
                System.out.println("Exiting");
                break;
            }
        }
    }


    // Process user input
    private static int userInput() throws IOException
    {
        while (true)
        {
            System.out.println();
                System.out.println("1. Frequency Chart");
                System.out.println("2. Huffman Values");
                System.out.println("3. ASCII output");
                System.out.println("4. Huffman output");
                System.out.println("5. Compare ASSCII to Huffman");
                System.out.println("6. All");
                System.out.println("7. Exit");
                System.out.println("---------------------------------------------");
                Scanner scan = new Scanner(System.in);
                int choice = scan.nextInt();
                if (choice == 1 || choice == 2 || choice == 3  || choice == 4  || choice == 5  || choice == 6  || choice == 7 || choice == 8)
                {
                    return choice;
                }

            }
    }


    // Assignment header that is displayed in console.
    public static void assignmentHeader()
    {
        System.out.println();
        System.out.println("    Neal Noble");
        System.out.println("    June 2017  ");
        System.out.println("    Assignment: Priory Queue Part 2");
        System.out.println("    Instructor: Josh Archer");
        System.out.println();
    }


    public static void assignment()
    {
        System.out.println();
        System.out.println();
        System.out.println("Analyzing war and peace(Short).txt");
        frequencyChartShortVersion();
        System.out.println();
        showHuffValues(huff);
        aSCIIOutput();
        huffmanOutput();
        comparison();

        System.out.println("Analyzing war and peace.txt");
        frequencyChartFullVersion();


        System.out.println("ASCII Output");
        System.out.println();
        System.out.println("Total Length: " + intFormat.format(huffLongVersion.getData().length));
        System.out.println();
        System.out.println("Hufmman Output");
        System.out.println();
        System.out.println("Total Length: " + intFormat.format(huffLongVersion.getTotalHuffmanBits()));
        System.out.println();
        System.out.println();
    }
}


