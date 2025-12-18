def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_simple(grid, start, goal):
    open_list = [start]        
    came_from = {}             
    g = {start: 0}             

    rows, cols = len(grid), len(grid[0])

    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    while open_list:
        #
        current = min(open_list, key=lambda x: g[x] + heuristic(x, goal))

       
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return [start] + path[::-1]

        open_list.remove(current)

        
        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 1:
                    continue  

                neighbor = (nx, ny)
                new_cost = g[current] + 1

                
                if neighbor not in g or new_cost < g[neighbor]:
                    g[neighbor] = new_cost
                    came_from[neighbor] = current

                    if neighbor not in open_list:
                        open_list.append(neighbor)

    return None


grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start_pos = (0, 0)
goal_pos = (4, 4)

path = a_star_simple(grid, start_pos, goal_pos)
print("Shortest Path:", path)