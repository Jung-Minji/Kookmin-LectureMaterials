// HW1 : 입력과 출력
// 학번   : 20191662
// 이름   : 정민지

import java.util.Scanner;
public class HW1 {

	public static void main(String[] args) {
		//1. 
		int id = 20191662;
		String name = "정민지";
		int age = 21;
		
		System.out.println("저는 " + name + "입니다." + " 저의 학번은 " + id + "이고 저의 나이는 "+ age + "입니다.");
		
		//2. 
		System.out.println("직사각형의 넓이 구하기");
		System.out.println("가로의 길이를 입력하세요");
		Scanner input = new Scanner(System.in);
		int a = input.nextInt();
		System.out.println("세로의 길이를 입력하세요");
		int b = input.nextInt();
		
		System.out.println("직사각형의 넓이는 " + a*b + "입니다.");

	}

}
