# Number of vertices
V = 7

INF = 99999

# A utility function to print the solution
def printSolution(dist):
    print "Following matrix shows the shortest distances between every pair of vertices"
    for i in xrange(V):
        for j in xrange(V):
            if dist[i][j] == INF:
                print "%7s" %("INF"),
            else:
                print "%7d\t" %(dist[i][j]),
            if j == V - 1:
                print ""


# solve all pair shortest path via Floyd-Warshall Algorithm
def floydWarshall(graph):
    """
    dist[][] will be the output matrix that will finally
    have the shortest distances between every pair of vertices.
    """

    """
    Initializing the solution matrix same as input graph matrix
    OR we can say that the initial values of shortest distances
    are based on shortest paths considerting no
    intermedidate vertices.
    """
    dist = map(lambda i : map(lambda j : j, i), graph)


    """
    Add all vertices one by one to the set of intermediate vertices.
    ---> Before start of a iteration, we have shortest distances
    between all pairs of vertices such that the shortest
    distances consider only the vertices in set
    {0, 1, 2, .. k-1} as intermediate vertices.
    ----> After the end of a iteration, vertex no. k is
    added to the set of intermediate vertices and the
    set becomes {0, 1, 2, .. k}.
    """
    for k in xrange(V):

        # pick all vertices as source one by one.
        for i in xrange(V):

            # pick all vertices as destination for the
            # above picked source.
            for j in xrange(V):
                # If vertex k is on the shortest path from 
                # i to j, then update the value of dist[i][j].
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        printSolution(dist)
    
    #printSolution(dist)

if __name__ == '__main__':
    graph = [[0, -1, INF, 2, INF, INF, INF],
             [INF, 0, INF, INF, -1, INF, INF],
             [4, INF, 0, INF, -2, -1, INF],
             [INF, INF, -2, 0, INF, 3, INF],
             [3, INF, INF, INF, 0, INF, 2],
             [INF, INF, INF, INF, INF, 0, 2],
             [INF, INF, 1, INF, INF, INF, 0]]

    # Print the solution
    floydWarshall(graph);

