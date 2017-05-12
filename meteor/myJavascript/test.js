/**
 * Created by Neal on 5/2/2016.
 */

function getRandomBingoNumber (low, high)
{
    return Math.floor (Math.random() * (high - low) + low)
}


function columnNumbers(low,high)
{
    var column = [5];
    var numberCount = 1;
    column[0] =  getRandomBingoNumber (low, high);
    while (numberCount <= 5)
    {
        var randomNumber = getRandomBingoNumber (low, high);
        for (i = 0; i < 5; i++)
        {
            if(column[i] ==  undefined)
            {
                column[i] = randomNumber;
                numberCount++;
                break;
            }

            if (column[i] !=  randomNumber)
            {
                continue;
            }


            if (column[i] ==  randomNumber)
            {
                break;
            }

        }
    }

}

function foo()
{
    var count =2;
    count++;
    return count;
}

var myObj = new Object();

myObj.counter = foo();
myObj.somefunction = function (){

    return this.counter;
};

var tst = foo();
WScript.Echo(myObj.somefunction());

//columnNumbers(1,15);
