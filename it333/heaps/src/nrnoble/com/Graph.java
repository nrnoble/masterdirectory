package nrnoble.com;

/**
 * Created by Neal on 5/7/2017.
 */
public class Graph
{

    private final int V;// number of vertices
    private int E;                // number of edges
    private Bag<Integer>[] adj;   // adjacency lists

    public Graph(int V)
    {
        this.V = V;
        this.E = 0;
        adj = (Bag<Integer>[]) new Bag[V];      // Create array of lists.
        for (int v = 0; v < V; v++)             // Initialize all lists
            adj[v] = new Bag<Integer>();         //   to empty.
    }

    public Graph(In in)
    {
        this(in.readInt());          // Read V and construct this graph.
        int E = in.readInt();        // Read E.
        for (int i = 0; i < E; i++)
        {  // Add an edge.
            int v = in.readInt();     // Read a vertex,
            int w = in.readInt();     // read another vertex,
            addEdge(v, w);               // and add edge connecting them.
        }
    }


    public int V()
    {
        return V;
    }

    public int E()
    {
        return E;
    }

    public void addEdge(int v, int w)
    {
        adj[v].add(w);                          // Add w to v’s list.
        adj[w].add(v);                          // Add v to w’s list.
        E++;
    }

    public Iterable<Integer> adj(int v)
    {
        return adj[v];
    }
}
















    //compute maximum degree
    public static int degree(Graph G, int v)
    {
        int degree = 0;
        for (int w : G.adj(v)) degree++;
        return degree;
    }
   // compute maximum degree
    public static int maxDegree(Graph G)
    {
        int max = 0;
        for (int v = 0; v < G.V(); v++)
            if (degree(G, v) > max)
                max = degree(G, v);
        return max; }
    //compute average degree
    public static int avgDegree(Graph G)
    {
        return 2 * G.E() / G.V();
    }
    //count self-loops
    public static int numberOfSelfLoops(Graph G) /
    {   int count = 0;
        for (int v = 0; v < Graph.V(); v++)
            for (int w : Graph.adj(v))
                if (v == w) count++;
        return count/2; // each edge counted twice
    }
    //string representation of the Graph’s adjacency lists (instance method in Graph)
    public String toString()
    {
        String s = V + " vertices, " + E + " edges\n";
        for (int v = 0; v < V; v++)
        {
            s += v + ": ";
            for (int w : this.adj(v))
                s += w + " ";
            s += "\n";   }
        return s;
    }

}
