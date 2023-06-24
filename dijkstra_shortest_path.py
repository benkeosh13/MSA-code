import math
def dijkstra(graph,start):
  #initialize tentative and confirmed dictionaries
  tentative = {}
  confirmed = {}

  #add start node cost to confirmed dictionary
  confirmed[start] = 0

  #place the start nodes neighbors in the tentative dictinary
  for node,distance, in graph[start].items():
     tentative[node] = distance

  #set next to the node just added to confirmed
  next = start

  #while the tentative list dictionary still has nodes 
  while tentative:
     shortest_distance = math.inf
     #select the node from tghe tentative dictionary with the lowest cost
     for node, distance in tentative.items():
        #determine shortest distance node
        if distance <shortest_distance:
           shortest_distance=distance
           next = node

    #add lowest cost node to confirmed dictionary and update next
     confirmed[next] = shortest_distance
    #remove next node from tentative dictinary
     tentative.pop(next)

    #place next nodes neighbors on tentative list
     for node,distance in graph[next].items():
        cost = confirmed[next] + distance
        #if neighbor is not in tentative, add to tentative
        #if neighbor in tentative, update cost if neccesary
        #if neighbor in confirmed list then ignore
        if node in confirmed:
           continue
        elif (node in tentative) and (cost < tentative[node]):
           tentative[node] = cost
        elif node not in tentative:
           tentative[node] = cost
    
  return confirmed

def main():
   graph = {
      'A' : {'B':5, 'C':10},
      'B' : {'A' : 5, 'C' : 3, 'D' : 11},
      'C' : {'A' : 10, 'B' : 3 , 'D' : 2},
      'D' : {'B' : 11, 'C' : 2}
    }
   
   #chose a start node
   start_node = 'D'

   distances = dijkstra(graph, start_node)

   for node, distance in distances.items():
      print(f"{node} -> {distance}")
   
main()