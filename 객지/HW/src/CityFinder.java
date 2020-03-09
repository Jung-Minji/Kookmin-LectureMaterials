// HW2-1: if문장 사용하기
// 학번     : 20191662
// 이름     : 정민지 

import java.util.Scanner;
public class CityFinder {
	
	public static String searchLocation(int n) {
		String area = null;
		if (n < 200)
			area = "서울";
		else if (n < 300)
			area = "부산";
		else if (n < 400)
			area = "대전";
		else if (n < 500)
			area = "광주";
		else if (n < 600)
			area = "강릉";
		else if (n < 700)
			area = "제주";
		else
			area = "미정";
		return area;
	}
		

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("찾을 도시의 정수값을 입력하세요: ");
		int num = input.nextInt();
		
		System.out.println("입력한 수는 " + num + "입니다.");
		System.out.println(searchLocation(num));
		
	}

}
