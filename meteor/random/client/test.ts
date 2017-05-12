/**
 * Created by Neal on 5/22/2016.
 */
class Greeter
{
     

    constructor(public greeting: string) { }
    greet()
    {
        return "<h1>" + this.greeting + "</h1>";
    }
};

var greeter = new Greeter("Hello, world!");
var foo = 1;
document.body.innerHTML = greeter.greet();