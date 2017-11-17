# 15SliderPuzzle
My agent uses a pattern database method to solve a Sliding Fifteen Puzzle

My agent use Breadth First Search through the possible moves and assigns a heuristic value to each move based on its favorability.

I initially implemented a manhattan distance heuristic which counted the sum of the distances between each tiles space and where it should be. I improved the heuristic by changing it to a pattern database with four groups. 

               #   4 4 2
               # 3 3 4 2
               # 3 3 2 2
               # 1 1 1 1
               start = time()
               self._lookups = []

               elf._groups = [ [0,12,13,14,15], [0,3,7,11,10], [0,4,5,8,9], [0,1,2,6] ] #FRINGECORNER
               
This found a solution to the puzzle more quickly. 
