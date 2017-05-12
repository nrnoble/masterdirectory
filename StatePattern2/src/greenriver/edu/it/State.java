//        Neal Noble
//        IT426
//        Assignment: State Pattern Website
//        Instructor Josh Archer
//        Dec 2016
package greenriver.edu.it;

public interface State
{
    public void LoginGranted(StateContext context);
    public void LoginRequested(StateContext context);
    public String getStatus();
}