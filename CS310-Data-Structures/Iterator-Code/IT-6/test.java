public class test{

   public static void main(String[] args){
  

      DoublyLinkedList<Integer> myList = new DoublyLinkedList<Integer>();
      
      myList.insert(5);
      myList.insert(10);
      
      Iterator itr = myList.iterator();
      while(itr.hasNext()){
         System.out.println(itr.next());
      }
      
   }
}