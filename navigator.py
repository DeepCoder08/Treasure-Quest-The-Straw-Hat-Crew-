from __future__ import annotations
from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
       
        self.navigator_maze = grid.grid_representation
    def find_path(self, start , end ):
        # IMPLEMENT FUNCTION HERE
        Path_Stack= Stack()
        visited_cells= [[False for _ in range(len(self.navigator_maze[0]))] for _ in range(len(self.navigator_maze))]
        #list of visited cells
        visited_cells[start[0]][start[1]]= True
        
        # Possible movements: down, right, up, left
        pac_movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        Path_Stack.pushdown(start) #initaialise the path stack
        path_is_found=0
        
        
        
        while(Path_Stack):
            
            curr_pos = Path_Stack.top()  #got the current pos of pacman
            
            
            
            
            if(curr_pos == end):
                path_is_found=1
                return Path_Stack._Stacker
                
                #checks if pacman reached the end
            
            #checking the neighbourhood
            for move in pac_movements:
                new_x = curr_pos[0]+move[0]
                new_y = curr_pos[1]+move[1]
                
                if(0<=new_x < len(self.navigator_maze ) and 0<= new_y< len(self.navigator_maze[0]) and self.navigator_maze[new_x][new_y]==0  and visited_cells[new_x][new_y]== False):
                    Path_Stack.pushdown((new_x,new_y))
                    visited_cells[new_x][new_y]= True
                    break
                
                else:
                    Path_Stack.popup()
                    #Backstrack pacman if no valid moves are there
            
                    
                    
            
        
        if(path_is_found == 0):
            raise PathNotFoundException
             
         
        
        
