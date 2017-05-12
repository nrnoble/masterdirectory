package acm;

import java.awt.Color;
import java.awt.Font;
import java.awt.event.KeyEvent;

import acm.graphics.GLabel;
import acm.graphics.GRect;
import acm.program.GraphicsProgram;
import acm.util.RandomGenerator;

public class FlappyBirdGame extends GraphicsProgram
{
	private static final int APPLET_WIDTH = 900;
	private static final int APPLET_HEIGHT = 700;
	private static final int GRASS_HEIGHT = 20;
	private static final int DIRT_HEIGHT = 50;
	private static final double GRAVITY = 0.15;
	private static final int PIPE_WIDTH = 100;
	private static final int MIN_PIPE_HEIGHT = 100;
	private static final int MAX_PIPE_HEIGHT = 400;
	private static final int PIPE_MOVEMENT = 3;
	private static final int PIPE_GAP = 150;
	
	private FlappyBird bird;
	private GRect grass;
	private double birdVelocity;
	
	private GRect[] pipes = new GRect[6];
	private GLabel scoreLabel;
	private double score;
	
	public void init()
	{
		setSize(APPLET_WIDTH, APPLET_HEIGHT);
		setBackground(new Color(153, 255, 255));
		
		//response to up arrows
		addKeyListeners();
	}
	
	public void run()
	{
		//build the scene
		addShapes();
		
		//play the game
		playGame();
	}
	
	public void playGame()
	{
		boolean continueGame = true;
		
		birdVelocity = 0.0;
		
		while (continueGame)
		{
			//pull the bird with gravity
			birdVelocity += GRAVITY;
			
			//animate the bird
			
			//make sure the bird does not collide with the top of the screen
			if (bird.getY() + birdVelocity >= 0)
			{
				bird.move(0, birdVelocity);
			}
			
			//check for the bird colliding with the bottom of the screen
			if (bird.getY() + bird.getHeight() > grass.getY())
			{
				continueGame = false;
			}
			
			//move the pipes
			for (int i = 0; i < pipes.length; i++)
			{
				//move the pipe
				pipes[i].move(-PIPE_MOVEMENT, 0);
				
				//check if the pipe is off the screen
				if (pipes[i].getX() + pipes[i].getWidth() <= 0)
				{
					pipes[i].setLocation(APPLET_WIDTH, pipes[i].getY());
					updateScore();
				}
				
				//check for collisions with flappy bird
				if (bird.getBounds().intersects(pipes[i].getBounds()))
				{
					continueGame = false;
					break;
				}
			}
			
			pause(20);
		}
	}
	
	public void addShapes()
	{
		//add the bird
		bird = new FlappyBird();
		bird.assemble();
		
		add(bird, 20, 100);
		
		//add the ground
		grass = new GRect(-1, APPLET_HEIGHT - DIRT_HEIGHT - GRASS_HEIGHT, 
								APPLET_WIDTH + 1, GRASS_HEIGHT);
		
		grass.setFilled(true);
		grass.setFillColor(Color.GREEN);
		add(grass);
		
		//add the ground
		GRect dirt = new GRect(-1, APPLET_HEIGHT - DIRT_HEIGHT, 
								APPLET_WIDTH + 1, DIRT_HEIGHT);
		
		dirt.setFilled(true);
		dirt.setFillColor(new Color(238, 213, 183));
		add(dirt);
		
		//add the obstacles
		addPipes();
		
		//score keeping
		addScore();
	}
	
	public void updateScore()
	{
		score += 0.5; 
		
		scoreLabel.setLabel("Score: " + (int)score);
	}
	
	public void addScore()
	{
		scoreLabel = new GLabel("Score: 0");
		scoreLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 30));
		
		add(scoreLabel, (APPLET_WIDTH / 2) - 30, APPLET_HEIGHT - (DIRT_HEIGHT / 2) + 10);
	}
	
	public void addPipes()
	{
		RandomGenerator generator = new RandomGenerator();
		int[] xLocations = { 300, 700, 1000 };
		
		int count = 0;
		for (int i = 0; i < xLocations.length; i++)
		{
			int topHeight = generator.nextInt(MIN_PIPE_HEIGHT, MAX_PIPE_HEIGHT);
			//top
			addPipe(count, xLocations[i], 0, PIPE_WIDTH, topHeight);
			
			count++;
			//bottom
			addPipe(count, xLocations[i], topHeight + PIPE_GAP, PIPE_WIDTH, 
					APPLET_HEIGHT - (topHeight + PIPE_GAP + DIRT_HEIGHT + GRASS_HEIGHT));
			
			count++;
		}
	}
	
	public void addPipe(int index, int x, int y, int width, int height)
	{
		pipes[index] = new GRect(x, y, width, height);
		pipes[index].setFilled(true);
		pipes[index].setFillColor(Color.GREEN);
		add(pipes[index]);
	}
	
	public void keyPressed(KeyEvent event)
	{
		int keyCode = event.getKeyCode();
		
		if (keyCode == KeyEvent.VK_UP)
		{
			//move the bird up
			birdVelocity = -4.0;
		}
	}
}
