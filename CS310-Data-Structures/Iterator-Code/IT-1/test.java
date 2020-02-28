public class test{

   public static void main(String[] args){

      MyArrayList<Integer> myList = new MyArrayList<Integer>();
      myList.add(3);
      myList.add(4);
      System.out.println(myList.get(0));
      
      /************ ITERATE ****************/
      for(int i=0; i<myList.size(); i++){
            System.out.println(myList.get(i));   
        }
      
   }
}