class MyArrayListIterator implements Iterator{

   private int current = 0;
   private MyArrayList arrList;
   
   MyArrayListIterator(MyArrayList arrList){
      this.arrList = arrList;
   }
   
   public boolean hasNext(){
      return (current < arrList.size());
   }
   
   public Object next(){
      return arrList.data[current++];
   }

}