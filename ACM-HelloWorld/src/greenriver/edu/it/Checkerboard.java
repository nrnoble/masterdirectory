package greenriver.edu.it;/*
 * File: greenriver.edu.it.Checkerboard.java
 * -----------------------
 * This program draws a checkerboard.  The dimensions of the
 * checkerboard is specified by the constants NROWS and
 * NCOLUMNS, and the size of the squares is chosen so
 * that the checkerboard fills the available vertical space.
 */

import greenriver.edu.it.graphics.*;
import greenriver.edu.it.program.*;

public class Checkerboard extends GraphicsProgram {

/** Runs the program */
	public void run() {
		double sqSize = (double) getHeight() / NROWS;
		for (int i = 0; i < NROWS; i++) {
			for (int j = 0; j < NCOLUMNS; j++) {
				double x = j * sqSize;
				double y = i * sqSize;
				GRect sq = new GRect(x, y, sqSize, sqSize);
				sq.setFilled((i + j) % 2 != 0);
				add(sq);
			}
		}
	}

/* Private constants */
	private static final int NROWS = 8;     /* Number of rows    */
	private static final int NCOLUMNS = 8;  /* Number of columns */

/* Standard Java entry point */
/* This method can be eliminated in most Java environments */
	public static void main(String[] args) {
		new Checkerboard().start(args);
	}
}
