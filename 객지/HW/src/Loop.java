// HW 3-1 Loop
// 학번: 20191662
// 이름 : 정민지 

import java.util.Scanner;
public class Loop {
	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);
	int [] arr = new int [10]; 
	
	// 양의 정수 10개를 입력받아 배열에 저장하고, 3의 배수만 출력하기 
	for (int i=0 ; i<10; i++) {
		System.out.println("배열에 저장할 양의 정수를 입력하세요: ");
		int num = input.nextInt();
		while (num < 0) {
			System.out.println("양의 정수가 아닙니다. 다시 입력하세요!: ");
			num = input.nextInt();
		}
		arr[i] = num;
	}
	
	for (int i=0 ; i<arr.length ; i++) {
		if (arr[i] % 3 == 0) {
			System.out.println(arr[i]);
		}
	}
	
	// 사용자에게 알고 싵은 배수 값을 입력 받은 후 배열에서 그 배수를 출력하기 
	System.out.println("배열에서 출력하고 싶은 배수의 수를 입력하세요: ");
	int multiple = input.nextInt();
	
	for (int i=0 ; i<arr.length ; i++) {
		if (arr[i] % multiple == 0) {
			System.out.println(arr[i]);
		}
	}
	
	
	}

}
