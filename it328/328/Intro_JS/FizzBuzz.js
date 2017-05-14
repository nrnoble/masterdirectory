
var FIZZ = "Fizz";
var BUZZ = "Buzz";
var FIZZ_BUZZ = FIZZ + BUZZ;
var BUZZFACTOR = 5;
var FIZZFACTOR = 3;

function main()
{
    for (var idx = 1; idx <=100 ; idx++)
    {
        "<div>" + getFizzBuzz + "<div>\n\r";
    }
}

/**
 *
 * @param num any Interger value
 * @returns {"Buzz", "FizzBuzz" or orginal value} if the number is divisible by 3 * 5 return "Fizz", divisible
 * by 3 & 5 return "FizzBuzz" otherwise the original value;
 */
function isFizzBuzz(num){

    var fizzResult = getFizz(num);
    var buzzResult = getBuzz(num);

    if (fizzResult == FIZZ  && buzzResult == BUZZ )
    {
        return FIZZ_BUZZ;
    }
    
    return "";

}

/**
 *
 * @param num any Interger value
 * @returns {"Buzz", "FizzBuzz" or orginal value} if the number is divisible by 3 return "Fizz".
 * Ff the number is divisible by 5 return "Buzz"
 * if divisible by 3 & 5 return "FizzBuzz"
 * otherwise the original value;
 */
function getFizzBuzz (num) {

    if (getFizz(num) == FIZZ_BUZZ) {
        return FIZZ_BUZZ;
        }

    if (getFizz(num) == FIZZ){
        return FIZZ;
    }


    return getBuzz(num)
}




/**
 *
 * @param num any Interger value
 * @returns {"Buzz", "FizzBuzz" or orginal value} if the number is divisible by 3 return "Fizz",
 * If divisible by 3 & 5 return "FizzBuzz"
 * otherwise the original value;
 */
function getFizz(num) {

    result = isFizzBuzz(num);
    if (result != "") {
        return result;
    }
    
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

    var result = isFizzBuzz(num);
    if (result != "") {
        return result;
    }
    
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