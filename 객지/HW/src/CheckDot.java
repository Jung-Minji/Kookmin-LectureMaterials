// �й� : 20191662
// �̸� : ������ 
import java.util.Scanner;
public class CheckDot {
	
	public static boolean isIntheCircle(double centerX, double centerY, double r, double inputX, double inputY) {

		if (Math.sqrt((Math.pow(inputX - centerX, 2) + Math.pow(inputY - centerY, 2))) <= r){
			return true;
		}
		return false;
		
	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("���� �߽ɰ� ������ �Է�>>");
		double x = input.nextDouble();
		double y = input.nextDouble();
		double r = input.nextDouble();
		
		System.out.println("�� �Է�>>");
		double inputX = input.nextDouble();
		double inputY = input.nextDouble();
		
		boolean answer = isIntheCircle(x, y, r, inputX, inputY);
		if (answer == true) {
			System.out.println("�� (" + inputX + ',' + inputY + ")�� �� �ȿ� �ִ�.");
				
			
		}else {
			System.out.println("�� (" + inputX + ',' + inputY + ")�� �� �ۿ� �ִ�.");
		}
		

	

		
	}

}
