// HW5 
// 학번 : 20191662
// 이름 : 정민지 

public class Circle extends Shape{
	private float radius;
	private static int totalNumberCircles = 0;	// 초기값을 주는 것이 좋다.
	
	public Circle() {
		super();
		radius = 1;
		totalNumberCircles += 1;
	}
	
	public Circle(Point center, float radius) {
		super(center);
		this.radius = radius;
		totalNumberCircles += 1;

	}
	
	public Circle(Point center) {
		this(center, 1);
	}
	
	public Point getCenter() {
		return super.getPosition();
	}
	
	public float getRadius() {
		return radius;
	}
	
	public void setCenter(Point center) {
		super.setPosition(center);
	}
	
	public void setRadius(float radius) {
		this.radius = radius;
	}
	
	public String toString() {
		return ("at center : " + super.toString() + " with radius " + radius);
	}
	
	public double getArea() {
		return 3.14 * radius * radius;
	}
	
	public static int getTotalNumberCircles() {
		return totalNumberCircles;
	}
}
