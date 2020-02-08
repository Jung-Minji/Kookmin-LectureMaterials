// HW6
// �й� : 20191662
// �̸� : ������ 

import java.util.Scanner;
public class ShapeTest2 {
	public static void main (String [] args) {
		
		final int NUMBER_OF_POINTS;
		final int NUMBER_OF_RECTANGLES;
		final int NUMBER_OF_PLACES;
		
		if (args.length > 0){
			NUMBER_OF_POINTS = Integer.parseInt(args[0]);
		}
		else {
			NUMBER_OF_POINTS = 10;
		}
		
		
		// Point �迭 ���� 
		Point [] myPointList = new Point[NUMBER_OF_POINTS];
		
		for (int i=0 ; i<myPointList.length; i++) {
			myPointList[i] = new Point(i, i*20);
			System.out.println(myPointList[i]);
		}
		
		// Point �� ��������
		for (int i=0 ; i<myPointList.length ; i++) {
			System.out.println("myPointList["+ i+ "].getX = "+ myPointList[i].getX());
		}
		
		// Point �� �ٲٱ�
		for (int i=0 ; i<myPointList.length ; i++) {
			myPointList[i].setX(i+2);
		}
		
		System.out.println("after change myPointList's x");
		for (int i=0 ; i<myPointList.length; i++) {
			System.out.println(myPointList[i]);
		}
		
		System.out.println("The number of Points " + Point.getTotalNumberPoints());
		
	
		// Rectangle �迭 ���� 
		Scanner input = new Scanner(System.in);
		System.out.println("rectangle�迭�� ���̸� �Է��ϼ���: ");
		NUMBER_OF_RECTANGLES = input.nextInt();
		
		Rectangle [] myRectangleList = new Rectangle[NUMBER_OF_RECTANGLES];

		
		for (int i=0 ; i<myRectangleList.length  && i < myPointList.length; i++) {
			myRectangleList[i] = new Rectangle(myPointList[i], i+1, (i+1)*20);
			System.out.println(myRectangleList[i]);
		}
		
		//Rectangle�� Height�� ��������
		
		for (int i=0 ; i<myRectangleList.length ; i++) {
			System.out.println("myRectangleList["+ i+ "].getHeight = "+ myRectangleList[i].getHeight());
		}
		
		//Rectangle�� Height�� �ٲٱ� & ���� ���ϱ� 
		for (int i=0 ; i<myRectangleList.length ; i++) {
			 myRectangleList[i].setHeight(i+10);
		}
		System.out.println("after change myRectanglelist's Height");
		
		for (int i=0 ; i<myRectangleList.length; i++) {
			System.out.println(myRectangleList[i]);
			System.out.println("myRectanglelist["+ i+ "]'s Area: " + myRectangleList[i].getArea());

		}
		System.out.println("The number of Rectangles " + Rectangle.getTotalNumberRectangles());

		
		// Square �迭 ���� 
		Square [] mySquareList = new Square[NUMBER_OF_POINTS];

		for (int i=0 ; i<mySquareList.length  && i < myPointList.length; i++) {
			mySquareList[i] = new Square((i+1)*20, myPointList[i]);
			System.out.println(mySquareList[i]);
		}
		
		// Square�� facet�� ��������
		for (int i=0 ; i<mySquareList.length ; i++) {
			System.out.println("mySquareList["+ i+ "].getFacet = "+ mySquareList[i].getFacet());
		}
		
		// Square�� facet�� �ٲٱ� & ���� ���ϱ�
		for (int i=0 ; i<mySquareList.length ; i++) {
			mySquareList[i].setFacet(i*2);
		}
		
		System.out.println("after change mySquareList's facet");
		for (int i=0 ; i<mySquareList.length ; i++) {
			System.out.println(mySquareList[i]);
			System.out.println("mySquareList["+ i+ "]'s Area: " + mySquareList[i].getArea());

			
		}
		System.out.println("The number of Squares " + Square.getTotalNumberSquares());

		
		// Circle �迭 ����
		Circle [] myCircleList = new Circle[NUMBER_OF_POINTS];

		for (int i=0 ; i<myCircleList.length  && i < myPointList.length; i++) {
			myCircleList[i] = new Circle(myPointList[i], i+10 );
			System.out.println(myCircleList[i]);
		}
		
		// Circle�� radius�� ��������
		for (int i=0 ; i<myCircleList.length; i++) {
			System.out.println("myCircleList["+ i+ "].getRadius = "+ myCircleList[i].getRadius());
		}
		
		// Circle�� radius�� �ٲٱ� & ���� ���ϱ�
		for (int i=0 ; i<myCircleList.length; i++) {
			myCircleList[i].setRadius(i*3);
		}
		System.out.println("after change myCircleList's radius");

		for (int i=0 ; i<myCircleList.length; i++) {
			System.out.println(myCircleList[i]);
			System.out.println("myCircleList["+ i+ "]'s Area: " + myCircleList[i].getArea());
		}
	
		System.out.println("The number of Circles " + Circle.getTotalNumberCircles());
		
		// Shape type�� �迭 �����
		Shape [] myShapeList = new Shape[3];
		myShapeList[0] = new Circle();
		myShapeList[1] = new Rectangle();
		myShapeList[2] = new Square();
		
		System.out.println("myShapeList[0] = " + myShapeList[0].toString());
		System.out.println("myShapeList[0]'s area = " + myShapeList[0].getArea());

		System.out.println("myShapeList[1]" + myShapeList[1].toString());
		System.out.println("myShapeList[1]'s area = " + myShapeList[1].getArea());
		

		System.out.println("myShapeList[2] = " + myShapeList[2].toString());
		System.out.println("myShapeList[2]'area = " + myShapeList[2].getArea());
		
		
		// interface
		System.out.println("Enter the number of places to consider: ");
		NUMBER_OF_PLACES = input.nextInt();
		AreaInterface [] placeList = new AreaInterface [NUMBER_OF_PLACES];
		
		for (int i=0 ; i<placeList.length; i++) {
			if (i % 3 == 0) {
				placeList[i] = new Circle();
			}
			else if (i % 3 == 1) {
				placeList[i] = new Rectangle();
			}
			else {
				placeList[i] = new House();
			}
			
			System.out.println(placeList[i]);
			System.out.println(placeList[i].getArea());
		}
		
		
	}

}
