public class IntListTester {
    public static void main(String[] args) {
        IntList list = new IntList(10, null);
        list.tail = new IntList(8, null);
        list.tail.tail = new IntList(6, null);

        list = list.addFirst(12);

        System.out.println(list.sizeRecur());
        System.out.println(list.sizeIter());
        System.out.println(list.get(0));
    }
}