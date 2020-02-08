// HW5 
// 학번 : 20191662
// 이름 : 정민지 

public class Point {
	
	//  attributes or field or instance variable; 특성 
	private int x;
	private int y;
	
	private static int totalNumberPoints = 0;
	
	// constructor ; 생성자
	// 초기값을  setting할 수 있다.
	
	// * 생성자 : 객체가 생성될 때 불려지는 method
	// - class 이름과 동일하다.
	// - 오버로딩 개념 사용 : 같은 이름의 method를 재정의 가능(단, parameter는 달라야 한다)
	
	public Point() {	/// default constructor -- no argument constructor
		x = 0;
		y = 0;
		totalNumberPoints += 1;

	}
	
	public Point(int x, int y) {	// full-argument constructor
		this.x = x;
		this.y = y;
		totalNumberPoints += 1;
	}
	
	public Point(int a) {		// partial-argument constructor
		this(a,a);		// 파라미터가 두 개인 생성자를 호출한다.
	}
	
	public String toString() {
		return ("(x, y) = (" + x + ", " + y + ")");
	}
	
//	public void testString() {
//		System.out.println("ddd");
//	}
//	자바에서 return이 없는 함수를 System.out.println하면 에러가 발생한다 --> None이 출럭되는 파이썬과 다름!!
	
	public int getX() {
		return x;
	}
	
	public int getY() {
		return y;
	}
	
	public void setX(int a) {
		x = a;
	}
	
	public void setY(int b) {
		y = b;
	}
	
	//static attribute 외부에서 접근하는 메서드
	public static int getTotalNumberPoints() {
		return totalNumberPoints;
	}

	
}
