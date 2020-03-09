// HW5 
// �й� : 20191662
// �̸� : ������ 

public class Square extends Shape{
	private double facet;
	static private int totalNumberSquares = 0;
	
	public Square() {
		super();
		facet = 1;
		totalNumberSquares += 1;	
	}
	
	public Square(double facet, Point position) {
		super(position);
		this.facet = facet;
		totalNumberSquares += 1;
		
	}
	
	public Square(Point pos) {
		this(1.0, pos);		// �Ķ���Ͱ� 2���� ���� �����ڸ� ȣ���Ѵ�.
	}

	public double getFacet() {
		return facet;
	}

	public void setFacet(double facet) {
		this.facet = facet;
	}

	public Point getPosition() {
		return super.getPosition();
	}

	public void setPosition(Point position) {
		super.setPosition(position);;
	}
	
	public String toString() {
		return ("at point : " + super.toString() + " with facet " + facet); 
	}
	
	public double getArea() {
		return (facet * facet);
	}
	
	public static int getTotalNumberSquares() {
		return totalNumberSquares;
	}

}
