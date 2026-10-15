from collections import deque

# --- State: (robot_pos, left_dirty, right_dirty) ---
# robot_pos: 'L' or 'R'
# left_dirty / right_dirty: True if dirty, False if clean

initial_state = ('L', True, True)  # both dirty, robot on left

def is_goal(state):
    return state[1] == False and state[2] == False

def transition(state, action):
    pos, left, right = state
    if action == 'left':
        return ('L', left, right)
    elif action == 'right':
        return ('R', left, right)
    elif action == 'suck':
        if pos == 'L':
            return ('L', False, right)
        else:
            return ('R', left, False)

actions = ['left', 'right', 'suck']

# --- Node class to track state and parent for path reconstruction ---
class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

# --- Dynamic child generation using transition function ---
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

    return None  # no solution found

def reconstruct_path(node):
    path = []
    while node.parent is not None:
        path.append((node.action, node.state))
        node = node.parent
    path.reverse()
    return path

# --- Run ---
print("Initial State:", initial_state)
solution = bfs(initial_state)
if solution:
    print("Solution found in", len(solution), "steps:")
    for step, (action, state) in enumerate(solution, 1):
        print(f"  Step {step}: {action} -> {state}")
else:
    print("No solution found.")