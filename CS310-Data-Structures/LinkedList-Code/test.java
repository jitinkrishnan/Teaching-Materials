public class test{

   public static void main(String[] args){

      DoublyLinkedList<String> myList1 = new DoublyLinkedList<String>();
      myList1.insert("apple");
      myList1.insert("orange");
      myList1.printList();
      
      HLinkedList<Integer> myList2 = new HLinkedList<Integer>();
      myList2.insert(5);
      myList2.insert(10);
      myList2.printList();
      
   }
}