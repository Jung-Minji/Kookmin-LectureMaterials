// HW5 
// 학번 : 20191662
// 이름 : 정민지 

public class Rectangle extends Shape{
	private float height;
	private float width;
	
	private static int totalNumberRectangles = 0;
	
	public Rectangle() {
		super();
		height = 1;
		width = 1;	
		totalNumberRectangles += 1;
	}
	
	public Rectangle(Point position, float height, float width) {
		super(position);
		this.height = height;
		this.width = width;
		totalNumberRectangles += 1;

	}
	
	public Rectangle(float height, float width) {
		this(new Point(0,0), height, width);
	}
	
	public Point getPosition() {
		return super.getPosition();
	}
	
	public float getHeight() {
		return height;
	}
	
	public float getWidth() {
		return width;
	}
	
	public void setPosition(Point position) {
		super.setPosition(position);;
	}
	
	public void setHeight(float height) {
		this.height = height;
	}
	
	public void setWidth(float width) {
		this.width = width;
	}
	
	public String toString() {
		return ("at point : " + super.toString() 
				+ " with height = " + height + ", width = " + width);
	}
	
	public double getArea() {
		return height * width;
	}
	
	public static int getTotalNumberRectangles() {
		return totalNumberRectangles;
	}

}
