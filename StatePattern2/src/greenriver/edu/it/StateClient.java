//        Neal Noble
//        IT426
//        Assignment: State Pattern Website
//        Instructor Josh Archer
//        Dec 2016
package greenriver.edu.it;

//public class StateClient extends StateContext
//{
//    public static void main(String[] args)
//    {
//        StateContext context = new StateClient();
//        context.acceptApplication();
//        context.requestPermission();
//        context.LoginGranted(context);
//        System.out.println(context.getStatus());
//    }
//    public void LoginGranted(StateContext context)
//    {
//
//    }
//
//    public void LoginRequested(StateContext context)
//    {
//
//    }
//
//}


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