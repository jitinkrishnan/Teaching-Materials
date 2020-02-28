public class MyCoolArrayList<T>{
   
   T[] data; 
   int size; // Holds elements, virtual size
   
   public MyCoolArrayList(){ // Initialize fields
      this.data = (T[]) new Object[10];
      this.size = 0;
   }
   public int size(){ // Virtual size of AL
      return this.size;
   }
   
   // Add an element to the end
   public void add(T x){
      // if the array is full, then expand
     if(this.size == this.data.length){
         // 1. create a new larger array
         T[] o = (T[]) new Object[(3*this.size/2)+1];
         // 2. copy items from old array to new array
         for(int i=0; i<this.size; i++){
          o[i] = this.data[i];
         } 
         // 4. set old array to new array
         this.data = o; 
      } 
      
      // 3. add the new elements to the array
      this.data[this.size] = x;
      this.size++;
   }
   
   public T get(int i){ // Retrieve element i
      return this.data[i];
   }
   
   //HOMEWORK
   
   //public void set(int i, T x); // Replace element i with x
   
   // public void insert(int i, T x); // Insert x at position i, shift
   // elements if necessary
   
   //public void remove(int i); // Remove element at position i,
   // shift elements to remove gap*/
}