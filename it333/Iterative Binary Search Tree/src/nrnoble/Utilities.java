package nrnoble;

/*
* Neal Noble
* May 2017
* Assignment: Trees Part1 and Part 2
* Instructor: Josh Archer
*/

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;


/**
 * helper functions
 */

public class Utilities
{


    /**
     * Get the relative path for the executing application
     * @return {String} Path of the executing application
     */
    public static String getPath2()
    {
        String path1 = Main.class.getProtectionDomain().getCodeSource().getLocation().getPath();
        String decodedPath = null;
        try
        {
            decodedPath = URLDecoder.decode(path1, "UTF-8");
        } catch (UnsupportedEncodingException e)
        {
            e.printStackTrace();
        }
        decodedPath = decodedPath.substring(1);
        return decodedPath;
    }


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
     * @return Entry object with the parsed NodeData into key\value pair
     */
    public static Entry parseLines(String line)
    {
        String[] lines = line.split(":");
        Entry entry = new Entry(lines[0], lines[1]);
        return entry;
    }



    /**
     *  Return a specific number of words from daw dictionary NodeData file.
     *  1 - 86,000. If less than 1, then return max. If greater, then return max.
     * @param numberOfWords the number of words to be extracted from the data data file
     * @param  file path to the dictionary file
     * @return  a specific number of words from daw dictionary file.
     * @throws IOException when there is as file IO
     */
    public static List<Entry> getWords(int numberOfWords, String path) throws IOException
    {
        List<String> lines = readTextFile(path);
        List<Entry> sublist = new ArrayList<>();
        int counter = 0;

        if (numberOfWords <= 0 || numberOfWords > lines.size())
        {
            numberOfWords =  lines.size();
        }

        while (counter < numberOfWords  && counter < lines.size())
        {
            String line = lines.get(counter++);
            sublist.add(parseLines(line));
        }

        return sublist;
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


    public static List<Entry> getDictionaryData()
    {
        try
        {
            return getEntriesFromFile( Main.dictionaryPath);
        } catch (IOException e)
        {
            e.printStackTrace();
        }
        return null;
    }
}



