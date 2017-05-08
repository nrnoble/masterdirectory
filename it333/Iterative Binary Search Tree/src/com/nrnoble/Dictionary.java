package com.nrnoble;

/*
* Neal Noble
* May 2017
* Assignment: Trees Part1
* Instructor: Josh Archer
*/

import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

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
         */
        public Dictionary(String[] words, String[] definitions)
        {

        }

        /**
         * Returns true if the input word is in the dictionary, otherwise false.
         * @param word a single string word
         * @return true if the input word is in the dictionary
         */
        public boolean hasWord(String word)
        {
            return true;
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

            return new String();
        }


        /**
         * Returns an ordered list of words from the dictionary. There should be no duplicates in the result list.
         * @return Returns an ordered list of words from the dictionary.
         */
        public List<String> words()
        {
            return null;
        }


        /**
         * Returns an unordered list of definitions from the dictionary.
         * @return an unordered list of definitions from the dictionary.
         */
        public List<String> definitions()
        {
            return null;

        }


        /**
         * Returns the number of words in the dictionary.
         * @return the number of words in the dictionary.
         */
        public int size()
        {
            return 0;
        }


        /**
         * 	Returns true if the dictionary has no words, otherwise false.
         * @return true if the dictionary has no words, otherwise false.
         */
        public boolean isEmpty()
        {

            return true;
        }


        /**
         * 	Removes all words from the dictionary.
         */
        public void clear()
        {

        }
    }

