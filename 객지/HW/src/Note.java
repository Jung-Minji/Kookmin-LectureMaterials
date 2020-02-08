import java.util.*;
public class Note {
	public static void main(String[] args) {
		int[] a = new int[5];
		int[] b = new int[a.length];
		
		for(int i=0; i<a.length; i++) {
			a[i] = i+1;
		}
		for(int i:a)
			System.out.println(i);
		
		for(int i=a.length-1; i>=0; i--) {
			b[a.length-1-i] = a[i];
		}
		
		for(int i:b)
			System.out.println(i);
	
		
		
		
		
	}
}
        
        		    



