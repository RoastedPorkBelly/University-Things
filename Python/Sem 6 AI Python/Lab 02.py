class Node:
  def __init__(self, state=None, parent=None):
    self.state  = state
    self.parent = parent

def expandAndReturnChildren(state_space, node):
  children = []
  for [m, n, c] in state_space:
    if   m == node.state: children.append(Node(n, node))
    elif n == node.state: children.append(Node(m, node))
  return children

def bfs(state_space, initial_state, goal_state):
  frontier  = []
  explored  = []
  found_goal = False
  frontier.append(Node(initial_state, None))

  while not found_goal:
    children = expandAndReturnChildren(state_space, frontier[0])
    explored.append(frontier[0])
    del frontier[0]
    for child in children:
      in_exp = child.state in [e.state for e in explored]
      in_fr  = child.state in [f.state for f in frontier]
      if not in_exp and not in_fr:
        if child.state == goal_state:
          found_goal = True
          goal_node  = child
          break
        frontier.append(child)

  solution   = [goal_node.state]
  trace_node = goal_node
  while trace_node.parent is not None:
    solution.insert(0, trace_node.parent.state)
    trace_node = trace_node.parent
  return solution

initial_state = "Arad"
goal_state    = "Bucharest"

state_space = [
  ['Arad',      'Zerind',       75],
  ['Arad',      'Sibiu',        140],
  ['Arad',      'Timisoara',    118],
  ['Zerind',    'Oradea',       71],
  ['Oradea',    'Sibiu',        151],
  ['Timisoara', 'Lugoj',        111],
  ['Lugoj',     'Mehadia',      70],
  ['Mehadia',   'Drobeta',      75],
  ['Drobeta',   'Craiova',      120],
  ['Craiova',   'RimnicuVilcea', 146],
  ['Craiova',   'Pitesti',      138],
  ['Sibiu',     'Fagaras',      99],
  ['Sibiu',     'RimnicuVilcea', 80],
  ['RimnicuVilcea', 'Pitesti',  97],
  ['Fagaras',   'Bucharest',    211],
  ['Pitesti',   'Bucharest',    101],
  ['Bucharest', 'Giurgiu',      90],
  ['Bucharest', 'Urziceni',     85],
  ['Urziceni',  'Hirsova',      98],
  ['Urziceni',  'Vaslui',       142],
  ['Hirsova',   'Eforie',       86],
  ['Vaslui',    'Iasi',         92],
  ['Iasi',      'Neamt',        87],
]

if __name__ == '__main__':
  print('Solution: ' + str(bfs(state_space, initial_state, goal_state)))