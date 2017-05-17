package nrnoble;
/*
* Neal Noble
* May 2017
* Assignment: Trees Part2
* Instructor: Josh Archer
*/


import java.util.Iterator;
import java.util.List;


/**
 * A dictionary class that stores word-definition pairs
  */

    public class Dictionary
    {
        private BSTSymbolTable<String, String> words;


        /**
         * Adds a word/definition pair to the dictionary if the input word is not presently in the dictionary.
         * Otherwise, the method will update the definition for an already existing word.
         * @param words array of words
         * @param definitions array of definations for each word
         * This method throws an IllegalArgumentException if the size of the both input arrays differ.
         * This method throws an IllegalStateException if the elements of the words array are not in sorted order.
         */
        public Dictionary(String[] words, String[] definitions)
        {
            addArrayOfWords(words,definitions);
        }


        private void addArrayOfWords(String[] words, String[] definitions)
        {
            // Check to determine if words and defs are 1:1
            if (words.length != definitions.length)
            {
                throw new IllegalArgumentException("The length of arrays must be equal.");
            }

            // check if list is in sorted order, if not, throw IllegalStateException
            if (!sortCheck (words))
            {
                throw new IllegalStateException("The data must be presorted from smallest to largest");
            }

            // add words with definitions to dictionary

            this.words = new BSTSymbolTable();

            System.out.println("words.length: " + words.length);
            for (int i = 0; i < words.length; i++)
            {
                if ((i % 10000) == 0)
                {
                    System.out.print(i + ", ");
                }
                this.updateDictionary (words[i],definitions[i]);
            }
        }


        /**
         * Adds a word/definition pair to the dictionary if the input word is not presently in the dictionary.
         * Otherwise, the method will update the definition for an already existing word.
         * @param List of Entries that contains key/value pair of words with their definition
         * This method throws an IllegalArgumentException if the size of the both input arrays differ.
         * This method throws an IllegalStateException if the elements of the words array are not in sorted order.
         */
        public Dictionary(List<Entry> entries)
        {
            String[] words =  new String[entries.size()];
            String[] definitions = new String[entries.size()];
            int count=0;

            Iterator itr = entries.iterator();
            while(itr.hasNext())
            {
                Entry entry = (Entry)itr.next();
                words[count] = entry.getKey().toLowerCase().trim();
                definitions[count] = entry.getValue().toLowerCase().trim();
                count++;
            }

            addArrayOfWords(words, definitions);
        }


        // check the order of words. Return true of they are in a-z order
        private boolean sortCheck(String[] words)
        {
            String word = words[0];
            for (int i = 1; i < words.length; i++)
            {
                if (word.toLowerCase().trim().compareTo(words[i].toLowerCase().trim()) == 1)
                {
                    return false;
                }
                word = words[i];
            }

            return true;
        }



        /**
         * Adds a word/definition pair to the dictionary if the input word is not presently in the dictionary.
         * Otherwise, the method will update the definition for an already existing word.
         * @param word string to be added or updated in the dictionary
         * @param definition string that is to be added or updated
         * @return true if successful.
         */
        public boolean updateDictionary(String word, String definition)
        {
            this.words.put(word.toLowerCase().trim(), definition.toLowerCase().trim());
            return true;
        }



        /**
         * Returns true if the input word is in the dictionary, otherwise false.
         * @param word a single string word
         * @return true if the input word is in the dictionary
         */
        public boolean hasWord(String word)
        {
            return this.words.containsKey(word.toLowerCase().trim());
        }


        /**
         *
         * Returns the definition of the input word from the dictionary.
         * This method throws a NoSuchElementException if the word is not found in the dictionary.
         * @param word to be looked up in the dictionary
         * @return the definition of the input word from the dictionary.
         */
        public String define(String word)
        {
            if (this.words.get(word.toLowerCase().trim()) == null)
            {
                return "";
            }

            return this.words.get(word.toLowerCase().trim());
        }


        /**
         * Returns an ordered list of words from the dictionary. There should be no duplicates in the result list.
         * @return Returns an ordered list of words from the dictionary.
         */
        public List<String> words()
        {
            return this.words.keys();
        }


        /**
         * Returns an unordered list of definitions from the dictionary.
         * @return an unordered list of definitions from the dictionary.
         */
        public List<String> definitions()
        {
            return this.words.values();
        }


        /**
         * Returns the number of words in the dictionary.
         * @return the number of words in the dictionary.
         */
        public int size()
        {

            return this.words.size();
        }


        /**
         * 	Returns true if the dictionary has no words, otherwise false.
         * @return true if the dictionary has no words, otherwise false.
         */
        public boolean isEmpty()
        {

            return this.words.isEmpty();
        }


        /**
         * 	Removes all words from the dictionary.
         */
        public void clear()
        {
            this.words.clear();
        }
    }

