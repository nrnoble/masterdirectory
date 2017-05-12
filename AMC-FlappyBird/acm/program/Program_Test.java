package acm.program;

import greenriver.edu.it.io.IOModel;

import greenriver.edu.it.gui.*;
import greenriver.edu.it.io.*;
import greenriver.edu.it.util.*;
import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;

/**
 * Created by Neal on 1/1/2017.
 */
public abstract  class Program_Test extends JApplet
        implements IOModel, Runnable, MouseListener, MouseMotionListener,
        KeyListener, ActionListener {


    /* Private constants */
    private static final int DEFAULT_X = 16;
    private static final int DEFAULT_Y = 40;
    private static final int DEFAULT_WIDTH = 754;
    private static final int DEFAULT_HEIGHT = 492;
    private static final int PRINT_MARGIN = 36;

    /* Private instance variables */
    private ArrayList<Object> finalizers;
    private HashMap<String,String> parameterTable;
    private JFrame programFrame;
    private AppletStub appletStub;
    private String myTitle;
    private ProgramMenuBar myMenuBar;
    private Component northBorder;
    private Component southBorder;
    private Component eastBorder;
    private Component westBorder;
    private JPanel northPanel;
    private JPanel southPanel;
    private JPanel eastPanel;
    private JPanel westPanel;
    private JPanel centerPanel;
    private IOConsole myConsole;
    private IODialog myDialog;
    private IOModel inputModel;
    private IOModel outputModel;
    private Object startupObject;
    private AppletStarter appletStarter;
    private Rectangle programBounds;
    private boolean started;
    private boolean shown;
    private boolean initFinished;
    private boolean appletMode;







    private String getMyCaller() {
        StackTraceElement[] stack = new Throwable().getStackTrace();
        return stack[2].getClassName() + "." + stack[2].getMethodName();
    }

    public int getWidth() {
        String caller = getMyCaller();
        if (caller.startsWith("java.") || caller.startsWith("javax.")) {
            return super.getWidth();
        } else {
            return getCentralRegionSize().width;
        }
    }

/* Overridden method: getHeight() */
    /**
     * Returns the height of the central region.
     *
     * @usage int height = getHeight();
     * @return The height of the central region
     * @noshow
     */
    public int getHeight() {
        String caller = getMyCaller();
        if (caller.startsWith("java.") || caller.startsWith("javax.")) {
            return super.getHeight();
        } else {
            return getCentralRegionSize().height;
        }
    }

    /* Method: getCentralRegionSize() */
    /**
     * Returns the size of the central region.  If the content pane has
     * not been validated, this method computes its preferred size by
     * subtracting the sizes required for the side panels from the size
     * of the entire frame.
     *
     * @return The size of the central region
     */
    public Dimension getCentralRegionSize() {
        if (centerPanel == null) return super.getSize();
        if (initFinished) return centerPanel.getSize();
        Dimension size = (programFrame == null) ? super.getSize() : programFrame.getSize();
        Insets insets = (programFrame == null) ? super.getInsets() : programFrame.getInsets();
        size.width -= westPanel.getPreferredSize().width + eastPanel.getPreferredSize().width;
        size.width -= insets.left + insets.right;
        size.height -= northPanel.getPreferredSize().height + southPanel.getPreferredSize().height;
        size.height -= insets.top + insets.bottom;
        return size;
    }


}
