public class Primes {
    /**
     * Print all primes up to ARGS[0] (interpreted as an integer), 10 to a line.
     */
    public static void main(String[] args) {
        printPrimes(Integer.parseInt(args[0]));
    }

    /**
     * Print all primes up to and including LIMIT, 10 to a line.
     */
    private static void printPrimes(int limit) {
        /**
         * { For every integer x, between 2 and LIMIT, print it if isPrime(x), 10 to a line. }
         */
        int numberOfPrime = 0;

        for (int p = 0; p <= limit; p++) {
            if (isPrime(p)) {
                System.out.print(p + " ");
                numberOfPrime += 1;
                if (numberOfPrime % 10 == 0)
                    System.out.println();
            }
        }
        
        if (numberOfPrime % 10 != 0)
            System.out.println();
    }

    /**
     * True iff X is a prime
     */
    private static boolean isPrime(int x) {
        if (x <= 1)
            return false;
        else
            return !isDivisible(x, 2);
    }

    /**
     * True iff X is divisible by some number >= K and < X, given that K > 1,
     * and that X is not divisible by any number >1 and <K.
     */
    private static boolean isDivisible(int x, int k) {
        int limit = (int) Math.round(Math.sqrt(x));

        for (int k1 = k; k1 <= limit; k1++) {
            if (x % k1 == 0)
                return true;
        }

        return false;
    }
}