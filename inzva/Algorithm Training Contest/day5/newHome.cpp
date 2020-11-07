#include<bits/stdc++.h> 
using namespace std; 
# define INF 0x3f3f3f3f 
  
// iPair ==> Integer Pair 
typedef pair<int, int> iPair; 
  
// To add an edge 
void addEdge(vector <pair<int, int> > adj[], int u, 
                                     int v, int wt) 
{ 
    adj[u].push_back(make_pair(v, wt)); 
    adj[v].push_back(make_pair(u, wt)); 
} 
   
  
// Prints shortest paths from src to all other vertices 
void shortestPath(vector<pair<int,int> > adj[], int V, int src,int*T , int nT) 
{ 
    // Create a priority queue to store vertices that 
    // are being preprocessed. This is weird syntax in C++. 
    // Refer below link for details of this syntax 
    // http://geeksquiz.com/implement-min-heap-using-stl/ 
    priority_queue< iPair, vector <iPair> , greater<iPair> > pq; 
  
    // Create a vector for distances and initialize all 
    // distances as infinite (INF) 
    vector<int> dist(V, INF); 
  
    // Insert source itself in priority queue and initialize 
    // its distance as 0. 
    pq.push(make_pair(0, src)); 
    dist[src] = 0; 
  
    /* Looping till priority queue becomes empty (or all 
    distances are not finalized) */
    while (!pq.empty()) 
    { 
        // The first vertex in pair is the minimum distance 
        // vertex, extract it from priority queue. 
        // vertex label is stored in second of pair (it 
        // has to be done this way to keep the vertices 
        // sorted distance (distance must be first item 
        // in pair) 
        int u = pq.top().second; 
        pq.pop(); 
  
        // Get all adjacent of u.  
        for (auto x : adj[u]) 
        { 
            // Get vertex label and weight of current adjacent 
            // of u. 
            int v = x.first; 
            int weight = x.second; 
  
            // If there is shorted path to v through u. 
            if (dist[v] > dist[u] + weight) 
            { 
                // Updating distance of v 
                dist[v] = dist[u] + weight; 
                pq.push(make_pair(dist[v], v)); 
            } 
        } 
    } 
  
    // Print shortest distances stored in dist[] 
    //printf("Vertex Distance from Source\n"); 
    int minn = dist[T[0]];
    for (int i = 0; i < nT; ++i){ 
        //printf("%d \t\t %d\n", i, dist[i]);
        if (dist[T[i]] < minn) minn = dist[T[i]];
    }
     printf("%d",minn);
}       
  
  
int main() 
{   
    int node , nT ,edges, i;
    
    
    scanf("%d %d",&node,&nT);
    int T[nT];
    for(i = 0 ; i < nT ; i++) scanf("%d",&T[i]);
    scanf("%d",&edges);
    vector<iPair > adj[node];
    for(i=0;i < edges; i++){
        int u , v , w ;
        scanf("%d %d %d",&u,&v,&w);
        addEdge(adj,u,v,w);
        
    }
  
    shortestPath(adj, node, 0,T,nT); 
  
    return 0; 
} 
