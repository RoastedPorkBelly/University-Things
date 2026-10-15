class Node:
  def __init__(self, state=None, parent=None, path_cost=0):
    self.state     = state
    self.parent    = parent
    self.path_cost = path_cost

def expandAndReturnChildren(state_space, node):
  children = []
  for [m, n, c] in state_space:
    if m == node.state:
      children.append(Node(n, node, node.path_cost + c))
    elif n == node.state:
      children.append(Node(m, node, node.path_cost + c))
  return children

def ucs(state_space, initial_state, goal_state):
  frontier = []
  explored = []
  frontier.append(Node(initial_state, None, 0))

  while frontier:
    # Sort frontier after adding children
    frontier.sort(key=lambda node: node.path_cost)
    
    # Goal test at EXPANSION (pop from frontier first)
    node = frontier.pop(0)
    
    if node.state == goal_state:
      # Build and return solution
      solution = [node.state]
      trace_node = node
      while trace_node.parent is not None:
        solution.insert(0, trace_node.parent.state)
        trace_node = trace_node.parent
      return solution, node.path_cost
    
    explored.append(node.state)
    
    children = expandAndReturnChildren(state_space, node)
    for child in children:
      in_exp = child.state in [e for e in explored]
      # Check if child is in frontier with higher cost
      in_fr_higher = False
      for f in frontier:
        if f.state == child.state and f.path_cost > child.path_cost:
          frontier.remove(f)
          in_fr_higher = True
          break
      in_fr_exact = child.state in [f.state for f in frontier]
      if not in_exp and not in_fr_exact:
        frontier.append(child)

  return None, float('inf')

initial_state = "Arad"
goal_state    = "Bucharest"

state_space = [
  ['Arad',            'Zerind',           75],
  ['Arad',            'Sibiu',            140],
  ['Arad',            'Timisoara',        118],
  ['Zerind',          'Oradea',           71],
  ['Zerind',          'Sibiu',            151],
  ['Oradea',          'Neamt',            380],
  ['Timisoara',       'Lugoj',            111],
  ['Sibiu',           'Fagaras',          99],
  ['Sibiu',           'RimnicuVilcea',    80],
  ['Lugoj',           'Mehadia',          70],
  ['Mehadia',         'Drobeta',          75],
  ['Mehadia',         'Craiova',          120],
  ['Drobeta',         'Craiova',          120],
  ['Craiova',         'RimnicuVilcea',    146],
  ['Craiova',         'Pitesti',          138],
  ['RimnicuVilcea',   'Craiova',          146],
  ['RimnicuVilcea',   'Pitesti',          97],
  ['Fagaras',         'Bucharest',        211],
  ['Fagaras',         'Pitesti',          100],
  ['Pitesti',         'Bucharest',        101],
  ['Bucharest',       'Giurgiu',          90],
  ['Bucharest',       'Urziceni',         85],
  ['Giurgiu',         'Craiova',          120],
  ['Urziceni',        'Hirsova',          98],
  ['Urziceni',        'Vaslui',           142],
  ['Hirsova',         'Eforie',           86],
  ['Vaslui',          'Iasi',             92],
  ['Iasi',            'Neamt',            87],
]

if __name__ == '__main__':
  solution, cost = ucs(state_space, initial_state, goal_state)
  if solution:
    print('Solution: ' + str(solution))
    print('Total Cost: ' + str(cost))
  else:
    print('No solution found')
