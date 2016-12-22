//        Neal Noble
//        IT426
//        Assignment: State Pattern Website
//        Instructor Josh Archer
//        Dec 2016
package greenriver.edu.it;

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