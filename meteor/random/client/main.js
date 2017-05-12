import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';

import './main.html';
//import { test } from './server/main.js';
var loopCount = 0;

Template.hello.onCreated(function helloOnCreated() {
  // counter starts at 0
    this.counter = new ReactiveVar(0);
    this.randomNumber = new ReactiveVar(0);
    this.randomNumbers = new ReactiveVar(randomizeNumbers(1,10,5));
    this.myTestRandomNumbers = new ReactiveVar(randomizeNumbers(1,10,5));
    this.mySequence = new ReactiveVar([]);
    this.myLoopCount = new ReactiveVar(0);
    loopCount = this.myLoopCount;
});

Template.hello.helpers({
    randomNumbers_2()
    {
        return Template.instance().mySequence.get();
    },

    myLoopCount ()
    {
        return Template.instance().myLoopCount .get();
    },

    randomNumbers()
    {
        console.log("return Template.instance().randomNumber.get()");
        return Template.instance().randomNumber.get();
    },
    serverCounter()
    {
        console.log("return serverloopCount.get()");
        //return serverloopCount.get();
    },
    testRandomNumbers()
    {

        var randNums = Template.instance().myTestRandomNumbers.get();
        console.log("return Template.instance().myTestRandomNumbers.get(): {" + randNums +"}");
        return  randNums;
    }
});


var testRandomNumber = 1;


var running = false;
var mainLoop = null;
var instanceMySequence = null;

Template.hello.events({
    'click button'(event, instance)
    {


        // increment the counter when button is clicked
        instance.randomNumbers.set(randomizeNumbers(1,10,5));
        instance.randomNumber.set(randomizeNumbers(1,5,5));
        instance.myTestRandomNumbers.set(randomizeNumbers(1,5,5));
        instance.mySequence.set(sequence);

        instanceMySequence = instance.mySequence;
        running = !running;

        if (running)
        {
            mainLoop = setInterval(main, 5);

        }
        else
        {
            clearInterval(mainLoop);
        }

        //console.log("sequence: " + sequence);
        ///console.log("loopCount: " + loopCount);
        // shuuffledNumbers = randomizeNumbers(1,10,5);
        testRandomNumber =  getRandomNumber(1,10);
        console.log("testRandomNumber: " + testRandomNumber);
        // console.log("myRandomNumber: " + myRandomNumber);
    }
});

// returns a random number between low and high paramenters
export function getRandomNumber (low, high)
{
    high++;
    return Math.floor (Math.random() * (high - low) + low);
}



var length = 10;
var sequence = new Array(length).fill(0);
var mainLoopCounter = 0;
function main()
{
    mainLoopCounter++;
    //console.log("loopCount: " + loopCount);
    numbers = randomizeNumbers(1,length,length);

    for (var idx = 0; idx < length; idx++)
    {
        if (numbers[idx] != idx + 1)
        {
            //console.log("instanceMySequence: " + instanceMySequence);
            if(idx == 4)
            {
                loopCount.set(mainLoopCounter);
                instanceMySequence.set(sequence);
            }
            return;
        }
        sequence[idx]++;
    }



    // if (numbers[0] != 1)
    // {
    //     //console.log("instanceMySequence: " + instanceMySequence);
    //     instanceMySequence.set(sequence);
    //     return;
    // }

    // sequence[0]++;
    // if (numbers[1] != 2)
    // {
    //     //console.log("instanceMySequence: " + instanceMySequence);
    //     instanceMySequence.set(sequence);
    //     return;
    // }
    //
    // sequence[1]++;
    // if (numbers[2] != 3)
    // {
    //     //console.log("instanceMySequence: " + instanceMySequence);
    //     instanceMySequence.set(sequence);
    //     return;
    // }
    //
    // sequence[2]++;
    // if (numbers[3] != 4)
    // {
    //   //  console.log("instanceMySequence: " + instanceMySequence);
    //     instanceMySequence.set(sequence);
    //     return;
    // }
    //
    // sequence[3]++;
    // if (numbers[4] != 5)
    // {
    //     //console.log("instanceMySequence: " + instanceMySequence);
    //     instanceMySequence.set(sequence);
    //     return;
    // }
    //
    // sequence[4]++;
    //console.log("instanceMySequence.mySequence: " + instanceMySequence.mySequence);
    instanceMySequence.set(sequence);
    return;

}




// causes the the current execution thread to sleep for a period of time in milliseconds
// 1000 = 1 second
export function sleep(delay)
{
  var start = new Date().getTime();
  while (new Date().getTime() < start + delay);
}



// returns an array of randomized numbers
export function randomizeNumbers(low, high, shuffleCount)
{

  var total = high - low;
  var randomNumbers = [];

    // console.log("total: " + total);
  for (var idx = 0; idx <= total; idx++)
  {
      randomNumbers[idx] = idx+1;
      //console.log("randomNumbers[" + idx + "]: " + randomNumbers[idx]);

  }
    randomNumbers = myShuffle(randomNumbers,shuffleCount);

   // console.log("return randomNumbers");
    return randomNumbers;
}


export function myShuffle(arrayObj, shuffleCount)
{
  // console.log("entering myShuffle(arrayObj, shuffleCount)");
  var numberOfElements = arrayObj.length;

    //console.log("numberOfElements: " + numberOfElements);
    for (var idx = 0; idx < shuffleCount; idx++)
    {
      //  console.log("idx: " + idx);
        for (var idx2 = 0; idx2 < numberOfElements; idx2++)
        {
            //console.log("idx2: " + idx2);
            var tmp = arrayObj[idx2];
            var randomNumber    = getRandomNumber(0,numberOfElements-1);
            arrayObj[idx2] = arrayObj[randomNumber];
            arrayObj[randomNumber] = tmp;
        }
    }

    //console.log("Exiting myShuffle(arrayObj, shuffleCount)");
    return arrayObj;
}