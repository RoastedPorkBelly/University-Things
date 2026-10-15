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
    elif n == node.state: children.append(Node(m, node))
  return children

def ucs(state_space, initial_state, goal_state):
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

initial_state = "Kelana Jaya"
goal_state    = "KLCC"

state_space = [
  ['Gombak',           'Taman Melati',     1.2],
  ['Taman Melati',     'Wangsa Maju',      1.5],
  ['Wangsa Maju',      'Sri Rampai',       1.8],
  ['Sri Rampai',       'Setiawangsa',      2.1],
  ['Setiawangsa',      'Jelatek',          1.3],
  ['Jelatek',          'Ampang Park',      2.4],
  ['Ampang Park',      'KLCC',             0.8],
  ['KLCC',             'Kampung Baru',     1.1],
  ['Kampung Baru',     'Dang Wangi',       0.9],
  ['Dang Wangi',       'Masjid Jamek',     0.7],
  ['Masjid Jamek',     'Pasar Seni',       0.8],
  ['Pasar Seni',       'KL Sentral',       1.2],
  ['KL Sentral',       'Bangsar',          2.0],
  ['Bangsar',          'Abdullah Hukum',   1.5],
  ['Abdullah Hukum',   'Kerinchi',         1.8],
  ['Kerinchi',         'Universiti',       1.6],
  ['Universiti',       'Taman Jaya',       1.4],
  ['Taman Jaya',       'Asia Jaya',        1.2],
  ['Asia Jaya',        'Taman Paramount',  1.5],
  ['Taman Paramount',  'Taman Bahagia',    1.3],
  ['Taman Bahagia',    'Kelana Jaya',      1.7],
]

if __name__ == '__main__':
  print('Solution: ' + str(bfs(state_space, initial_state, goal_state)))