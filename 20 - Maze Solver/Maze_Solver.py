def print_maze(maze):
    for row in maze:
        print(" ".join(row))
    print()


def solve_maze(maze, x, y):

    rows = len(maze)
    cols = len(maze[0])

    # Out of bounds
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return False

    # Wall or visited
    if maze[x][y] == "#" or maze[x][y] == ".":
        return False

    # Goal found
    if maze[x][y] == "E":
        return True

    # Mark current path
    if maze[x][y] != "S":
        maze[x][y] = "."

    # Move: Down, Right, Up, Left
    if (solve_maze(maze, x + 1, y) or
        solve_maze(maze, x, y + 1) or
        solve_maze(maze, x - 1, y) or
        solve_maze(maze, x, y - 1)):
        return True

    # Backtrack
    if maze[x][y] == ".":
        maze[x][y] = " "

    return False


maze = [
    ["S", " ", "#", " ", " "],
    ["#", " ", "#", " ", "#"],
    [" ", " ", " ", " ", "#"],
    [" ", "#", "#", " ", " "],
    [" ", " ", " ", "#", "E"]
]

start_x = 0
start_y = 0

print("=" * 40)
print("        MAZE SOLVER")
print("=" * 40)

print("\nOriginal Maze:\n")
print_maze(maze)

if solve_maze(maze, start_x, start_y):
    print("Path Found!\n")
else:
    print("No Path Exists.\n")

print_maze(maze)