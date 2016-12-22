<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


    <style type="text/css">

        pre.prettyprint{
            width: auto;
            overflow: auto;
            max-height: 350px
        }

        body
        {
            text-align:justify;
            font-family: courier;
            font-size: 10pt;
            background-color:#4A62E8;
        }


        a:hover
        {
            background-color: yellow;
            color:blue;
            font-size: 14pt;
            font-weight: bold;
        }

        a
        {
            text-decoration: none;
        }


        b
        {
            color:blue;
        }

        th
        {
            text-decoration: underline;

        }

        tr:nth-child(even)
        {
            background-color: #E0E0E0;
        }

        #text
        {
            text-align: left;
            font-size: 10pt;

        }
        div
        {
            font-size: 10pt;
            margin: auto;
        }


        .page
        {
            font-family: Verdana;
            max-width: 800px;
            font-size: 12pt;
            background-color: #ffffff;
            border: solid;
            border-width: 1px;
            text-align: left;
            margin-top: 10px;
            padding: 10px;
            box-shadow: 5px 5px 5px #0026FF
        }

        #page
        {
            max-width: 500px;
            font-size: 12pt;
            background-color: #ffffff;
            border: solid;
            border-width: 1px;
            text-align: left;
            margin-top: 100px;
            padding: 10px;
            box-shadow: 5px 5px 5px #0026FF
        }
    </style>

    <title>Assignment: State Pattern</title>
</head>

<body>


<div id="assignmentinfo"  class="page">
    State Pattern<br>
    Neal Noble<br>
    IT-426<br>
    Dec 2016<br><br>

    NOTE: Click on each header to toggle expansion
</div>


<div id = "idDefinition" class ="page">
    <h3>Definition</h3>
    <p style="padding-left: 30px;">
        <span style="font-size: 14pt;">
            <em>Allow an object to alter its behavior when its internal state changes.
                The object will appear to change its class. - Gang of Four
            </em>
        </span>
    </p>

</div>


<div id = "idUML" class ="page" onclick="$(idUMLBody).toggle()">
    <h3 data-toggle="tooltip" title="Click to expand\collapse content">UML: State Pattern</h3>
    <div id="idUMLBody" style="display: none">
        <p><img src="../images/statepattern.gif"  alt="" width="762" height="231" /></p>
    </div>
</div>


<div id = "idExplained" class ="page" onclick="$(idExplainedBody).toggle()" >
    <h3 data-toggle="tooltip" title="Click to expand\collapse content">State Pattern Explained</h3>
    <DIV id="idExplainedBody"  style="display: none">
        <p>An easy to understand example of the State pattern is an individual person. An individual in the
            context of an computer application would be considered an generic object with basic automatic
            functions, walk, talk, etc, but the individual can take on additional functionality when put
            into a different contexts, such as a college student, an employee, &nbsp;or parent. When the
            state of the individual changes to one of the three, the behavior of the individual changes,
            but the individual remains the same (object). The State pattern allows the object to remain the
            same by changing the state of the object, thus the behavior changes to handle requirements of
            each state.</p>
    </DIV>
</div>


<div id = "idParticipants" class ="page" onclick="$(idParticipantsBody).toggle()">
    <h3 data-toggle="tooltip" title="Click to expand\collapse content">Participants</h3>
    <div id ="idParticipantsBody" style="display: none">
        <ul>
            <li><strong>Context</strong>&nbsp;&nbsp;<strong>(Individual)</strong>
                <ul>
                    <li>defines the interface of interest to clients</li>
                    <li>maintains an instance of a ConcreteState subclass that defines the current state.</li>
                </ul></li>
            <li><strong>State</strong>&nbsp;&nbsp;<strong>(State)</strong>
                <ul>
                    <li>defines an interface for encapsulating the behavior associated with a particular state of the Context.</li>
                </ul></li>
            <li><strong>Concrete State</strong>&nbsp;&nbsp;<strong>(Student, Employee, Parent)</strong>
                <ul>
                    <li>each subclass implements a behavior associated with a state of Context</li>
                </ul></li>
        </ul>
    </div>
</div>


<div id = "idRoles" class ="page" onclick="$(idRolesBody).toggle()" style="display: none">
    <h3 data-toggle="tooltip" title="Click to expand\collapse content">Roles</h3>
    <div id ="idRolesBody" style="display: none">
        test
    </div>
