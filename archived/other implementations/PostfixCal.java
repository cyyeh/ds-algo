import java.util.Stack;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class PostfixCal {
	public static void main(String[] args) {
		/**
		 * Read user input
		 */
		Scanner reader = new Scanner(System.in);
		System.out.println("Enter calculations as postfix: ");
		String calculation = reader.nextLine();
		System.out.println("Input: " + calculation);
		reader.close();
		
		Stack<String> postfixStack = new Stack<>();
		Set<String> operators = new HashSet<>(Arrays.asList("+", "-", "*", "/"));
		Boolean completeCalculation = true;
		
		for (int i = 0; i < calculation.length(); i++) {
			if (operators.contains(calculation.charAt(i) + "")) {
				double firstOperand, secondOperand, calculationResult;
				if (!postfixStack.empty()) {
					secondOperand = Double.parseDouble(postfixStack.pop());
				} else {
					completeCalculation = false;
					System.out.println("Illegal calculation");
					break;	
				}
				if (!postfixStack.empty()) {
					firstOperand = Double.parseDouble(postfixStack.pop());
				} else {
					completeCalculation = false;
					System.out.println("Illegal calculation");
					break;						
				}
				
				calculationResult = doMathCalculation(calculation.charAt(i) + "", firstOperand, secondOperand);
				postfixStack.push(calculationResult + "");
			} else {
				postfixStack.push(calculation.charAt(i) + "");
			}
		}
		
		if (completeCalculation == true && postfixStack.size() == 1)
			System.out.println("Calculation Result: " + postfixStack.pop());
		else
			System.out.println("Illegal calculation");
	}
	
	private static double doMathCalculation(String operator, double firstOperand, double secondOperand) {
		double result;
		
		if (operator.equals("*")) {
			result = firstOperand * secondOperand;
		} else if (operator.equals("/")) {
			result = firstOperand / secondOperand;
		} else if (operator.equals("+")) {
			result = firstOperand + secondOperand;
		} else {
			result = firstOperand - secondOperand;
		}
		
		return result;
	}
}
