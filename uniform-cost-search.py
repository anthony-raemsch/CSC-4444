import heapq

# uniform cost function
# returns the minimum cost and the path with minimum cost
def uniform_cost_search(start, goal, graph, cost):
    answer = {node: {'cost': float('inf'), 'path': []} for node in goal}
#     **************************************
#     ******** Write your code here ********
#     **************************************
    pq = [(0, start, [])]
    visited = {}

    while pq:
        cost_of_current_node, node_im_currently_at, path_taken_to_node = heapq.heappop(pq)

        if node_im_currently_at in goal:
            return {node_im_currently_at: {'cost': cost_of_current_node, 'path': path_taken_to_node + [node_im_currently_at]}}

        if node_im_currently_at in visited and visited[node_im_currently_at] <= cost_of_current_node:
            continue

        visited[node_im_currently_at] = cost_of_current_node

        for neighbor_node in graph[node_im_currently_at]:
            edge_cost = cost.get((node_im_currently_at, neighbor_node), float('inf'))
            heapq.heappush(pq, (cost_of_current_node + edge_cost, neighbor_node, path_taken_to_node + [node_im_currently_at]))

    return answer

# main function
if __name__ == "__main__":
    # create a graph with no more than 30 nodes
    graph, cost = [[] for i in range(30)], {}

    # add edges to the graph
    graph[0].append(4)
    graph[0].append(5)
    graph[0].append(16)
    graph[2].append(1)
    graph[3].append(1)
    graph[4].append(2)
    graph[4].append(3)
    graph[4].append(5)
    graph[5].append(8)
    graph[5].append(18)
    graph[6].append(3)
    graph[6].append(7)
    graph[8].append(16)
    graph[8].append(17)
    graph[16].append(17)
    graph[18].append(6)

    # add cost to each edge
    cost[(0, 4)] = 3
    cost[(0, 5)] = 9
    cost[(0, 16)] = 1
    cost[(2, 1)] = 2
    cost[(3, 1)] = 2
    cost[(4, 2)] = 1
    cost[(4, 3)] = 8
    cost[(4, 5)] = 2
    cost[(5, 8)] = 3
    cost[(5, 18)] = 2
    cost[(6, 3)] = 3
    cost[(6, 7)] = 2
    cost[(8, 16)] = 4
    cost[(8, 17)] = 4
    cost[(16, 17)] = 15
    cost[(18, 6)] = 1

    # set start state 
    start = 0
    # set goal state, there can be multiple goal states
    goal = [7]

    # call uniform_search_cost function to get the minimum cost to reach the goal and the path with minimum cost
    # ****** You have to implement this function *****
    min_cost_info = uniform_cost_search(start, goal, graph, cost)

    for node, info in min_cost_info.items():
        print(f'Minimum cost from {start} to {node} is {info["cost"]}')
        print(f'Path: {info["path"]}')
