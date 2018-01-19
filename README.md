# Dijkstra's Algorithm

![Dijkstra's algorithm runtime](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif "Dijkstra's algorithm runtime")

Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. The algorithm exists in many variants; Dijkstra's original variant found the shortest path between two nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

For a given source node in the graph, the algorithm finds the shortest path between that node and every other. It can also be used for finding the shortest paths from a single node to a single destination node by stopping the algorithm once the shortest path to the destination node has been determined. For example, if the nodes of the graph represent cities and edge path costs represent driving distances between pairs of cities connected by a direct road, Dijkstra's algorithm can be used to find the shortest route between one city and all other cities. As a result, the shortest path algorithm is widely used in network routing protocols, most notably IS-IS (Intermediate System to Intermediate System) and Open Shortest Path First (OSPF). It is also employed as a subroutine in other algorithms such as [Johnson's](https://en.wikipedia.org/wiki/Johnson%27s_algorithm).

### Algorithm
Let the node at which we are starting be called the **initial node**. Let the distance of node *Y* be the distance from the initial node to *Y*. Dijkstra's algorithm will assign some initial distance values and will try to improve them step by step.
1. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes
2. Set the initial node as current. Mark all other nodes unvisited. Create a set of all the unvisited nodes called the *unvisited* set
3. For the current node, consider all of its neighbors and calculate their *tentative* distances. Compare the newly calculated *tentative* distance to the current assigned value and assign the smaller one. For example, if the current node *A* is marked with a distance of 6, and the edge connecting it with a neighbor *B* has length 2, then the distance to *B* (through *A*) will be 6 + 2 = 8. If *B* was previously marked with a distance greater than 8 then change it to 8. Otherwise, keep the current value
4. When we are done considering all of the neighbors of the current node, mark the current node as visited and remove it from the *unvisited* set. A visited node will never be checked again
5. If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the *unvisited* set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished
6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 3

### How to Use
Create the directory `dijkstra` in your localhost document root and copy [`index.php`](../blob/master/index.php) there
The Python script will output `result.json` in your `[DOCUMENT_ROOT]/dijkstra` before it opens the new tab in your default web browser with the URL http://localhost/dijkstra

Run the Python script with the following command:
```
$ python3 main.py
```
