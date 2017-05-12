import javax.swing.*;
import java.awt.*;

public class Main
{

    public static void main(String[] args) {


        JFrame frame = new JFrame("form2");
        frame.setContentPane(new form2().myjpanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
        centreWindow(frame);

        System.out.println("Compiled successfully");
    }


    public static void centreWindow(Window frame) {
        Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();
        int x = (int) ((dimension.getWidth() - frame.getWidth()) / 2);
        int y = (int) ((dimension.getHeight() - frame.getHeight()) / 2);
        frame.setLocation(x, y);
    }

}
