// HW2-2 : 돈 반환 프로그램
// 학번	 : 20191662
// 이름	 : 정민지

import java.util.Scanner;
public class ReturnMoney {
	public static void main(String [] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("금액을 입력하세요>>");
		int money = input.nextInt();
		
		int fiftyThousand = 0;
		int tenThousand = 0;
		int thousand = 0;
		int hundred = 0;
		int fifty = 0;
		int ten = 0;
		int one = 0;		
		
		while (money > 0) {
			if (money >= 50000) {
				money -= 50000;
				fiftyThousand += 1;
			}
			else if (money >= 10000) {
				money -= 10000;
				tenThousand += 1;
			}
			else if (money >= 1000) {
				money -= 1000;
				thousand += 1;
			}
			else if (money >= 100) {
				money -= 100;
				hundred += 1;
			}
			else if (money >= 50) {
				money -= 50;
				fifty += 1;
			}
			else if (money >= 10) {
				money -= 10;
				ten += 1;
			}
			else if (money >= 1) {
				money -= 1;
				one += 1;
			}
		}
		
		System.out.println("오만원권 " + fiftyThousand + "매" );
		System.out.println("만원권 " + tenThousand + "매" );
		System.out.println("천원권 " + thousand + "매" );
		System.out.println("백원 " + hundred + "개" );
		System.out.println("오십원 " + fifty + "개" );
		System.out.println("십원 " + ten + "개" );
		System.out.println("일원 " + one + "개" );

    }
}
