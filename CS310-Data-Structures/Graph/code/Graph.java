import java.util.*;
public class Graph{

   private Map<String, Vertex> vertexMap = new HashMap<String, Vertex>();
   
   public void addEdge(String source, String dest, double cost){
      Vertex v = getVertex(source);
      Vertex w = getVertex(dest);
      v.adj.add(new Edge(w,cost));
   }
   
   private Vertex getVertex(String vertexName){
      Vertex v = vertexMap.get(vertexName);
      if(v == null){
         v = new Vertex(vertexName);
         vertexMap.put(vertexName, v);
      }
      return v;
   }
   
   private void printAdjList(String vname){
      Vertex v = vertexMap.get(vname);
      v.printAdjList();
   }
   
   public void dijskra(String name){
      // TO DO
   }
   
   // main
   public static void main(String[] args){
      Graph g = new Graph();
      
      // you should know how to read from file
      
      // creating graph manually
      
      g.addEdge("D", "C", 10);
      g.addEdge("A", "B", 12);
      g.addEdge("D", "B", 23);
      g.addEdge("A", "D", 87);
      g.addEdge("E", "D", 43);
      g.addEdge("B", "E", 11);
      g.addEdge("C", "A", 19);
      
      g.printAdjList("A");
   
   }
   
}