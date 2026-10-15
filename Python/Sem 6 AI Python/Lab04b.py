from collections import deque

# --- State: (robot_row, robot_col, dirty_00, dirty_01, dirty_10, dirty_11) ---
# Grid positions:  (0,0) top-left   (0,1) top-right
#                  (1,0) bottom-left (1,1) bottom-right
# dirty_XX: True if dirty, False if clean

initial_state = (0, 0, True, True, True, True)  # robot at (0,0), all 4 dirty

def is_goal(state):
    # Goal: all four squares are clean
    return state[2] == False and state[3] == False and state[4] == False and state[5] == False

def transition(state, action):
    row, col, d00, d01, d10, d11 = state
    if action == 'up':
        new_row = max(row - 1, 0)
        return (new_row, col, d00, d01, d10, d11)
    elif action == 'down':
        new_row = min(row + 1, 1)
        return (new_row, col, d00, d01, d10, d11)
    elif action == 'left':
        new_col = max(col - 1, 0)
        return (row, new_col, d00, d01, d10, d11)
    elif action == 'right':
        new_col = min(col + 1, 1)
        return (row, new_col, d00, d01, d10, d11)
    elif action == 'suck':
        # Clean the square the robot is currently on
        dirty = [d00, d01, d10, d11]
        index = row * 2 + col  # map (row, col) to dirty list index
        dirty[index] = False
        return (row, col, dirty[0], dirty[1], dirty[2], dirty[3])

actions = ['up', 'down', 'left', 'right', 'suck']

# --- Node class ---
class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

# --- Dynamic child generation ---
def expandAndReturnChildren(node):
    children = []
    for action in actions:
        new_state = transition(node.state, action)
        children.append(Node(new_state, node, action))
    return children

# --- BFS ---
def bfs(initial_state):
    start_node = Node(initial_state)
    if is_goal(start_node.state):
        return reconstruct_path(start_node)

    frontier = deque([start_node])
    explored = set()
    explored.add(initial_state)

    while frontier:
        node = frontier.popleft()
        for child in expandAndReturnChildren(node):
            if child.state not in explored:
                if is_goal(child.state):
                    return reconstruct_path(child)
                explored.add(child.state)
                frontier.append(child)

    return None

def reconstruct_path(node):
    path = []
    while node.parent is not None:
        path.append((node.action, node.state))
        node = node.parent
    path.reverse()
    return path

# --- Run ---
print("=== 2x2 Vacuum World (BFS) ===")
print("Initial State:", initial_state)
print("Grid: (row, col, dirty_00, dirty_01, dirty_10, dirty_11)\n")

solution = bfs(initial_state)
if solution:
    print(f"Solution found in {len(solution)} steps:")
    for step, (action, state) in enumerate(solution, 1):
        row, col = state[0], state[1]
        print(f"  Step {step}: {action:>5} -> robot at ({row},{col}), dirty = {list(state[2:])}")
else:
    print("No solution found.")