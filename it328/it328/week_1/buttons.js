/*
Neal Noble
March 30th, 2016
IT328
Assignment introduction to Javascript
*/
function red()
{
    var currentBGColor = document.getElementById("redbtn").style.backgroundColor;
    // alert(currentBGColor);
    if (currentBGColor != "rgb(255, 0, 0)")
    {
        document.getElementById("redbtn").style.backgroundColor = "#FF0000";
        //alert(document.getElementById("redbtn").style.backgroundColor)
    }
    else
    {
        document.getElementById("redbtn").style = "initial" ;
        //alert("color being reset")
    }
}

function white()
{
    var currentBGColor = document.getElementById("whitebtn").style.backgroundColor;
    // alert(currentBGColor);
    if (currentBGColor != "rgb(255, 255, 255)")
    {
        document.getElementById("whitebtn").style.backgroundColor = "#FFFFFF";
    }
    else
    {
        document.getElementById("whitebtn").style = "initial" ;
        //alert("color being reset")
    }
}

function blue()
{
    var currentBGColor = document.getElementById("bluebtn").style.backgroundColor;
    // alert(currentBGColor);
    if (currentBGColor != "rgb(0, 0, 255)")
    {
        document.getElementById("bluebtn").style.backgroundColor = "#0000FF";
    }
    else
    {
        document.getElementById("bluebtn").style = "initial" ;
        //alert("color being reset")
    }
}


function example_1()
{
    foo = 1;
    alert("example#1: foo=" + foo);
    var foo;
}


function example_2()
{
    var foo2;
    foo2 = 1;
    alert("example#2: foo=" + foo2);
}

function example_3()
{
    foo3 = 1;
    alert("example#3: foo=" + foo3);
}


function example_4()
{
    alert("example#4: foo=" + foo4);
    var foo4 = 1;
    alert("example#4: foo=" + foo4);

}


function example_5()
{
    alert("example#5: foo=" + foo5);
    foo5 = 1;
    alert("example#5: foo=" + foo5);
}


function example_6()
{
    var foo6;
    alert("example#6: foo=" + foo6);
    alert("example#6: foo=" + foo6);
}


function example_7()
{
    alert("example#7: foo=" + foo7);
    alert("example#7: foo=" + foo7);
}