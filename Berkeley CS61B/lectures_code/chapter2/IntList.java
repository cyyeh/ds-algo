public class IntList {
    // Constructor function (used to initialize new object)
    /** List cell containing (HEAD, TAIL). */
    public IntList(int head, IntList tail) {
        head = head; 
        tail = tail;
    }

    // Names of simple containers (fields
    // WARNING: public instance variables usually bad style!
    public int head;
    public IntList tail;

    IntList addFirst(int x) {
        return new IntList(x, this);
    }

    /**
     * return size of List in recursive way.
     */
    int sizeRecur() {
        if (tail == null) {
            return 1;
        } else {
            return 1 + tail.sizeRecur();
        }
    }

    /**
     * retur size of List in iterative way.
     */
    int sizeIter() {
        IntList tail = tail;
        int size = 1;

        while (tail != null) {
            size += 1;

            tail = tail.tail;
        }

        return size;
    }

    /**
     * return ith element of List in recursive way
     */
    int get(int i) {
        if (i == 0) {
            return head;
        } else {
            return tail.get(i - 1);
        }
    }

    /** 
     * Non-destructively add N to P's items in recursive way.
     */    
    static IntList incrListRecur(IntList P, int n) {
        if (P == null)
            return null;
        else
            return new IntList(P.head + n, incrListRecur(P.tail, n));
    }

    /** 
     * Non-destructively add N to P's items in iterative way.
     */
    static IntList incrListIter(IntList P, int n) {
        if (P == null)
            return null;
        IntList result, last;
        result = last = new IntList(P.head + n, null);

        while (P.tail != null) {
            P = P.tail;
            last.tail = new IntList(P.head + n, null);
            last = last.tail;
        }

        return result;
    }

    /**
     * Destructively add N to P's items in recursive way
     */
    static IntList dincrListRecur(IntList P, int n) {
        if (P == null)
            return null;
        else {
            P.head += n;
            P.tail = dincrListRecur(P.tail, n);
            return P;
        }
    }

    /**
     * Destructively add N to P's items in iterative way
     */
    static IntList dincrListIter(IntList P, int n) {
        // 'for' can do more than count!
        for (IntList p = P; p != null; p = p.tail)
            p.head += n;
        return P;
    }

    /**
     * The list resulting from removing all instances of X 
     * from non-destructively in recursive way
     */
    static IntList removeAllRecur(IntList L, int x) {
        if (L == null)
            return null;
        else if (L.head == x)
            return removeAllRecur(L.tail, x);
        else
            return new IntList(L.head, removeAllRecur(L.tail, x));
    }

    /**
     * The list resulting from removing all instances of X 
     * from non-destructively in iterative way
     */
    static IntList removeAllIter(IntList L, int x) {
        IntList result, last;
        result = last = null;

        for (; L != null; L = L.tail) {
            if (x == L.head)
                continue;
            else if (last == null)
                result = last = new IntList(L.head, null);
            else
                last = last.tail = new IntList(L.head, null);
        }

        return result;
    }

    /**
     * The list resulting from removing all instances of X
     * from L. The original list may be destroyed in
     * recursive way.
     */
    static IntList dremoveAllRecur(IntList L, int x) {
        if (L == null) {
            return null;
        } else if (L.head == x) {
            return dremoveAllRecur(L.tail, x);
        } else {
            L.tail = dremoveAllRecur(L.tail, x);
            return L;
        }
    }

    /**
     * The list resulting from removing all X's from L 
     * destructively in iterative way.
     */
    static IntList dremoveAllIter(IntList L, int x) {
        IntList result, last;
        result = last = null;
        
        while (L != null) {
            IntList next = L.tail;
            if (x != L.head) {
                if (last == null)
                    result = last = L;
                else
                    last = last.tail = L;
                L.tail = null;
            }
            L = next;
        }

        return result;
    }
}