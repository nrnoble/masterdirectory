import { Meteor } from 'meteor/meteor';

export var foo = 0;
export var serverloopCount = 0;
var TIMER_DELAY = 1000;
Meteor.startup(() =>
{
    this.serverLoopCount = new ReactiveVar(0);
    serverloopCount = this.serverLoopCount;
   // gameInstance = setInterval(serverMain, TIMER_DELAY);
});


export var mainServerLoopCounter = 0;
function serverMain()
{
    mainServerLoopCounter++;
    serverloopCount.set(mainServerLoopCounter);
    var foo = serverloopCount;
    console.log("serverloopCount: " + serverloopCount.get());
   
}

export function test()
{
    return serverloopCount;
}

