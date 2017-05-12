<!DOCTYPE html>


<html lang="en">

<html>
<head>
    <link rel="stylesheet" href="301.css">
    <script type="text/javascript" src="http://jqueryjs.googlecode.com/files/jquery-1.3.1.min.js" > </script>
    <script type="text/javascript">

        function PrintElem(elem)
        {
            Popup($(elem).html());
        }

        function Popup(data)
        {
            var mywindow = window.open('', 'my div', 'height=400,width=600');
            mywindow.document.write('<html><head><title>my div</title>');
            /*optional stylesheet*/ //mywindow.document.write('<link rel="stylesheet" href="main.css" type="text/css" />');
            mywindow.document.write('</head><body >');
            mywindow.document.write(data);
            mywindow.document.write('</body></html>');

            mywindow.document.close(); // necessary for IE >= 10
            mywindow.focus(); // necessary for IE >= 10

            mywindow.print();
            mywindow.close();

            return true;
        }

    </script>


</head>



<body>


        <div id="anotherdiv" class = "page">
            <h2>Nothing inside this will be printed<h2>
        </div>

        <div class = "page">
            <div id="printtest" class>




                <h1> put whatever you want to print inside this div.</h1>
                <h2> Only the contents with the id='printtest' will be printed</h2>




            </div>

        This line and the BUTTON will not be printed<br>
        <input type="button" value="Print everythining inside <Div id = 'printtest>'" onclick="PrintElem('#printtest')" />

        </div>

        <div class = "page">
            This will not be printed.
        </div>

        <div id="anotherdiv" class = "page">
            <h2>Nothing else on this page will be printed<h2>
        </div>


</body>
</html>