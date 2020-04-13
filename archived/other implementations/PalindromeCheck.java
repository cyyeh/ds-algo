import java.util.Stack;
import java.util.Scanner;

public class PalindromeCheck {
	public static void main(String[] args) {
		/**
		 * Read user input
		 */
		Scanner reader = new Scanner(System.in);
		System.out.println("Enter a string: ");
		String inputString = reader.nextLine();
		reader.close();
		
		Stack<String> stringStack = new Stack<>();
		String poppedString = "";
		
		if (inputString.length() > 0) {
			for (int i = 0; i < inputString.length(); i++) {
				stringStack.push("" + inputString.charAt(i));
			}
			
			while (!stringStack.empty()) {
				poppedString += stringStack.pop();
			}
			
			// check if input string is a palindrome
			if (poppedString.equals(inputString)) {
				System.out.println("Input string is a palindrome: " + inputString);
			} else {
				System.out.println("Input string isn't a palindrome: " + inputString);
			}	
		} else {
			System.out.println("Input string is empty");
		}
	}	
}
