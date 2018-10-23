/**
 * return true if there exists three integers(Integers can only be used once.) 
 * in an array that sum to zero and false otherwise.
 */
public class ThreeSumDistinct {
    public static void main(String[] args) {

        int[] array01 = {-6, 2, 4};
        System.out.println(threeSumDistinct(array01));

        int[] array02 = {-6, 2, 5};
        System.out.println(threeSumDistinct(array02));

        int[] array03 = {-6, 3, 10, 200};
        System.out.println(threeSumDistinct(array03));

        int[] array04 = {8, 2, -1, 15};
        System.out.println(threeSumDistinct(array04));
        
        int[] array05 = {8, 2, -1, -1, 15};
        System.out.println(threeSumDistinct(array05));
        
        int[] array06 = {5, 1, 0, 3, 6};
        System.out.println(threeSumDistinct(array06));
    }

    private static boolean threeSumDistinct(int[] array) {
        if (array.length < 3)
            return false;

        for (int i = 0; i < array.length; i++) {
            for (int j = 1; j < array.length; j++) {
                for (int k = 2; k < array.length; k++) {
                    if (i == j || i == k || j == k) {
                        continue;
                    }
                    else if (array[i] + array[j] + array[k] == 0) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}