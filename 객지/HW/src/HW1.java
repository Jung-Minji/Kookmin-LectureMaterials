// HW1 : �Է°� ���
// �й�   : 20191662
// �̸�   : ������

import java.util.Scanner;
public class HW1 {

	public static void main(String[] args) {
		//1. 
		int id = 20191662;
		String name = "������";
		int age = 21;
		
		System.out.println("���� " + name + "�Դϴ�." + " ���� �й��� " + id + "�̰� ���� ���̴� "+ age + "�Դϴ�.");
		
		//2. 
		System.out.println("���簢���� ���� ���ϱ�");
		System.out.println("������ ���̸� �Է��ϼ���");
		Scanner input = new Scanner(System.in);
		int a = input.nextInt();
		System.out.println("������ ���̸� �Է��ϼ���");
		int b = input.nextInt();
		
		System.out.println("���簢���� ���̴� " + a*b + "�Դϴ�.");

	}

}
