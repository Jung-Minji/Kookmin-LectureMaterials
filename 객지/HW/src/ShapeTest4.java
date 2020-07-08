// HW7 : abstract class
// �й� : 20191662
// �̸� : ������ 
public class ShapeTest4 {

	public static void main(String[] args) {
		
		// Point ��ü �迭 
		Point [] myPointList = new Point[10];
		
		for (int i=0 ; i<myPointList.length; i++) {
			myPointList[i] = new Point(i, i*20);
			System.out.println(myPointList[i]);
		}
		
		// Circle ��ü �迭
		Circle [] myCircleList = new Circle[10];

		for (int i=0 ; i<myCircleList.length  && i < myPointList.length; i++) {
			myCircleList[i] = new Circle(myPointList[i], i+10 );
			System.out.println(myCircleList[i]);
		}
		
		// Square ��ü �迭 
		Square [] mySquareList = new Square[10];

		for (int i=0 ; i<mySquareList.length  && i < myPointList.length; i++) {
			mySquareList[i] = new Square((i+1)*20, myPointList[i]);
			System.out.println(mySquareList[i]);
		}
		
		// Rectangle ��ü �迭
		Rectangle [] myRectangleList = new Rectangle[10];

		
		for (int i=0 ; i<myRectangleList.length  && i < myPointList.length; i++) {
			myRectangleList[i] = new Rectangle(myPointList[i], i+1, (i+1)*20);
			System.out.println(myRectangleList[i]);
		}
		
		



	}

}
