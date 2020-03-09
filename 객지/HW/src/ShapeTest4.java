// HW7 : abstract class
// 학번 : 20191662
// 이름 : 정민지 
public class ShapeTest4 {

	public static void main(String[] args) {
		
		// Point 객체 배열 
		Point [] myPointList = new Point[10];
		
		for (int i=0 ; i<myPointList.length; i++) {
			myPointList[i] = new Point(i, i*20);
			System.out.println(myPointList[i]);
		}
		
		// Circle 객체 배열
		Circle [] myCircleList = new Circle[10];

		for (int i=0 ; i<myCircleList.length  && i < myPointList.length; i++) {
			myCircleList[i] = new Circle(myPointList[i], i+10 );
			System.out.println(myCircleList[i]);
		}
		
		// Square 객체 배열 
		Square [] mySquareList = new Square[10];

		for (int i=0 ; i<mySquareList.length  && i < myPointList.length; i++) {
			mySquareList[i] = new Square((i+1)*20, myPointList[i]);
			System.out.println(mySquareList[i]);
		}
		
		// Rectangle 객체 배열
		Rectangle [] myRectangleList = new Rectangle[10];

		
		for (int i=0 ; i<myRectangleList.length  && i < myPointList.length; i++) {
			myRectangleList[i] = new Rectangle(myPointList[i], i+1, (i+1)*20);
			System.out.println(myRectangleList[i]);
		}
		
		



	}

}
