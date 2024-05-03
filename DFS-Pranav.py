
def dfs(visited, graph, node,goal):
    visited.append(node)
    print(node, end="\n")

    if node == goal:
        return True

    for neighbour in graph[node]:
        if neighbour not in visited:    
            if dfs(visited, graph, neighbour,goal):
                return True

    return False

#PRANAV KUMAR
#PRN 1032200232
if __name__ == '__main__':
    
    graph = {
    '0': ['1', '2', '3'],
    '1': ['0', '4'],
    '2': ['4', '5'],
    '3': ['0', '5'],
    '4': ['1', '5'],
    '5': ['5']
    }

    visited = []
    goal = '5'
    start = '0'
    dfs(visited, graph, start,goal)
    
