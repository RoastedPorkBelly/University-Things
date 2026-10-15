initial_state = "Arad"
goal_state    = "Bucharest"

state_space = [
  ['Arad',           'Zerind',          75],
  ['Arad',           'Sibiu',          140],
  ['Arad',           'Timisoara',      118],
  ['Zerind',         'Oradea',          71],
  ['Oradea',         'Sibiu',          151],
  ['Sibiu',          'Fagaras',         99],
  ['Sibiu',          'Rimnicu Vilcea',  80],
  ['Timisoara',      'Lugoj',          111],
  ['Lugoj',          'Mehadia',         70],
  ['Mehadia',        'Drobeta',         75],
  ['Drobeta',        'Craiova',        120],
  ['Craiova',        'Rimnicu Vilcea', 146],
  ['Craiova',        'Pitesti',        138],
  ['Rimnicu Vilcea', 'Pitesti',         97],
  ['Fagaras',        'Bucharest',      211],
  ['Pitesti',        'Bucharest',      101],
  ['Bucharest',      'Giurgiu',         90],
  ['Bucharest',      'Urziceni',        85],
  ['Urziceni',       'Hirsova',         98],
  ['Urziceni',       'Vaslui',         142],
  ['Hirsova',        'Eforie',          86],
  ['Vaslui',         'Iasi',            92],
  ['Iasi',           'Neamt',           87],
]

## Node in the search tree
# We can use a class to represent each node in the search tree. 
# The important information for each node includes the state and the parent of the node.
class Node:
  def __init__(self, state=None, parent=None):
    self.state = state
    self.parent = parent

# updated function with the implementation of node as a class
def expandAndReturnChildren(state_space, node):
  children = []
  for [m,n,c] in state_space:
    if m == node.state:
      childnode = Node(n, node)
      children.append(childnode)
    elif n == node.state:
      childnode = Node(m, node)
      children.append(childnode)
  return children

def bfs(state_space, initial_state, goal_state):
  frontier = []
  explored = []
  frontier.append(Node(initial_state, None))