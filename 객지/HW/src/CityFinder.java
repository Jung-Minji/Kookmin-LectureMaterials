// HW2-1: if���� ����ϱ�
// �й�     : 20191662
// �̸�     : ������ 

import java.util.Scanner;
public class CityFinder {
	
	public static String searchLocation(int n) {
		String area = null;
		if (n < 200)
			area = "����";
		else if (n < 300)
			area = "�λ�";
		else if (n < 400)
			area = "����";
		else if (n < 500)
			area = "����";
		else if (n < 600)
			area = "����";
		else if (n < 700)
			area = "����";
		else
			area = "����";
		return area;
	}
		

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("ã�� ������ �������� �Է��ϼ���: ");
		int num = input.nextInt();
		
		System.out.println("�Է��� ���� " + num + "�Դϴ�.");
		System.out.println(searchLocation(num));
		
	}

}
