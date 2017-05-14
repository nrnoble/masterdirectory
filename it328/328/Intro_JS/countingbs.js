/**
 * Neal Noble
 * Course: IT 328 - Full-Stack Web Development
 * Assignment: Intro to JS
 * May 2017
 * Instructor: Tina Ostrander
 */


// Instructions:
// 3) Write just the countBs function (and the code needed to test it) described on page 56 ("Bean Counting")
// in your text.


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
    var count =  countingBs(testStr1);
    var comment = "There are " + count + " characters of 'B's in the string: '" + testStr1 +"'";
    console.log(comment);

    var testStr2 = "1011001110100101";
    var char = "1";
    count =  countChar(testStr2,char);
    comment = "There are " + count + " characters of '" + char + "'s in the string: '" + testStr2 +"'";
    console.log(comment);


}


function countingBs(str)
{
    return countChar (str,"B");
}


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