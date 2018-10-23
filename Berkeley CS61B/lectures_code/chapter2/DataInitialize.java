public class DataInitialize {
    public static void main(String[] args) {
        int integerANotInitialized;
        double doubleBNotInitialized;
        int[] integerArray = new int[10];
        Integer[] integerArrayNotInitialized = new Integer[10];
        Double[] doubleArrayNotInitialized = new Double[10];
        
        int[] integerArray2 = {1, 2, 3, 4, 5};
        int[] integerArray3;
        integerArray3 = new int[]{1, 2, 3 ,4, 5, 6}; // error if only {1, 2, 3, 4, 5, 6} 

        //System.out.println(integerANotInitialized);  // error
        //System.out.println(doubleBNotInitialized);  // error
        printIntegerArrayElements(integerArray);    // all 0
        printIntegerArrayElements(integerArray2);   // 1 2 3 4 5
        printIntegerArrayElements(integerArray3);   // 1 2 3 4 5 6
        printArrayElements(integerArrayNotInitialized); // all null
        printArrayElements(doubleArrayNotInitialized);  // all null
    }

    // generic method
    private static < T > void printArrayElements(T[] array) {
        for (T element : array) {
            System.out.print(element + " ");
        }
        System.out.println();
    }

    private static void printIntegerArrayElements(int[] array) {
        for (int element : array) {
            System.out.print(element + " ");
        }
        System.out.println();
    }
}