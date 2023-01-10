from collections import deque

def is_name_ok(name):
    return name[-1] == 'k'

def breadth_first_search(name, graph):
    queue = deque()
    queue += graph[name]

    searched_names = []
    while queue:
        current_name = queue.popleft()

        if current_name in searched_names:
            continue

        if is_name_ok(current_name):
            print(current_name)
            return True
        
        queue += graph[current_name]

    print("Didn't find")
    return False


graph = {
    "Mike": ["John", "Adam", "Anna"],
    "John": ["Bob", "Carol", "Robert"],
    "Adam": ["Anna", "Marcus"],
    "Anna": [],
    "Bob": ["Mike"],
    "Carol": ["Jennifer", "Robert"],
    "Robert": [],
    "Marcus": ["Frank"],
    "Jennifer": [],
    "Frank": []
}

breadth_first_search("John", graph)