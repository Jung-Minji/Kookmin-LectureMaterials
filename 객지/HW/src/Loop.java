// HW 3-1 Loop
// �й�: 20191662
// �̸� : ������ 

import java.util.Scanner;
public class Loop {
	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);
	int [] arr = new int [10]; 
	
	// ���� ���� 10���� �Է¹޾� �迭�� �����ϰ�, 3�� ����� ����ϱ� 
	for (int i=0 ; i<10; i++) {
		System.out.println("�迭�� ������ ���� ������ �Է��ϼ���: ");
		int num = input.nextInt();
		while (num < 0) {
			System.out.println("���� ������ �ƴմϴ�. �ٽ� �Է��ϼ���!: ");
			num = input.nextInt();
		}
		arr[i] = num;
	}
	
	for (int i=0 ; i<arr.length ; i++) {
		if (arr[i] % 3 == 0) {
			System.out.println(arr[i]);
		}
	}
	
	// ����ڿ��� �˰� ���� ��� ���� �Է� ���� �� �迭���� �� ����� ����ϱ� 
	System.out.println("�迭���� ����ϰ� ���� ����� ���� �Է��ϼ���: ");
	int multiple = input.nextInt();
	
	for (int i=0 ; i<arr.length ; i++) {
		if (arr[i] % multiple == 0) {
			System.out.println(arr[i]);
		}
	}
	
	
	}

}
