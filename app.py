import heapq  # Importing heapq for priority queue



class Node:

    def __init__(self, position, parent=None, g=0, h=0):

        self.position = position  # (x, y) coordinates

        self.parent = parent  # Parent node to trace the path

        self.g = g  # Cost from start node to current node

        self.h = h  # Estimated cost from current node to goal

        self.f = g + h  # Total estimated cost



    def __lt__(self, other):  

        return self.f < other.f  # Priority queue compares nodes based on f(n)



def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance heuristic



def astar(grid, start, goal):

    open_list = []  # Priority queue for nodes to explore

    closed_set = set()  # Set of visited nodes

    heapq.heappush(open_list, Node(start, None, 0, heuristic(start, goal)))  



    while open_list:

        current = heapq.heappop(open_list)  # Get node with lowest f(n)



        if current.position == goal:  # Goal reached, backtrack to find path

            path = []

            while current:

                path.append(current.position)

                current = current.parent

            return path[::-1]  # Return reversed path



        closed_set.add(current.position)



        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Possible moves (up, right, down, left)

            neighbor_pos = (current.position[0] + dx, current.position[1] + dy)



            if neighbor_pos in closed_set or not (0 <= neighbor_pos[0] < len(grid) and 0 <= neighbor_pos[1] < len(grid[0])) or grid[neighbor_pos[0]][neighbor_pos[1]] == 1:

                continue  # Skip if visited, out of bounds, or obstacle



            g = current.g + 1  # Cost to move to this node

            h = heuristic(neighbor_pos, goal)  # Estimate remaining cost

            neighbor_node = Node(neighbor_pos, current, g, h)



            heapq.heappush(open_list, neighbor_node)  # Add to priority queue



    return None  # No path found



# Example Grid (0 = open space, 1 = obstacle)

grid = [

    [0, 0, 0, 0, 1],

    [1, 1, 0, 1, 0],

    [0, 0, 0, 0, 0],

    [0, 1, 1, 1, 0],

    [0, 0, 0, 0, 0]

]



start = (0, 0)  # Start position

goal = (4, 4)  # Goal position



path = astar(grid, start, goal)  # Run A* Algorithm


print("Path:", path)  # Output the shortest path