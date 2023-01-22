from math import inf


def find_cheapest_path(graph: dict):
    processed = ['Meta']
    costs = build_costs_table(graph)
    parents = build_parents_table(graph)

    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        neighbours = graph[node]
        cost = costs[node]

        for x in neighbours:
            if neighbours[x] + cost < costs[x]:
                costs[x] = neighbours[x] + cost
                parents[x] = node
            
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    
    return print_cheapest_path(parents, costs)

    
def build_costs_table(graph: dict):
    nodes = [x for x in graph.keys() if x != 'Start'] + ['Meta']
    start_nodes = graph['Start']
    costs = {}

    for node in nodes:
        if node in start_nodes:
            costs[node] = start_nodes[node]
        else:
            costs[node] = float(inf)

    return costs


def build_parents_table(graph: dict):
    nodes = [x for x in graph.keys() if x != 'Start'] + ['Meta']
    start_nodes = graph['Start']
    parents = {}

    for node in nodes:
        if node in start_nodes:
            parents[node] = "Start"
        else:
            parents[node] = None

    return parents


def find_lowest_cost_node(costs, processed):
    lowest_cost = float(inf)
    lowest_cost_node = None

    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
        
    return lowest_cost_node

    
def print_cheapest_path(parents, costs, node = 'Meta'):
    if parents['Meta'] is None:
        return "Path not found"
    
    if node == 'Start':
        return f"({costs['Meta']}): Start"

    return print_cheapest_path(parents, costs, parents[node]) + ' -> ' + node



graph = {
    "Start": {
        "A": 5,
        "B": 2
    },
    "A": {
        "C": 4,
        "D": 2
    },
    "B": {
        "A": 8,
        "D": 7
    },
    "C": {
        "D": 6,
        "Meta": 3
    },
    "D": {
        "Meta": 1
    }
}

print(find_cheapest_path(graph))