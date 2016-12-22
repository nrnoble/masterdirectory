//        Neal Noble
//        IT426
//        Assignment: State Pattern Website
//        Instructor Josh Archer
//        Dec 2016
package greenriver.edu.it;

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