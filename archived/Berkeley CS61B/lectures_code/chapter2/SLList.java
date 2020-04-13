/**
 * Accompanying with IntNode class, SLList is an improvement version for IntList.
 * Essentially, the SLList class acts as a middleman between the list user and the naked recursive data structure.
 */
public class SLList {
    // nested class: no meaningful effect on code performance, 
    // is simply a tool for keeping code organized.

    // If the nested class has no need to use any of the instance methods or 
    // variables of SLList, you may declare the nested class static, as follows.
    // This saves a bit of memory, because each IntNode no longer
    // needs to keep track of how to access its enclosing SLList.
    public static class IntNode {
        public int item;
        public IntNode next;

        public IntNode(int i, IntNode n) {
            item = i;
            next = n;
        }
    }

	/* The first item (if it exists) is at sentinel.next. */
	private IntNode sentinel;
    private int size;

    public SLList() {
        sentinel = new IntNode(63, null);
        size = 0;
    }

    public SLList(int x) {
        sentinel = new IntNode(63, null);
        sentinel.next = new IntNode(x, null);
        size = 1;
    }

    /** Adds an item to the front of the list. */
    public void addFirst(int x) {
        sentinel.next = new IntNode(x, sentinel.next);
        size += 1;
    }

    /** Retrieves the front item from the list. */
    public int getFirst() {
        return sentinel.next.item;
    }

    /** Retrieves the number of items in the list using recursion */
    public int size() {
        return size(sentinel.next);
    }

    private static int size(IntNode p) {
        if (p == null)
            return 0;
        else if (p.next == null)
            return 1;
        
        return 1 + size(p.next);
    }

    public int getSize() {
        return size;
    }

    /** Adds an item to the end of the list. */
    public void addLast(int x) {
        size += 1;
        IntNode p = sentinel;

        /* Advance p to the end of the list. */
        while (p.next != null) {
            p = p.next;
        }

        p.next = new IntNode(x, null);
    }
}