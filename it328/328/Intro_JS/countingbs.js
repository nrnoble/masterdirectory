/**
 * Neal Noble
 * Course: IT 328 - Full-Stack Web Development
 * Assignment: Intro to JS
 * May 2017
 * Instructor: Tina Ostrander
 */

// Instructions:
// 3) Write just the countBs function (and the code needed to test it) described on page 56 ("Bean Counting")
// 4) Write the countChar function (and the code needed to test it) described on page 56 ("Bean Counting") in your text.
// 5) Rewrite countBs to use countChar.

// Bean counting
// You can get the Nth character, or letter, from a string by writing "string". harAt(N), similar to
// how you get its length with "s".length. The returned value will be a string containing only one
// character (for example, "b" ). The ﬁrst character has position zero, which causes the last one
// to be found at position string.length - 1. In other words, a two-character string has length 2,
// and its characters have positions 0 and 1. Write a function countBs that takes a string as its
// only argument and returns a number that indicates how many uppercase“B”characters are in the string.
// Next,write a function called countChar that behaves like countBs, except it takes a second argument
// that indicates the character that is to be counted (rather than counting only uppercase “B” characters).
// Rewrite countBs to make use of this new function.



function countingbs() {

    var testStr1 = "Black and Brown Bears";
    var char = "B";
    var count =  countingBs(testStr1);
    console.log ("countingBs returned a count of: " + count);
    unitTest (testStr1,char);

    var testStr2 = "01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100";
    var char = "1";
    unitTest (testStr2,char);
}

function unitTest(testStr,char)
{
    count =  countChar(testStr,char);
    comment = "There are " + count + " characters of '" + char + "'s in the string: '" + testStr +"'";
    console.log(comment);
}


/**
 * Count the number of uppercase "B" there are in a string.
 * @param str input string.
 * @returns Interger number of "B" in the string.
 */
function countingBs(str) {
    return countChar (str,"B");
}


/**
 * Count the number of a specific ascii character there are in the string
 * @param str input string.
 * @param character a single ascii character that is to be counted
 * @returns Interger number of "B" in the string.
 */
function countChar(str,character)
{
    var count = 0;
    for (var idx = 0; idx < str.length; idx++)
    {
        if (str.charAt(idx) == character){
            count++;
        }
    }

    return count;
}