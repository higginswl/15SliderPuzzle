from FifteenPuzzle import *
from PriorityQueue import *

from time import *

#Manhattan
#class MyFifteenPuzzle(FifteenPuzzle):
#	def __init__(self, initial=None):
#		FifteenPuzzle.__init__(self, initial)
#	
#	def heuristic(self, state):
#		"""A heuristic to aid in searching the solution space."""
#               d = 0
#               for i in range(4):
#                       for j in range(4):
#                               s = state[i][j]
#                               if s > 0:
#                                       d += abs(i - s/4) + abs(j - s%4)
#               return d

#PatternDatabase
class MyFifteenPuzzle(FifteenPuzzle):
       def __init__(self, initial=None):
               FifteenPuzzle.__init__(self, initial)

               # Build the pattern database with two groups
               #
               #   1 1 2   4 4 2
               # 1 1 1 2 3 3 4 2
               # 1 1 1 2 3 3 2 2
	           # 2 2 2 2 1 1 1 1
               start = time()
               self._lookups = []


	       self._groups = [ [0,12,13,14,15], [0,3,7,11,10], [0,4,5,8,9], [0,1,2,6] ] #FRINGECORNER

               for i in range(len(self._groups)):
                       print 'Building pattern database', i
                       v = self._groups[i]

                       queue = PriorityQueue()
                       distances = {}
                       representatives = {}

                       state = self.getGoal()
                       projectedState = self.projection(self.getGoal(), v)

                       queue.push(projectedState, 0)
                       representatives[projectedState] = state
                       distances[projectedState] = 0

                       count = 0
                       while len(queue) > 0:
                               projectedState = queue.pop()
                               state = representatives[projectedState]
                               dist = distances[projectedState]

                               count += 1
                               if count % 10000 == 0:
                                       print count, len(distances), len(queue), dist, time()-start

                               for a in self.actions(state):
                                       newState = self.result(state, a)
                                       newProjectedState = self.projection(newState, v)
                                       if self.tileMoved(state,a) in v:
                                               newDist = dist + 1
                                       else:
                                               newDist = dist

                                       if not distances.has_key(newProjectedState) or newDist < distances[newProjectedState]:
                                               queue.push(newProjectedState, newDist)
                                               distances[newProjectedState] = newDist
                                               representatives[newProjectedState] = newState

                       self._lookups.append(distances)

       def projection(self, state, group):
               a = tuple([tuple([x if x in group else -1 for x in y]) for y in state])

               return a

       def heuristic(self, state):
               h = 0
               for i in range(len(self._groups)):
                       h += self._lookups[i][self.projection(state,self._groups[i])]
               return h

