/***************************
 * Author: Jitin Krishnan
 * CS310 Fall 2017
 *
 * A Doubly Linked List
 ***************************/
public class DoublyLinkedList<AnyType>{

   // NODE CLASS
   private class ListNode<AnyType> {
	   AnyType value;
	   ListNode<AnyType> next;
      ListNode<AnyType> prev;
      
      public ListNode(AnyType value){
         this.value = value;
      }
   }


	private ListNode<AnyType> head;
   private ListNode<AnyType> current;
   private ListNode<AnyType> tail;
	
	public DoublyLinkedList(){
        head = new ListNode<AnyType>(null);
        tail = new ListNode<AnyType>(null);
        current = head; 
        head.next = tail;
        tail.prev = head;
   }

   public void insert(AnyType x){
      
         ListNode<AnyType> temp = new ListNode<AnyType>(x);
         temp.prev = current;
         temp.next = current.next;
         current.next = temp;
         temp.next.prev = temp;
         current = temp;
   
   }
   
   public void printList(){
   
      ListNode<AnyType> loop = head;
      while(loop != null){
         System.out.print(loop.value + " ");
         loop = loop.next;
      }
   
   }
   
}
