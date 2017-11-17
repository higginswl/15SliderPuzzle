# 15SliderPuzzle
My agent uses a pattern database method to solve a Sliding Fifteen Puzzle

My agent use Breadth First Search through the possible moves and assigns a heuristic value to each move based on its favorability.

I initially implemented a manhattan distance heuristic which counted the sum of the distances between each tiles space and where it should be. I improved the heuristic by changing it to a pattern database with two groups. 

               #   1 1 2
               # 1 1 1 2
               # 1 1 1 2
               # 2 2 2 2
               start = time()
               self._lookups = []

               self._groups = [ [0,1,2,4,5,6,8,9,10], [0,3,7,11,12,13,14,15] ]
               
This found a solution to the puzzle more quickly. 
