public class Sort {
    /** Sort and print WORDS lexicographically. */
    public static void main(String[] words) {
        sort(words, 0, words.length - 1); // selection sort
        print(words);
    }

    /** Sort items A[L..U], with all others unchanged. */
    static void sort(String[] A, int L, int U) {
        while (L < U) {
            int k = indexOfLargest(A, L, U);
            String tmp = A[k]; A[k] = A[U]; A[U] = tmp;
            U -= 1;
        }
    }

    /**
     * Index k, I0<=k<=I1, such that V[k] is largest element
     * among V[I0], ... V[I1]. Require I0<=I1.
     */
    static int indexOfLargest(String[] V, int i0, int i1) {
        int i, k;
        k = i1;

        for (i = i1- 1; i >= i0; i -= 1) {
            k = (V[i].compareTo(V[k]) > 0) ? i : k;
        }

        return k;
    }

    /** Print A on one line, separated by blanks. */
    static void print(String[] A) {
        for (String s : A) {
            System.out.print(s + " ");
        }

        System.out.println();
    }
}