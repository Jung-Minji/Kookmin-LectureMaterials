// HW5 
// �й� : 20191662
// �̸� : ������ 

public class Point {
	
	//  attributes or field or instance variable; Ư�� 
	private int x;
	private int y;
	
	private static int totalNumberPoints = 0;
	
	// constructor ; ������
	// �ʱⰪ��  setting�� �� �ִ�.
	
	// * ������ : ��ü�� ������ �� �ҷ����� method
	// - class �̸��� �����ϴ�.
	// - �����ε� ���� ��� : ���� �̸��� method�� ������ ����(��, parameter�� �޶�� �Ѵ�)
	
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
		this(a,a);		// �Ķ���Ͱ� �� ���� �����ڸ� ȣ���Ѵ�.
	}
	
	public String toString() {
		return ("(x, y) = (" + x + ", " + y + ")");
	}
	
//	public void testString() {
//		System.out.println("ddd");
//	}
//	�ڹٿ��� return�� ���� �Լ��� System.out.println�ϸ� ������ �߻��Ѵ� --> None�� �ⷰ�Ǵ� ���̽�� �ٸ�!!
	
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
	
	//static attribute �ܺο��� �����ϴ� �޼���
	public static int getTotalNumberPoints() {
		return totalNumberPoints;
	}

	
}
