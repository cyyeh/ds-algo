/**
 * return true if there exists three integers(Integers may be used more than once.) in an array that sum to zero and false otherwise.
 */
public class ThreeSum {
    public static void main(String[] args) {

        int[] array01 = {-6, 2, 4};
        System.out.println(threeSum(array01));

        int[] array02 = {-6, 2, 5};
        System.out.println(threeSum(array02));

        int[] array03 = {-6, 3, 10, 200};
        System.out.println(threeSum(array03));

        int[] array04 = {8, 2, -1, 15};
        System.out.println(threeSum(array04));
        
        int[] array05 = {8, 2, -1, -1, 15};
        System.out.println(threeSum(array05));
        
        int[] array06 = {5, 1, 0, 3, 6};
        System.out.println(threeSum(array06));
    }

    private static boolean threeSum(int[] array) {
        if (array.length < 3)
            return false;

        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length; j++) {
                for (int k = 0; k < array.length; k++) {
                    if (array[i] + array[j] + array[k] == 0)
                        return true;
                }
            }
        }

        return false;
    }
}