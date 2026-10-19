
def dfs_can_reach(maze, start, exit_room, visited=None):
    if visited is None:
        visited = []

    if start not in visited:
        visited.append(start)

        if start == exit_room:
            return True

        for neighbour in maze[start]:
            if dfs_can_reach(maze, neighbour, exit_room, visited):
                return True

    return False


maze = {
    "Entrance": ["Hall1", "Hall2"],
    "Hall1": ["Room1"],
    "Hall2": ["Room2", "Trap"],
    "Room1": [],
    "Room2": ["Exit"],
    "Trap": [],
    "Exit": [],
    "Scerectroom":[]
}

visited = []
result = dfs_can_reach(maze, "Entrance", "Exit", visited)

print("Visit order:", visited)
print("Can reach Exit from Entrance?", result)
    