import java.util.Stack;
import java.util.Scanner;

public class BalancedParetheses {
	public static void main(String[] args) {
		/**
		 * Read user input
		 */
		Scanner reader = new Scanner(System.in);
		System.out.println("Enter parentheses: ");
		String parentheses = reader.nextLine();
		reader.close();
		
		Stack<String> parehthesesStack = new Stack<>();
		Boolean balanced = true;
		
		System.out.println("Input: " + parentheses);
		
		for (int i = 0; i < parentheses.length(); i++) {
			if (parentheses.charAt(i) == '(') {
				parehthesesStack.push("(");
			} else {
				if (parehthesesStack.empty()) {
					balanced = false;
					break;
				} else {
					parehthesesStack.pop();
				}
			}
		}
		
		if (balanced && parehthesesStack.empty()) {
			System.out.println("Balanced parentheses!");
		} else {
			System.out.println("Not balanced parentheses!");
		}
	}
}
