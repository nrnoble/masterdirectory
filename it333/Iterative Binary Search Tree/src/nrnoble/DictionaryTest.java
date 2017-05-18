package nrnoble;
/*
* Neal Noble
* May 2017
* Assignment: Trees Part2
* Instructor: Josh Archer
*/

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.io.IOException;

import static nrnoble.Utilities.getWords;
import static org.junit.Assert.*;


public class DictionaryTest
{
    private  Dictionary dictionary;
    private static int dictionarySize = 10001;
    public DictionaryTest()
    {

        try
        {
            //dictionary = new Dictionary(getWords(dictionarySize, nrnoble.Utilities.getPath2() + "\\nrnoble\\dictionary.txt"));
            dictionary = new Dictionary(getWords(dictionarySize, Main.dictionaryPath));
        }
        catch (IOException e)
        {
            e.printStackTrace();
        Assert.assertTrue("File IO", false);
    }

        Assert.assertTrue("Number of words is inncorrect", dictionary.size()==dictionarySize);
    }

    @Before
    public void setup()
    {
        try
        {
            //dictionary = new Dictionary(getWords(dictionarySize,"E:\\Data\\Github\\it333\\Iterative Binary Search Tree\\src\\nrnoble\\dictionary.txt"));
          //  dictionary = new Dictionary(getWords(dictionarySize,  nrnoble.Utilities.getPath2() + "\\nrnoble\\dictionary.txt" ));
            dictionary = new Dictionary(getWords(dictionarySize,  Main.dictionaryPath ));
        }
        catch (IOException e)
        {
            e.printStackTrace();
            Assert.assertTrue("File IO", false);
        }

        Assert.assertTrue("Number of words is inncorrect", dictionary.size()==dictionarySize);
    }



    @Test
    public void addWordToDictionary() throws Exception
    {
        System.out.println("dictionary.updateDictionary(\"Basketball\",  \"a sport\"): " + dictionary.updateDictionary("Basketball", "a sport"));
        System.out.println("dictionary.size(): " + dictionary.size());
        Assert.assertEquals("dictionary.size() has failed", dictionary.size(), dictionarySize +1);
        Assert.assertEquals("dictionary.hasWord has failed", dictionary.hasWord("Basketball"), true);
        Assert.assertEquals("dictionary.define() has failed", dictionary.define("Basketball"), "a sport");
    }


    @Test
    public void updateWordDefinition() throws Exception
    {
        addWordToDictionary();

        System.out.println("dictionary.updateDictionary(\"store\",  \"a business that sells goods\"): " + dictionary.updateDictionary("store", "a business that sells goods"));
        System.out.println("dictionary.define(\"store\"): " + dictionary.define("store"));
        System.out.println("dictionary.size(): " + dictionary.size());

        Assert.assertEquals("dictionary.size() has failed", dictionary.size(), dictionarySize +2);
        Assert.assertEquals("hasWord has failed", dictionary.hasWord("store"), true);

        System.out.println("dictionary.updateDictionary(\"Basketball\",  \"a sport\"): " + dictionary.updateDictionary("Basketball", "an American sport first played in 1891"));
        Assert.assertEquals("dictionary.define() has failed", dictionary.define("Basketball"), "an american sport first played in 1891");
        Assert.assertEquals("dictionary.size() has failed", dictionary.size(), dictionarySize +2);
    }


    @Test
    public void hasWord() throws Exception
    {
        Assert.assertEquals("hasWord has failed", dictionary.hasWord("abaca"), true);
    }

    @Test
    public void IrgnoreLeadingSpaces() throws Exception
    {
        Assert.assertEquals("hasWord has failed", dictionary.hasWord("abaca   "), true);
    }

    @Test
    public void IrgnoreTrailingSpaces() throws Exception
    {
        Assert.assertEquals("hasWord has failed", dictionary.hasWord("    abaca"), true);
    }


    @Test
    public void IrgnoreLeadingTrailingSpaces() throws Exception
    {
        Assert.assertEquals("hasWord has failed", dictionary.hasWord("    abaca    "), true);
    }



    @Test
    public void hasFirstDictionaryWord() throws Exception
    {
        Assert.assertEquals("hasWord has failed", dictionary.hasWord("------"), true);
    }


    @Test
    public void hasLastDictionaryWord() throws Exception
    {
        dictionary = new Dictionary(getWords(-1, Main.dictionaryPath));
        System.out.println("dictionary.define(\"zythepsary\"): " + dictionary.hasWord("zythepsary"));
        System.out.println("dictionary.size(): " + dictionary.size());


        Assert.assertEquals("hasWord has failed", dictionary.hasWord("zythepsary"), true);
    }



    @Test
    public void VerifyWordsDoNotExist() throws Exception
    {

        Assert.assertFalse("Store could not be found", dictionary.hasWord("store"));
    }


    @Test
    public void define() throws Exception
    {

        Assert.assertEquals("dictionary.define has failed",dictionary.define("abaca"),"The Manila-hemp plant (Musa textilis); also, its fiber. SeeManila hemp under Manila.".toLowerCase());

    }

    @Test
    public void words() throws Exception
    {

        Assert.assertEquals("dictionary.words() has failed", dictionary.words().size(), dictionarySize);

    }

