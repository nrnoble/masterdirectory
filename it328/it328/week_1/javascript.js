//change the <p> tag below
function bold() {
    document.getElementById("title").innerHTML = "FAVORITE Sports Team";
}

function foo() {
    var i = 10;
    document.write(i);
}

//store a function in a variable
var myFoo = function() { //anonymous function!
    //alert("Hello world!");
};

myFoo();

//print out the types in Javascript
document.write(typeof "John"); //string
document.write("<br>");
document.write(typeof 100.0);
document.write("<br>");
document.write(typeof false); //boolean
document.write("<br>");
document.write(typeof foo);
document.write("<br>");
document.write(typeof myFoo);
document.write("<br>");
document.write(typeof [1, 2, 3, 4]); //the type of arrays is object in JS
document.write("<br>");
document.write(typeof {showName: "Orphan Black", year: "2013"});
document.write("<br>");

var publisher = {
    name: "Harper Torch",
    location: "New York",
    year: 1993
}

//create a useful JS object
var book = {
    author: "Pablo Coelho",
    title: "The Alchemist",
    publishing: publisher,
    genres: ["quest", "survival", "fantasy", "drama"],
    synopsis: "Quest and stuff...."
};

document.write("Author: " + book.author);
document.write("<br>");
document.write("Title: " + book.title);
document.write("<br>");
document.write("First genre: " + book.genres[3]);
document.write("<br>");
document.write("Publisher location: " + book.publishing.location);
document.write("<br>");