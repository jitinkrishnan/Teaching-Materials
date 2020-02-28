public class MyArrayList<T>{
   
   /******* DATA MEMBERS *********/
   private Object[] data; 
   private int size; // Holds elements, virtual size
   
   /******* CONSTRUCTOR *********/
   public MyArrayList(){ 
      this.data = new Object[10];
      this.size = 0;
   }
   
   /******* METHOD: SIZE *********/
   public int size(){ // Virtual size of AL
      return this.size;
   }
   
   /******* METHOD: ADD *********/
   public void add(T x){
     if(this.size == this.data.length){
         Object[] o = new Object[(3*this.size/2)+1];
         for(int i=0; i<this.size; i++){
          o[i] = this.data[i];
         } 
         this.data = o; 
      } 
      this.data[this.size] = x;
      this.size++;
   }
   
   /******* METHOD: GET *********/
   public T get(int i){ // Retrieve element i
      return (T) this.data[i];
   }
   
   // ITERATOR CREATION
   public Iterator iterator(){
      return new MyArrayListIterator(this);
   }
   
   // NESTED CLASS ITERATOR
   private static class MyArrayListIterator implements Iterator{

   private int current = 0;
   private MyArrayList arrList;
   
   private MyArrayListIterator(MyArrayList arrList){
      this.arrList = arrList;
   }
   
   public boolean hasNext(){
      return (current < arrList.size());
   }
   
   public Object next(){
      return arrList.data[current++];
   }

}
   
   
}