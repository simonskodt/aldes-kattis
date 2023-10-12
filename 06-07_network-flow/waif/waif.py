import sys
import graph as gr

# No. of children, no. toys, and no. toy categories
n, m, p = map(int, next(sys.stdin).split())
SOURCE, CHILD, TOY, CATEGORY, SINK = 's', 'C', 'T', 'G', 't'

def main():
    graph = setup_graph()
    path = bfs(graph)

    print(max_flow(graph, path))

def max_flow(graph, path):
    max_flow = 0

    while path:
        graph, flow = augment(graph, path)
        max_flow += flow
        path = bfs(graph)

    return max_flow

def augment(graph, path):
    b = bottleneck(graph, path)

    for i in range(len(path)-1):
        u, v = path[i], path[i+1]
        capacity = graph.get_path_capacity(u, v)
        is_forward_edge = capacity > 0

        if is_forward_edge:
            # increase f(edge) in G by b
            graph.add_edge(v, u, b)
            graph.update_path_weight(u, v, capacity-b)
        elif not is_forward_edge:
            # decrease f(edge) in G by b
            graph.update_path_weight(u, v, capacity-b)
            graph.update_path_weight(u, v, b)

    return graph, b

def bottleneck(graph, path):
    weights = [graph.get_path_capacity(path[i], path[i+1]) for i in range(len(path)-1)]
    return min(weights)

def bfs(graph):
    queue = [(SOURCE, [SOURCE])]
    visited = [SOURCE]

    while queue:
        u, path = queue.pop(0)
        adj_nodes = graph.get_adjacent_nodes(u)

        for node, capacity in adj_nodes:
            if node not in visited and capacity > 0:
                queue.append((node, path + [node]))
                visited.append(node)

                if node == SINK:
                    return path + [SINK]
                
    return []

def setup_graph():
    graph = gr.Graph()

    # Add the children, C_i, and toys, T_i, to the graph
    for i in range(1, n+1):
        k, *toys = map(int, input().split())
        graph.add_node(CHILD + str(i))

        for j in range(1, k+1):
            graph.add_node(TOY + str(toys[j-1]))
            graph.add_edge(CHILD + str(i), TOY + str(toys[j-1]))

    # Add the toys, T_i, into their respective categories, G_i
    for i in range(1, p+1):
        l, *toys, r = map(int, input().split())
        graph.add_node(CATEGORY + str(i))

        for j in range(1, l+1):
            graph.add_edge(TOY + str(toys[j-1]), CATEGORY + str(i))

        graph.add_edge(CATEGORY + str(i), SINK, r)

    # Add a edge to the sink node from uncategorized toys
    for i in range(1, m+1):
        if graph.node_has_no_adjacent_nodes(TOY + str(i)):
            graph.add_edge(TOY + str(i), SINK)

    return graph

if __name__ == "__main__":
    main()