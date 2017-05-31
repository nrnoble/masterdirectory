/**
 * Neal Noble
 * Course: IT 328 - Full-Stack Web Development
 * Assignment: Intro to JS
 * May 2017
 * Instructor: Tina Ostrander
 */

var FIZZ = "Fizz";
var BUZZ = "Buzz";
var FIZZ_BUZZ = FIZZ + BUZZ;
var BUZZFACTOR = 5;
var FIZZFACTOR = 3;

function fizzBuzz() {
    for (var idx = 1; idx <=100 ; idx++) {
        var line = "<div>" + getFizzBuzz(idx) + "<div>\n\r";
        console.log(getFizzBuzz(idx));
        //document.write(line);
    }
}

/**
 *
 * @param num any Interger value
 * @returns {"Buzz", "FizzBuzz" or orginal value} if the number is divisible by 3 return "Fizz".
 * if the number is divisible by 5 return "Buzz"
 * if divisible by 3 & 5 return "FizzBuzz"
 * otherwise the original value;
 */
function getFizzBuzz (num) {

        var fizzResult = getFizz(num);
        var buzzResult = getBuzz(num);

        if (fizzResult == FIZZ && buzzResult == BUZZ)
        {
            return FIZZ_BUZZ;
        }

        if (fizzResult == FIZZ)
        {
            return FIZZ;
        }

        if (buzzResult == BUZZ)
        {
            return BUZZ;
        }

        return num;
}


/**
 *
 * @param num any Interger value
 * @returns {"Buzz", "FizzBuzz" or orginal value} if the number is divisible by 3 return "Fizz",
 * If divisible by 3 & 5 return "FizzBuzz"
 * otherwise the original value;
 */
function getFizz(num) {

    if (isDevisible(num,FIZZFACTOR)) {
        return FIZZ;
    }
    
    return num;
}


/**
 * 
 * @param num any Interger value
 * @returns {"Buzz", "FizzBuzz" or orginal va} if the number is divisible by 5 return "Buzz",
 * If divisible by 3 & 5 return "FizzBuzz"
 * otherwise the original value;
 */
function getBuzz(num){

    if (isDevisible(num,BUZZFACTOR)) {
        return BUZZ;
    }

    return num;
}


/**
 * 
 * @param num any interger number
 * @param divnum the devisor number
 * @returns {boolean} returns true of the number has no remainder
 */
function isDevisible(num, divnum) {
    if (num % divnum == 0)
    {
        return true;
    }

    return false;
}