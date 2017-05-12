<div style='direction:ltr;border-width:100%'>

    <div style='direction:ltr;margin-top:0in;margin-left:0in;width:6.109in'>

        <div style='direction:ltr;margin-top:.4305in;margin-left:0in;width:6.109in'>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>Hoisting is
                something that is not that difficult to understand which is <span
                style='text-decoration:underline'>at runtime the jS interrupter raises the declarations of variables to
                the top of the current scope</span> as if the developer had put them there. Seems Simple and straight
                forward, but what is puzzling and difficult to understand are the reasons behind the underlining design,
                as well as less-than-obvious changes behavior when hoisting occurs.</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>Examples 1-3 all
                have the same logical behavior</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <div style='direction:ltr'>

                <table border=1 cellpadding=0 cellspacing=0 valign=top style='direction:ltr;
 border-collapse:collapse;border-style:solid;border-color:#A3A3A3;border-width:
 1pt;margin-left:.3333in'>
                    <tr>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
  vertical-align:top;width:1.0444in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt;color:#458383'><span
                                    style='background:white'>Example #1</span></p>
                        </td>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
  vertical-align:top;width:1.0444in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt;color:#458383'><span
                                    style='background:white'>Example #2</span></p>
                        </td>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
                            vertical-align:top;width:.9055in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt;color:#458383'><span
                                    style='background:white'>Example #3</span></p>
                        </td>
                    </tr>
                    <tr>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
                            vertical-align:top;width:1.0638in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt'>foo = 1;</p>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt'>alert(foo);</p>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt'>var foo;</span></p>
                        </td>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
                            vertical-align:top;width:1.0638in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt'><span
                                    style='font-weight:bold;color:navy;'>var</span> foo;</span></p>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt'>foo = 1</p>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt'>alert(foo);</p>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt;color:#7A7A43'>&nbsp;</p>
                        </td>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
                            vertical-align:top;width:.9805in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt'>foo = 1;</span></p>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt'>alert(foo);</p>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt;color:#7A7A43'>&nbsp;</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="width:1.3in; text-align: center;"><button id ="bt1" onclick="example_1()">
                                Test Example #1</button></td>
                        <td style="width:1.3in; text-align: center;"><button id ="bt2" onclick="example_2()">
                                Test Example #2</button></td>
                        <td style="width:1.3in; text-align: center;"><button id ="bt3" onclick="example_3()">
                                Test Example #3</button></td>
                    </tr>
                </table>


            </div>

            <p style='margin:0in;margin-left:.375in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <p style='margin:0in;margin-left:.375in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>All Examples 1 - 3
                are the same as:</p>

            <p style='margin:0in;margin-left:.375in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <div style='direction:ltr'>

                <table border=1 cellpadding=0 cellspacing=0 valign=top style='direction:ltr;
 border-collapse:collapse;border-style:solid;border-color:#A3A3A3;border-width:
 1pt;margin-left:.3333in'>
                    <tr>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
  vertical-align:top;width:1.1597in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt'><span
                                style='font-weight:bold;color:navy;background:white'>var </span><span
                                style='color:#458383;background:white'>foo </span><span style='color:black;
  background:white'>= </span>
                                <span style='color:blue;background:white'>1</span><span
                                style='color:black;background:white'>;</span></p>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt'><span
                                style='color:#7A7A43;background:white'>alert</span><span style='color:black;
  background:white'>(</span><span
                                style='color:#458383;background:white'>foo</span><span
                                style='color:black;background:white'>);</span></p>
                        </td>
                    </tr>
                </table>

            </div>

            <p style="page-break-after:always;"></p>
            <p><!-- pagebreak --></p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>However, these
                examples #4 and #5, appear almost exactly the same, yet provide different
                results.</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <div style='direction:ltr'>

                <table border=1 cellpadding=0 cellspacing=0 valign=top style='direction:ltr;
 border-collapse:collapse;border-style:solid;border-color:#A3A3A3;border-width:
 1pt;margin-left:.3333in'>
                    <tr>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
  vertical-align:top;width:.9715in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt;color:#458383'><span
                                    style='background:white'>Example #4</span></p>
                        </td>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
  vertical-align:top;width:.8895in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt;color:#458383'><span
                                    style='background:white'>Example #5</span></p>
                        </td>
                    </tr>
                    <tr>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
  vertical-align:top;width:.952in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:Calibri;font-size:11.0pt;color:#0033CC'><span
                                    style='font-style:italic'>alert(foo);</span></p>
                            <p style='margin:0in;font-family:Calibri;font-size:11.0pt;color:#0033CC'><span
                                    style='font-style:italic'>var foo = 1;</span></p>
                            <p style='margin:0in;font-family:Calibri;font-size:11.0pt;color:#0033CC'><span
                                    style='font-style:italic'>alert(foo);</span></p>
                        </td>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
  vertical-align:top;width:.8395in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:Calibri;font-size:11.0pt;color:#0033CC'>alert(foo);</p>
                            <p style='margin:0in;font-family:Calibri;font-size:11.0pt;color:#0033CC'>foo
                                = 1;</p>
                            <p style='margin:0in;font-family:Calibri;font-size:11.0pt;color:#0033CC'>alert(foo);</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="width:1.3in; text-align: center;"><button id ="bt1" onclick="example_4()">
                                Test Example #4</button></td>
                        <td style="width:1.3in; text-align: center;"><button id ="bt2" onclick="example_5()">
                                Test Example #5</button></td>

                    </tr>
                </table>
                <p style = "margin-left:.3333in">Note: nothing happens when executing the code
                for example #5</p>

            </div>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>During the code execution of example #4, <span
                    style='font-style:italic;background:yellow;mso-highlight:yellow'>var foo</span> is
                hoisted to the top of the scope and becomes logically equivalent to example #6,
                and, example#5 becomes logically equivalent example# 7</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <div style='direction:ltr'>

                <table border=1 cellpadding=0 cellspacing=0 valign=top style='direction:ltr;
 border-collapse:collapse;border-style:solid;border-color:#A3A3A3;border-width:
 1pt;margin-left:.3333in'>
                    <tr>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
  vertical-align:top;width:.9888in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt;color:#458383'><span
                                    style='background:white'>Example #6</span></p>
                        </td>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
  vertical-align:top;width:.9069in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:"Courier New";font-size:9.0pt;color:#458383'><span
                                    style='background:white'>Example #7</span></p>
                        </td>
                    </tr>
                    <tr>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
  vertical-align:top;width:.9694in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:Calibri;font-size:11.0pt;color:#0033CC'><span
                                    style='font-style:italic'>var foo;</span></p>
                            <p style='margin:0in;font-family:Calibri;font-size:11.0pt;color:#0033CC'><span
                                    style='font-style:italic'>alert(foo);</span></p>
                            <p style='margin:0in;font-family:Calibri;font-size:11.0pt;color:#0033CC'><span
                                    style='font-style:italic'>alert(foo);</span></p>
                        </td>
                        <td style='border-style:solid;border-color:#A3A3A3;border-width:1pt;
  vertical-align:top;width:.8569in;padding:2.0pt 3.0pt 2.0pt 3.0pt'>
                            <p style='margin:0in;font-family:Calibri;font-size:11.0pt;color:#0033CC'>alert(foo);</p>
                            <p style='margin:0in;font-family:Calibri;font-size:11.0pt;color:#0033CC'>alert(foo);</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="width:1.3in; text-align: center;"><button id ="bt6" onclick="example_6()">
                                Test Example #6</button></td>
                        <td style="width:1.3in; text-align: center;"><button id ="bt7" onclick="example_7()">
                                Test Example #7</button></td>
                    </tr>
                </table>
                <p style = "margin-left:.3333in">Note: nothing happens when executing the code
                    for example #7</p>

            </div>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>When comparing the the examples #4 &amp;
                #6, taken note that the value assigned to foo is dropped when hoisting the declaration to the
                top of the scope. In examples #5 &amp; #7, <span style='background:yellow;
                mso-highlight:yellow'>foo</span> is
                removed as undeclared variable.</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'><span
                    style='mso-spacerun:yes'> </span>Any further examples beyond this point become more complex
                and even confusing to unravel, and from what I've read about hoisting so far, it
                all leads to the same recommendation:<span style='mso-spacerun:yes'>  </
                span><span
                    style='font-weight:bold;text-decoration:underline;color:#0033CC'>Declare all variables
                    at the top of scope</span></p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>

            <p style='margin:0in;font-family:Calibri;font-size:11.0pt'>I've yet figure out
                how to use hoisting to do something that is unique, which speeds us the
                application, reduces amount of code to be written, or simply achieves something
                that can only be accomplished using hoisting.<span style='mso-spacerun:yes'>
                </span>All the articles I've read so far are explanations on how hoisting works
                and how to avoid problems relating to it. It would be interesting to read an
                article titled something like: &quot;<i>JavaScript: How to leverage hoisting to make
                    scripts more powerful, faster, and require less code.</i>&quot;</p>

        </div>

    </div>

</div>