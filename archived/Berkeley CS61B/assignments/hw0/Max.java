import java.util.Arrays;
import java.util.Random;

/**
 * Return the maximum value of an int array
 */
public class Max {
    public static void main(String[] args) {
        int[] array = generateRandomIntArray();

        System.out.println("Original Array: ");
        printArrayToScreen(array);

        int max = getMaxFromArray(array);
        System.out.println("Max element: " + max);

        System.out.println("Sorted Array: ");
        Arrays.sort(array);
        printArrayToScreen(array);        
    }

    private static int[] generateRandomIntArray() {
        Random rand = new Random();
        int[] array = new int[rand.nextInt(100) + 1];

        for (int i = 0; i < array.length; i++) {
            array[i] = rand.nextInt(array.length);
        }

        return array;
    }

    private static void printArrayToScreen(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    } 

    private static int getMaxFromArray(int[] array) {
        assert array.length > 1;

        int max = array[0];

        for (int i = 1; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }

        return max;
    }
}