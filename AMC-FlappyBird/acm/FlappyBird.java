import java.awt.Color;

import acm.graphics.*;

public class FlappyBird extends GCompound
{
	public void assemble()
	{
		//build the bird!
		buildBody();
		buildWing();
		buildEye();
		buildMouth();
	}
	
	private void buildMouth()
	{
		GRoundRect top = new GRoundRect(34, 20, 34, 6);
		top.setFillColor(new Color(255, 153, 51));
		top.setFilled(true);
		
		add(top);
		
		GRoundRect bottom = new GRoundRect(34, 26, 30, 6);
		bottom.setFillColor(new Color(255, 153, 51));
		bottom.setFilled(true);
		
		add(bottom);
	}
	
	private void buildEye()
	{
		GOval eye = new GOval(34, 2, 25, 32);
		eye.setFillColor(Color.WHITE);
		eye.setFilled(true);
		
		add(eye);
		
		GOval pupil = new GOval(50, 8, 4, 9);
		pupil.setFillColor(Color.BLACK);
		pupil.setFilled(true);
		
		add(pupil);
	}
	
	private void buildWing()
	{
		GOval wing = new GOval(0, 10, 30, 20);
		wing.setFillColor(Color.YELLOW);
		wing.setFilled(true);
		
		add(wing);
	}
	
	private void buildBody()
	{
		GOval body = new GOval(10, 0, 50, 40);
		body.setFillColor(Color.YELLOW);
		body.setFilled(true);
		
		add(body);
	}
}
