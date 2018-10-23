public class LinkedListDeque<T> {
	public static class Node<T> {
		public T item;
		public Node<T> prev;
		public Node<T> next;
		
		public Node(T item, Node<T> prev, Node<T> next) {
			this.item = item;
			this.prev = prev;
			this.next = next;
		}
	}
	
	private Node<T> firstSentinel;
	private Node<T> lastSentinel;
	private int size;
	
	/**
	 * creates an empty deque.
	 */
	public LinkedListDeque() {
		firstSentinel = new Node<T>(null, null, null);
		lastSentinel = new Node<T>(null, null, null);
		firstSentinel.next = lastSentinel;
		lastSentinel.prev = firstSentinel;
		size = 0;
	}
	
	/**
	 * Adds an item of type T to the front of the deque.
	 * @param item
	 */
	public void addFirst(T item) {
		firstSentinel.next = new Node<T>(item, firstSentinel, firstSentinel.next);
		size += 1;
	}
	
	/**
	 * Adds an item of type T to the back of the deque.
	 * @param item
	 */
	public void addLast(T item) {
		lastSentinel.prev = new Node<T>(item, lastSentinel.prev, lastSentinel);
		size += 1;
	}
	
	/**
	 * Returns true if deque is empty, false otherwise.
	 * @return boolean
	 */
	public boolean isEmpty() {
		if (firstSentinel.next.equals(lastSentinel))
			return true;
		else
			return false;
	}
	
	/**
	 * Returns the number of items in the deque.
	 * @return
	 */
	public int size() {
		return size;
	}
	
	/**
	 * Prints the items in the deque from first to last, separated by a space.
	 */
	public void printDeque() {
		Node<T> current = firstSentinel.next;
		
		while (!current.equals(lastSentinel)) {
			System.out.print(current.item + " ");
			
			current = current.next;
		}
		
		System.out.println();
	}
	
	/**
	 * Removes and returns the item at the front of the deque. If no such item exists, returns null.
	 * @return removed first item
	 */
	public T removeFirst() {		
		Node<T> firstNode = firstSentinel.next;
		T item = firstNode.item;
		
		if (!firstNode.equals(lastSentinel)) {
			firstSentinel.next = firstNode.next;
			firstNode.next.prev = firstSentinel;
			
			firstNode = null;
			
			return item;
		} else {
			return null;
		}
 	}
	
	/**
	 * Removes and returns the item at the back of the deque. If no such item exists, returns null.
	 * @return removed last item
	 */
	public T removeLast() {
		Node<T> lastNode = lastSentinel.prev;
		T item = lastNode.item;
		
		if (!lastNode.equals(firstSentinel)) {
			lastSentinel.prev = lastNode.prev;
			lastNode.prev.next = lastSentinel;
			
			lastNode = null;
			
			return item;
		} else {
			return null;
		}
	}
	
	/**
	 * Gets the item at the given index, where 0 is the front, 1 is the next item, and so forth. 
	 * If no such item exists, returns null. Must not alter the deque!
	 * @param index
	 * @return item
	 */
	public T get(int index) {
		Node<T> currentNode = firstSentinel.next;
		
		while (index != 0 && !currentNode.equals(lastSentinel)) {
			currentNode = currentNode.next;
			
			index -= 1;
		}
		
		if (index == 0)
			return currentNode.item;
		else
			return null;
	}
	
	/**
	 * Same as get, but uses recursion.
	 * @param index
	 * @return item
	 */
	public T getRecursive(int index) {
		return getRecursiveHelper(firstSentinel.next, index);
	}
	
	/**
	 * Helper method for getRecursive method
	 * @param Node
	 * @param index
	 * @return item
	 */
	private T getRecursiveHelper(Node<T> Node, int index) {
		if (index == 0)
			return Node.item;
		else
			if (!Node.next.equals(lastSentinel))
				return getRecursiveHelper(Node.next, index--);
			else
				return null;
	}	
}
