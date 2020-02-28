public class test{

   public static void main(String[] args){
   
      MyArrayList<Integer> myList = new MyArrayList<Integer>();
      
      myList.add(5);
      myList.add(10);
      myList.add(27);
      
      MyArrayListIterator itr = myList.iterator();
      while(itr.hasNext()){
         System.out.println(itr.next());
      }

   }
}