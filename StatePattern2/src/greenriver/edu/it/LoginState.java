//        Neal Noble
//        IT426
//        Assignment: State Pattern Website
//        Instructor Josh Archer
//        Dec 2016
package greenriver.edu.it;

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
