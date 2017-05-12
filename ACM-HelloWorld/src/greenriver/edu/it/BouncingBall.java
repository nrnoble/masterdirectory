package greenriver.edu.it;

/*
 * File: BouncingBall.java
 * -----------------------
 * This file implements a simple bouncing ball using the run method
 * to drive the animation.
 */

import greenriver.edu.it.program.*;

public class BouncingBall extends GraphicsProgram {

/** Initialize the ball and its velocity components */
	public void init() {
		ball = new GBall(BALL_RADIUS);
		add(ball, getWidth() / 2, getHeight() / 2);
		dx = 2;
		dy = 1;
	}

/** Run forever bouncing the ball */
	public void run() {
		waitForClick();
		while (true)
		{
			advanceOneTimeStep();
			pause(PAUSE_TIME);
		}
	}

/* Check for bounces and advance the ball */
	private void advanceOneTimeStep()
	{
		double bx = ball.getX();
		double by = ball.getY();
		if (bx < BALL_RADIUS || bx > getWidth() - BALL_RADIUS) dx = -dx;
		if (by < BALL_RADIUS || by > getHeight() - BALL_RADIUS) dy = -dy;
		ball.move(dx, dy);
	}

/* Private constants */
	private static final double BALL_RADIUS = 10;
	private static final int PAUSE_TIME = 20;

/* Private instance variables */
	private GBall ball;     /* The ball object                   */
	private double dx;      /* Velocity delta in the x direction */
	private double dy;      /* Velocity delta in the y direction */

/* Standard Java entry point */
/* This method can be eliminated in most Java environments */
	public static void main(String[] args) {
		new BouncingBall().start(args);
	}
}
