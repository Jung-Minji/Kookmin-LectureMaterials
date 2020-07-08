// 학번 : 20191662
// 이름 : 정민지 
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
		System.out.println("원의 중심과 반지름 입력>>");
		double x = input.nextDouble();
		double y = input.nextDouble();
		double r = input.nextDouble();
		
		System.out.println("점 입력>>");
		double inputX = input.nextDouble();
		double inputY = input.nextDouble();
		
		boolean answer = isIntheCircle(x, y, r, inputX, inputY);
		if (answer == true) {
			System.out.println("점 (" + inputX + ',' + inputY + ")는 원 안에 있다.");
				
			
		}else {
			System.out.println("점 (" + inputX + ',' + inputY + ")는 원 밖에 있다.");
		}
		

	

		
	}

}
