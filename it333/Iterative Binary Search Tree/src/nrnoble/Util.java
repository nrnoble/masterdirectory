package nrnoble;

import java.io.IOException;
import java.net.URL;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Neal on 5/16/2017.
 */
public class Util
{


//    public static String getPath()
//    {
//        URL rootPath = getClass().getResource("");
//        String URI=rootPath.toString().substring(9);
//        String[] currentPath=URI.split("myjar.jar!");
//        currentPath[0]=currentPath[0].replaceAll("%20"," ");
//        return currentPath[0];
//    }


    /**
     * Read a text file into to List
     * @param filePath full path to text file
     * @return List of strings
     * @throws IOException is thrown when there are errors reading file
     */
    public static List<String> readTextFile (String filePath) throws IOException
    {
        List<String> lines = Files.readAllLines(Paths.get(filePath), Charset.defaultCharset());
        return lines;
    }



    /**
     * Helper function for part II of Tree assignment.
     * Parses a line into word and definition
     * @param line that contains
     * @return Entry object with the parsed data into key\value pair
     */
    public static Entry parseLines(String line)
    {

        String[] lines = line.split(":");
        Entry entry = new Entry(lines[0], lines[1]);
        return entry;
    }


    public static List<Entry> getEntriesFromFile(String path) throws IOException
    {
        List<Entry> entryList = new ArrayList<>();
        List<String> lines = readTextFile(path);

        for (String line: lines)
        {
            Entry entry = parseLines(line);
            entryList.add(entry);
        }

        return entryList;
    }


    public static List<Entry> getDictionaryData() throws IOException
    {

        return getEntriesFromFile("dictionary.txt");
//
//        try                          //  E:\\Data\\Github\\it333\\Iterative Binary Search Tree\\src\\nrnoble\\dictionary.txt
//        {                            //  E:\\Data\\Github\\it333\\Iterative Binary Search Tree\\src\\nrnoble\\dictionary.txt
//            return getEntriesFromFile("E:\\Data\\Github\\it333\\Iterative Binary Search Tree\\src\\nrnoble\\dictionary.txt");
//        } catch (IOException e)
//        {
//            e.printStackTrace();
//        }
//
//        return null;
    }


}
