// HW2-2 : �� ��ȯ ���α׷�
// �й�	 : 20191662
// �̸�	 : ������

import java.util.Scanner;
public class ReturnMoney {
	public static void main(String [] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("�ݾ��� �Է��ϼ���>>");
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
		
		System.out.println("�������� " + fiftyThousand + "��" );
		System.out.println("������ " + tenThousand + "��" );
		System.out.println("õ���� " + thousand + "��" );
		System.out.println("��� " + hundred + "��" );
		System.out.println("���ʿ� " + fifty + "��" );
		System.out.println("�ʿ� " + ten + "��" );
		System.out.println("�Ͽ� " + one + "��" );

    }
}
