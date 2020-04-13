public class Shove {
    /**
     * Rotate elements A[k] to A[A.length-1] one element to the right, where k is
     * the smallest index such that elements k through A.length-2 are all larger
     * than A[A.length-1].
     */
    private static void moveOver(int[] A) {
        int k = 0;
        int lastIndex = A.length - 1;
        int lastElement = A[lastIndex];

        for (int i = 0; i <= lastIndex; i++) {
            if (lastElement >= A[k]) {
                k += 1;
            }
        }

        if (k != lastIndex) {
            rotateRightByOne(A, k);
        }
    }

    private static void rotateRightByOne(int[] A, int k) {
        int lastElement = A[A.length - 1];

        for (int i = A.length - 2; i >= k; i--) {
            A[i + 1] = A[i];
        }

        A[k] = lastElement;
    }

    public static void main(String[] args) {
        int[] arrayA = { 1, 9, 4, 3, 0, 12, 11, 9, 15, 22, 12 };
        int[] arrayB = { 1, 9, 4, 3, 0, 12, 11, 9, 15, 22, -2 };

        moveOver(arrayA);
        moveOver(arrayB);

        print(arrayA);
        print(arrayB);
    }

    /** Print A on one line, separated by blanks. */
    private static void print(int[] A) {
        for (Integer s : A) {
            System.out.print(s + " ");
        }

        System.out.println();
    }    
}