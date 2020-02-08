// HW5 
// �й� : 20191662
// �̸� : ������ 

public class ShapeTest1 {
	public static void main(String [] args) {
		
		// Point ��ü ����
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
		p3 = p1;	// ���� object�� ���� ; shadow copy�� ����
		System.out.println("p3 --> " + p3);
		
		// Square ��ü ���� 
		Square square1 = new Square(10 ,p1);
		Point p4 = square1.getPosition();	// p4�� square1�� Position ��, p1�� �����Ѵ�.(����!!!!!)

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
		
		Square square3 = new Square();	// Point ��ü ���� 
		
		System.out.println("square3.position = " + square3.getPosition());
		System.out.println("square3.facet = " + square3.getFacet());
		System.out.println("square3 -> " + square3);
		
		
		// Circle ��ü ���� 
		Circle circle1 = new Circle(p2, 100);
		circle1.setCenter(p1);
		circle1.setRadius(10);
		
		System.out.println("circle1.center = " + circle1.getCenter());
		System.out.println("circle1.radius = " + circle1.getRadius());
		System.out.println("circle1'area = " + circle1.getArea());
		System.out.println("circle1 -> " + circle1);
		
		Circle circle2 = new Circle();	//Point ��ü ���� 
		System.out.println("circle2.center = " + circle2.getCenter());
		System.out.println("circle2.radius = " + circle2.getRadius());
		System.out.println("circle2 -> " + circle2);
		
		Circle circle3 = new Circle(p3);
		System.out.println("circle3.radius = " + circle3.getRadius());
		System.out.println("circle3'area = " + circle3.getArea());
		System.out.println("circle3 -> " + circle3);
		
		
		// Rectangle ��ü ����
		Rectangle rectangle1 = new Rectangle(p1, 40, 50);
		System.out.println("rectangle1'area = " + rectangle1.getArea());
		System.out.println("rectangle1 -> " + rectangle1);
	
		Rectangle rectangle2 = new Rectangle();		// Point ��ü ���� 
		System.out.println("rectangle2.position = " + rectangle1.getPosition());
		System.out.println("rectangle2.height = " + rectangle1.getHeight());
		System.out.println("rectangle2.width = " + rectangle1.getWidth());
		System.out.println("rectangle2 -> " + rectangle2);
		
		Rectangle rectangle3 = new Rectangle(20, 80);	// Point ��ü ���� 
		System.out.println("rectangle3.position = " + rectangle3.getPosition());
		rectangle3.setHeight(10);
		System.out.println("rectangle3 -> " + rectangle3);
		
		
		System.out.println("\n\nThe total number of points = " + Point.getTotalNumberPoints());
		System.out.println("\n\nThe total number of rectangles = " + Rectangle.getTotalNumberRectangles());
		
		
		
		
	}

}
