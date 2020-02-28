import java.util.*;

class Vertex{
   public String name;
   public List<Edge> adj;
   
   public Vertex (String name){
      this.name = name;
      adj = new LinkedList<Edge>();
   }
   
   public void printAdjList(){
      for(Edge e: adj){
         System.out.print(e.dest.name+"("+e.cost+") ");
      }
      System.out.println();
   }
}