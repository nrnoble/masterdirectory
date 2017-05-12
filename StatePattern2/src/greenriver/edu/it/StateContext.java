//        Neal Noble
//        IT426
//        Assignment: State Pattern Website
//        Instructor Josh Archer
//        Dec 2016
package greenriver.edu.it;


public class StateContext
{
    private State loginState;
    private State loginRequested;
    private State grantedState;

    //    private State loginState;
//    private State loginRequest;
//    private State grantedState;


    private State state;

    public StateContext() {
        loginState = new LoginState();
        loginRequested = new LoginRequested();
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
        return loginRequested;
    }

}