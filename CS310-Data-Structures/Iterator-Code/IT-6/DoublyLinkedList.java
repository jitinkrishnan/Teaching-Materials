public class DoublyLinkedList<AnyType>{

	private ListNode<AnyType> head;
   private ListNode<AnyType> current;
   private ListNode<AnyType> tail;


   // NODE CLASS
  private class ListNode<AnyType> {
	   AnyType value;
	   ListNode<AnyType> next;
      ListNode<AnyType> prev;
      
      public ListNode(AnyType value){
         this.value = value;
      }
   }
   
    // ITERATOR CREATION
   public Iterator iterator(){
      return new LinkedListIterator();
   }
   
   // ITERATOR CLASS
   private class LinkedListIterator implements Iterator{

      private ListNode<AnyType> current_itr;
      
      LinkedListIterator(){
         current_itr = DoublyLinkedList.this.head;
      }
      
      LinkedListIterator(ListNode<AnyType> node){
         current_itr = node;
      }
   
      public boolean hasNext(){
         return (current_itr.next != null);
      }
   
      public AnyType get(){
         return current_itr.value;
      }
   
      public void advance(){
       current_itr = current_itr.next;;
      }
   
      public boolean isValid(){
         return current_itr!=null;
      }
      
      public AnyType next(){
       advance();
       return current_itr.value;
      }

   }

	// DOUBLYLINKED LIST CONSTRUCTOR
	public DoublyLinkedList(){
        head = new ListNode<AnyType>(null);
        tail = new ListNode<AnyType>(null);
        current = head; 
        head.next = tail;
        tail.prev = head;
   }

   // INSERT METHOD
   public void insert(AnyType x){
      
         ListNode<AnyType> temp = new ListNode<AnyType>(x);
         temp.prev = current;
         temp.next = current.next;
         current.next = temp;
         temp.next.prev = temp;
         current = temp;
   
   }
   
   /*public void printList(){
   
     LinkedListIterator itr;
   
     for(itr = this.first(); itr.isValid(); itr.advance()){
      System.out.println(itr.get());
     }
   
   }*/
   
  /* public LinkedListIterator first(){
      
      return new LinkedListIterator(head.next);
   
   }*/
   
   
}
