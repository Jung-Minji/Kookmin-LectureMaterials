
public abstract class Shape implements AreaInterface{
	private Point position;
	
	public Shape() {
		this(new Point(10,10));
	}
	
	public Shape(Point position) {
		this.position = position;
	}

	public Point getPosition() {
		return position;
	}

	public void setPosition(Point position) {
		this.position = position;
	}

	public abstract double getArea();
	
	
	@Override
	public String toString() {
		return "Shape [position=" + position + "]";
	}
	
	
	
	

}
