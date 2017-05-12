<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/styles.css">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


    <script src="https://code.jquery.com/jquery-1.10.2.js"></script>

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
            font-size: 8pt;
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
            font-size: 8pt;

        }
        div
        {
            font-size: 8pt;
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


<div id = "idExplained" class ="page" onclick="$(idExplainedBody).toggle()" >
    <h3>State Pattern Explained</h3>
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


<div id = "idRoles" class ="page" onclick="$(idRolesBody).toggle()" style="display: none">
    <h3>Roles</h3>
    <div id ="idRolesBody" style="display: none">
        test
    </div>
</div>


<div id = "idUML" class ="page" onclick="$(idUMLBody).toggle()">
    <h3>UML</h3>
    <div id="idUMLBody" style="display: none">
        <p><img src="/StatePattern/images/statepattern.gif"  alt="" width="762" height="231" /></p>
    </div>
</div>


<div id = "idExample" class ="page" onclick="$(idExampleBody).toggle()">
    <h3>Example</h3>
    <div id="idExampleBody"  style="display: none">
        Demonstrate State pattern using a login authentication object
    </div>
</div>


<div id = "idClassDiagram" class ="page" onclick="$(idClassDiagramBody).toggle()">
    <h3>Class Diagram</h3>
    <div id="idClassDiagramBody" style="display: none">
        <p><img src="/StatePattern/images/statepatternuml.PNG"  alt="" width="750"></p>
    </div>
</div>


<div id = "idCodeSample" class ="page" onclick="$(idCodeSampleBody).toggle()">
    <h3>Code sample</h3>
    <DIV id="idCodeSampleBody"  style="display: none">
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
    </pre>

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
    </pre>

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

        <pre class="prettyprint linenums run code-hscroll">
public interface State
{
    public void LoginGranted(StateContext context);
    public void LoginRequested(StateContext context);
    public String getStatus();
}
    </pre>

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
    </pre>
    </div>
</div>


<div id = "idTemplate" class ="page" onclick="$(idTemplateBody).toggle()"  style="display: none" >
    <h3>Template</h3>
    <div id="idTemplateBody" style="display: none">
        Template
    </div>
</div>


<div id = "idParticipants" class ="page" onclick="$(idParticipantsBody).toggle()">
   <h3>Participants</h3>
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


<div id = "idCompareToOtherPatterns" class ="page" onclick="$(idCompareToOtherPatternsBody).toggle()">
    <h3>Related Patterns</h3>
    <div id ="idCompareToOtherPatternsBody" style="display: none" >
        <a href="http://www.cs.unc.edu/~stotts/GOF/hires/pat5ifso.htm">Strategy</a><br>
        <a href="http://www.cs.unc.edu/~stotts/GOF/hires/pat5gfso.htm">Observer</a>
    </div>
</div>


<div id = "idSources" class ="page">
    <h3>Sources</h3>
    <A href="http://java-x.blogspot.com/2006/12/implementing-state-pattern-in-java.html">Implementing State Pattern in Java</a><br>
    <A href="http://www.cs.unc.edu/~stotts/GOF/hires/pat5hfso.htm">Design Patterns - Gang of Four</a>

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