    @Test
    public void definitions() throws Exception
    {
        Assert.assertEquals("dictionary.definitions() has failed", dictionary.definitions().size(), dictionarySize);
    }

    @Test
    public void size() throws Exception
    {
        Assert.assertEquals("dictionary.size() has failed",dictionary.size(),dictionarySize);
    }

    @Test
    public void isEmpty() throws Exception
    {
        Assert.assertFalse("dictionary.isEmpty() has failed", dictionary.isEmpty());
    }

    @Test
    public void clear() throws Exception
    {
        System.out.println("dictionary.clear()");
        dictionary.clear();
        Assert.assertTrue("dictionary.clear() has failed", dictionary.isEmpty());
        Assert.assertTrue("dictionary.size() has failed", dictionary.size() == 0);
    }


    // These are manual tests that are to be converted over to unit tests.
    @Test
    public void manualTests() throws IOException
    {



        System.out.println("dictionary size(): " + dictionary.size());
        System.out.println("dictionary size(): " + dictionary.size());
        System.out.println("dictionary.hasWord(\"abhorrible\"): " + dictionary.hasWord("abhorrible"));
        System.out.println("dictionary.define(\"abhorrible\"): " + dictionary.define("abhorrible"));
        System.out.println("dictionary.define(\"store\"): " + dictionary.hasWord("store"));
        System.out.println("dictionary.updateDictionary(\"store\", \"to keep in reserve\"): " + dictionary.updateDictionary("store", "to keep in reserve"));
        System.out.println("dictionary.define(\"store\"): " + dictionary.hasWord("store"));
        System.out.println("dictionary.define(\"store\"): " + dictionary.define("store"));
        System.out.println("dictionary.size(): " + dictionary.size());
        System.out.println("dictionary.isEmpty(): " + dictionary.isEmpty());

        System.out.println("dictionary.clear()");
        dictionary.clear();

        System.out.println("dictionary.isEmpty(): " + dictionary.isEmpty());
        System.out.println("dictionary.size(): " + dictionary.size());
        System.out.println("dictionary.define(\"store\"): " + dictionary.hasWord("store"));
        System.out.println("dictionary.updateDictionary(\"store\", \"to keep in reserve\"): " + dictionary.updateDictionary("store", "to keep in reserve"));
        System.out.println("dictionary.size(): " + dictionary.size());
        System.out.println("dictionary.updateDictionary(\"store\",  \"to keep in reserve for future use\"): " + dictionary.updateDictionary("store", "to keep in reserve for future use"));
        System.out.println("dictionary.define(\"store\"): " + dictionary.define("store"));
        System.out.println("dictionary.size(): " + dictionary.size());
        System.out.println("dictionary.updateDictionary(\"store\",  \"a business that sells goods\"): " + dictionary.updateDictionary("store", "a business that sells goods"));
        System.out.println("dictionary.define(\"store\"): " + dictionary.define("store"));
        System.out.println("dictionary.size(): " + dictionary.size());
        System.out.println("dictionary.updateDictionary(\"Basketball\",  \"a sport\"): " + dictionary.updateDictionary("Basketball", "a sport"));
        System.out.println("dictionary.size(): " + dictionary.size());
        System.out.println("dictionary.updateDictionary(\"BASKETBALL\",  \"an american sport\"): " + dictionary.updateDictionary("BASKETBALL", "an american sport"));
        System.out.println("dictionary.size(): " + dictionary.size());
        System.out.println("dictionary.define(\"Basketball\"): " + dictionary.define("Basketball"));
        System.out.println("dictionary.define(\"BASKETBALL\"): " + dictionary.define("BASKETBALL"));
        System.out.println("dictionary.updateDictionary(\"   BASKETBALL    \",  \"an american sport\"): " + dictionary.updateDictionary("   BASKETBALL   ", "an american sport that was first played December 21, 1891"));
        System.out.println("dictionary.define(\"Basketball\"): " + dictionary.define("Basketball"));
        System.out.println("dictionary.define(\"BASKETBALL\"): " + dictionary.define("BASKETBALL"));
        System.out.println("dictionary.size(): " + dictionary.size());
        System.out.println("dictionary.define(\"store\"): " + dictionary.hasWord("store"));
        System.out.println("dictionary.define(\"Store\"): " + dictionary.hasWord("Store"));
        System.out.println("dictionary.define(\"StORe\"): " + dictionary.hasWord("StORe"));
        System.out.println("dictionary.define(\"StORe!\"): " + dictionary.hasWord("StORe!"));
        System.out.println("dictionary.define(\"  store    \"): " + dictionary.hasWord("   store   "));
        System.out.println("dictionary.define(\"store    \"): " + dictionary.hasWord("store   "));
        System.out.println("dictionary.define(\"store\\r\\n    \"): " + dictionary.hasWord("store\r\n   "));
        System.out.println("dictionary.define(\"   store\"): " + dictionary.hasWord("    store"));
        System.out.println("dictionary.define(\"\"): " + dictionary.hasWord(""));
        System.out.println("dictionary.define(\"\"): " + dictionary.hasWord(""));












    }






}