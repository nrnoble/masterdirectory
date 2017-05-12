package com.nrnoble;

/*
* Neal Noble
* May 2017
* Assignment: Trees Part1 and Part 2
* Instructor: Josh Archer
*/

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import static javafx.scene.input.KeyCode.K;
import static javafx.scene.input.KeyCode.V;


/**
 * helper functions
 */
/// BSTSymbolTable<K extends Comparable<K>, V>
public class Utilities <K,V>
{

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

    public static List<Entry> getDictionaryData()
    {
        return getEntriesFromFile("E:\\Data\\Github\\it333\\Iterative Binary Search Tree\\src\\com\\nrnoble\\dictionary.txt");
    }
}



