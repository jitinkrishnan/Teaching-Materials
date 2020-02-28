/***************************
 * Author: Jitin Krishnan
 * CS310 Fall 2017
 *
 * Linked List with Head
 ***************************/
public class HLinkedList<AnyType>{

   // NODE CLASS
   private class ListNode<AnyType> {
	   AnyType value;
	   ListNode<AnyType> next;
      
      public ListNode(AnyType value){
         this.value = value;
      }
   }


	private ListNode<AnyType> head;
   private ListNode<AnyType> current;
	
	public HLinkedList(){
        head = new ListNode<AnyType>(null);
        current = head; 
        head.next = null;
   }

   public void insert(AnyType x){
      
         ListNode<AnyType> temp = new ListNode<AnyType>(x);
         temp.next = current.next;
         current.next = temp;
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