</div>


<div id = "idExample" class ="page" onclick="$(idExampleBody).toggle()">
    <h3 data-toggle="tooltip" title="Click to expand\collapse content">Example: Authentication Object</h3>
    <div id="idExampleBody"  style="display: none">
        The previous example helps make the State pattern easy to understand, but to code an "individual" as state pattern
        could get complex. For a code example, an "authentication" object is a better choice be used because it’s an object
        that is more practical in terms of creating code.
    </div>
</div>


<div id = "idClassDiagram" class ="page" onclick="$(idClassDiagramBody).toggle()">
    <h3 data-toggle="tooltip" title="Click to expand\collapse content">Class Diagram: Authentication Object</h3>
    <div id="idClassDiagramBody" style="display: none">
        <p><img src="../images/statepatternuml.PNG"  alt="" width="750"></p>
    </div>
</div>


<div id = "idCodeSample" class ="page" onclick="$(idCodeSampleBody).toggle()">
    <h3 data-toggle="tooltip" title="Click to expand\collapse content">Code sample: Authentication Object</h3>
    <DIV id="idCodeSampleBody"  style="display: none">

<!--public class StateClient-->
        <p style="padding-left: 30px;">
            <span style="font-size: 10pt;">
                [<a href="StatePattern-Java.zip">Download Java Source</a>]<br><br>
                <strong>public class StateClient</strong> Main() is the starting point of the application where the StateContext object is created, then execute the individual methods. Each method
                will change the state of the object demonstrating that the object to switch a subclass\object internally
            </span>
        </p>
        <pre class="prettyprint linenums run code-hscroll">
public class StateClient
{
    public static void main(String[]args) {
        StateContext context = new StateContext();
        context.acceptApplication();
        context.requestPermission();
        context.grantPermission();
        System.out.println(context.getStatus());
    }
}
        </pre><br>


<!--public interface State-->
        <p style="padding-left: 30px;">
            <span style="font-size: 10pt;">
                <strong>public interface State</strong>. defines the interfaces for all subclasses. All the subclasses have the same interfaces even if some of the methods
                serve no practical purpose for some of the subclasses. If method does not have any function within a specific subclass, a subclass could do nothing,
                throw an error, or respond by changing the state.
            </span>
        </p>
        <pre class="prettyprint linenums run code-hscroll">
public interface State
{
    public void LoginGranted(StateContext context);
    public void LoginRequested(StateContext context);
    public String getStatus();
}
        </pre><br>

        <!--public abstract class StateContext implements State-->
        <p style="padding-left: 30px;">
            <span style="font-size: 10pt;">
                <strong>public abstract class StateContext implements State</strong>
            </span>
        </p>
        <pre class="prettyprint linenums run code-hscroll">
public abstract class StateContext implements State
{
    private State loginState;
    private State loginRequest;
    private State grantedState;

    private State state;

    public StateContext()
    {
        loginState = new LoginState();
        loginRequest = new LoginRequested();
        grantedState = new LoginGranted();
        state = null;
    }

    public void acceptApplication() {
        this.state = loginState;
    }

    public void requestPermission() {
        state.LoginRequested(this);
    }

    public void grantPermission() {
        state.LoginGranted(this);
    }

    public String getStatus() {
        return state.getStatus();
    }

    public void setState(State state) {
        this.state = state;
    }

    public State getAcceptedState() {
        return loginState;
    }

    public State getGrantedState() {
        return grantedState;
    }

    public State getRequestedState() {
        return loginRequest;
    }

}
    </pre><br>


<!--public class LoginGranted implements State-->
        <p style="padding-left: 30px;">
            <span style="font-size: 10pt;">
                <strong>public class LoginGranted implements State</strong>
            </span>
        </p>
        <pre class="prettyprint linenums run code-hscroll">
public class LoginGranted implements State
{
    public void LoginGranted(StateContext ctx)
    {
        System.out.println("Invalid login");
    }
    public void LoginRequested(StateContext context)
    {
        System.out.println("Invalid login");
    }

    public String getStatus()
    {
        return "Login Granted";
    }
}
    </pre><br>


