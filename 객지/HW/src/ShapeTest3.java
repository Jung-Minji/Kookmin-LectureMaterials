
public class ShapeTest3 {

	public static void main(String[] args) {
		Circle c1 = new Circle();
		System.out.println(c1);	// Circle class¿« toString()
		
		Shape s = c1;	// upcasting
		System.out.println(s);
		//System.out.println(s.getPosition());	
		
		//System.out.println(s.getRadius());	// error!
		
		System.out.println(s.getArea());
	}

}
