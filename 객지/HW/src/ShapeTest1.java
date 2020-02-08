// HW5 
// 학번 : 20191662
// 이름 : 정민지 

public class ShapeTest1 {
	public static void main(String [] args) {
		
		// Point 객체 생성
		Point p1 = new Point();	
		
		System.out.println("p1 --> " + p1);
		System.out.println("p1.x = " + p1.getX());
		System.out.println("p1.y = " +p1.getY());
		p1.setX(10);
		p1.setY(30);
		
		
		Point p2 = new Point(12, 44);

		p2.setX(50);
		p2.setY(10);

		System.out.println("p2 --> " + p2);
		
		Point p3;
		p3 = p1;	// 같은 object를 참조 ; shadow copy와 유사
		System.out.println("p3 --> " + p3);
		
		// Square 객체 생성 
		Square square1 = new Square(10 ,p1);
		Point p4 = square1.getPosition();	// p4가 square1의 Position 즉, p1을 참조한다.(참조!!!!!)

		p1.setX(100);
		System.out.println("p4: " + p4);
		square1.setFacet(4);
		square1.setPosition(new Point(40, 50));
		System.out.println("square1's area = " + square1.getArea());
		System.out.println("square1 -> " + square1);
		
		Square square2 = new Square(p2);
		square2.setFacet(100);
		System.out.println("square2 -> " + square2);
		System.out.println("square2's area = " +square2.getArea());
		
		Square square3 = new Square();	// Point 객체 생성 
		
		System.out.println("square3.position = " + square3.getPosition());
		System.out.println("square3.facet = " + square3.getFacet());
		System.out.println("square3 -> " + square3);
		
		
		// Circle 객체 생성 
		Circle circle1 = new Circle(p2, 100);
		circle1.setCenter(p1);
		circle1.setRadius(10);
		
		System.out.println("circle1.center = " + circle1.getCenter());
		System.out.println("circle1.radius = " + circle1.getRadius());
		System.out.println("circle1'area = " + circle1.getArea());
		System.out.println("circle1 -> " + circle1);
		
		Circle circle2 = new Circle();	//Point 객체 생성 
		System.out.println("circle2.center = " + circle2.getCenter());
		System.out.println("circle2.radius = " + circle2.getRadius());
		System.out.println("circle2 -> " + circle2);
		
		Circle circle3 = new Circle(p3);
		System.out.println("circle3.radius = " + circle3.getRadius());
		System.out.println("circle3'area = " + circle3.getArea());
		System.out.println("circle3 -> " + circle3);
		
		
		// Rectangle 객체 생성
		Rectangle rectangle1 = new Rectangle(p1, 40, 50);
		System.out.println("rectangle1'area = " + rectangle1.getArea());
		System.out.println("rectangle1 -> " + rectangle1);
	
		Rectangle rectangle2 = new Rectangle();		// Point 객체 생성 
		System.out.println("rectangle2.position = " + rectangle1.getPosition());
		System.out.println("rectangle2.height = " + rectangle1.getHeight());
		System.out.println("rectangle2.width = " + rectangle1.getWidth());
		System.out.println("rectangle2 -> " + rectangle2);
		
		Rectangle rectangle3 = new Rectangle(20, 80);	// Point 객체 생성 
		System.out.println("rectangle3.position = " + rectangle3.getPosition());
		rectangle3.setHeight(10);
		System.out.println("rectangle3 -> " + rectangle3);
		
		
		System.out.println("\n\nThe total number of points = " + Point.getTotalNumberPoints());
		System.out.println("\n\nThe total number of rectangles = " + Rectangle.getTotalNumberRectangles());
		
		
		
		
	}

}