<!--public class LoginRequested implements State-->
        <p style="padding-left: 30px;">
            <span style="font-size: 10pt;">
                <strong>public class LoginRequested implements State</strong>
            </span>
        </p>
        <pre class="prettyprint linenums run code-hscroll">
public class LoginRequested implements State
{
    public void LoginGranted(StateContext context)
    {

    }
    public void LoginRequested(StateContext context)
    {
        System.out.println("Requesting login");
        context.setState(context.getRequestedState());
    }

    public String getStatus()
    {
        return "Request Received";
    }
}
    </pre><br>


<!--public class LoginState implements State-->
        <p style="padding-left: 30px;">
            <span style="font-size: 10pt;">
                <strong>public class LoginState implements State</strong>
            </span>
        </p>
        <pre class="prettyprint linenums run code-hscroll">
public class LoginState implements State
{
    public void LoginGranted(StateContext context)
    {
        System.out.println("You are now logged into the system");
        context.setState(context.getGrantedState());
    }
    public void LoginRequested(StateContext context)
    {
        System.out.println("Login already requested");
    }
    public String getStatus()
    {
        return "Login Permission";
    }
}
    </pre>



    </div>
</div>


<div id = "idTemplate" class ="page" onclick="$(idTemplateBody).toggle()"  style="display: none" >
    <h3 data-toggle="tooltip" title="Click to expand\collapse content">Template</h3>
    <div id="idTemplateBody" style="display: none">
        Template
    </div>
</div>


<div id = "idCodeTemplate" class ="page" onclick="$(idCodeTemplateBody).toggle()"  style="display: none" >
    <h3 data-toggle="tooltip" title="Click to expand\collapse content">State Pattern Code Template</h3>
        <div id="idCodeTemplateBody" style="display: none">
        <script src="https://gist.github.com/nrnoble/3a4b9686d3eb84c79adc1a52ab8995e8.js"></script>

    </div>
</div>


<div id = "idCompareToOtherPatterns" class ="page" onclick="$(idCompareToOtherPatternsBody).toggle()">
    <h3 data-toggle="tooltip" title="Click to expand\collapse content">Related Patterns</h3>
    <div id ="idCompareToOtherPatternsBody" style="display: none" >
        <a href="http://www.cs.unc.edu/~stotts/GOF/hires/pat5ifso.htm">Strategy Pattern</a><br>
        <img src="../images/StrategyPattern.PNG"  alt="" width="600"><br><br>
        <a href="http://www.cs.unc.edu/~stotts/GOF/hires/pat5gfso.htm">Observer Pattern</a><br>
        <img src="../images/ObserverPattern.PNG"  alt="" width="600">
    </div>
</div>


<div id = "idSources" class ="page" onclick="$(idSourcesBody).toggle()">
    <h3 data-toggle="tooltip" title="Click to expand\collapse content">Sources</h3>
    <div id="idSourcesBody" style="display: none">
        <A href="http://java-x.blogspot.com/2006/12/implementing-state-pattern-in-java.html">Implementing State Pattern in Java</a><br>
        <A href="http://www.cs.unc.edu/~stotts/GOF/hires/pat5hfso.htm">Design Patterns - Gang of Four</a><br>

        <A href="http://www.dofactory.com/net/state-design-pattern">State .NET Design Pattern in C# and VB - dofactory.com</a><br>
        <A href="https://catalog.imagine.microsoft.com/en-us/Catalog/Product/99">Azure for students</A><br>
    </div>
</div>


<div id = "validate" class="page">

    <script>
        var url = $(location).attr('href');
        var url1 = "<a href='https://html5.validator.nu/?doc=" + url + "&showsource=yes'  target=\"#mytarget\">Validate this page</a>";
        $('#validate').html(url1);
    </script>


    <script>
        $("https://html5.validator.nu/?doc=http%3A%2F%2Fnnoble.greenrivertech.net%2F9%2Ficecream.php&showsource=yes").load();
    </script>
</div>


<div id= source class="page" onclick="$(sourecode).toggle();" style="margin-top: 10px;">

    <H3>Web Page Source Code</H3>

    <div id="sourecode" style="display: none">
        <?php
        highlight_file(__FILE__);
        ?>
    </div>
</div> <!--id = source -->

<script>
    $(document).ready(function(){
        $('[data-toggle="tooltip"]').tooltip();
    });
</script>

</body>

</html>
