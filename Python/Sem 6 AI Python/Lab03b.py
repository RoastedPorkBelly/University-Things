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
    frontier.sort(key=lambda node: node.path_cost)
    
    node = frontier.pop(0)
    
    if node.state == goal_state:
      solution = [node.state]
      trace_node = node
      while trace_node.parent is not None:
        solution.insert(0, trace_node.parent.state)
        trace_node = trace_node.parent
      return solution, node.path_cost
    
    explored.append(node.state)
    
    children = expandAndReturnChildren(state_space, node)
    for child in children:
      in_exp = child.state in explored
      for f in frontier:
        if f.state == child.state and f.path_cost > child.path_cost:
          frontier.remove(f)
          break
      in_fr = child.state in [f.state for f in frontier]
      if not in_exp and not in_fr:
        frontier.append(child)

  return None, float('inf')

initial_location = "Burger_Palace_Restaurant"
delivery_location = "Ocean_View_Apartments"

state_space = [
  ['Burger_Palace_Restaurant', 'Downtown_Plaza',      8],
  ['Burger_Palace_Restaurant', 'Market_District',     12],
  ['Downtown_Plaza',           'Central_Station',     9],
  ['Downtown_Plaza',           'Market_District',     11],
  ['Market_District',          'Harbor_Road',         13],
  ['Market_District',          'Central_Station',     10],
  ['Central_Station',          'Tech_Park',           7],
  ['Central_Station',          'Port_Area',           14],
  ['Central_Station',          'University_Zone',     11],
  ['Tech_Park',                'Ocean_View_Apartments', 6],
  ['Tech_Park',                'Port_Area',           16],
  ['Harbor_Road',              'Port_Area',           12],
  ['Harbor_Road',              'University_Zone',     10],
  ['Port_Area',                'Ocean_View_Apartments', 18],
  ['Port_Area',                'University_Zone',     15],
  ['University_Zone',          'Ocean_View_Apartments', 9],
]

if __name__ == '__main__':
  solution, total_cost = ucs(state_space, initial_location, delivery_location)
  
  if solution:
    print('Route:', ' -> '.join(solution))
    print('Total Cost:', total_cost)
    print('Number of Stops:', len(solution) - 1)
  else:
    print('No route found')