class Maze:
    def __init__(self, m: int, n : int) -> None:
        ## DO NOT MODIFY THIS FUNCTION, initialises the Maze/ Grid
        ## We initialise the list with all 0s, as initially all cells are vacant
        self.grid_representation = []
        for row in range(m):
            grid_row = []
            for column in range(n):
                grid_row.append(0)
            self.grid_representation.append(grid_row)
    
    def add_ghost(self, x : int, y: int) -> None:
        # IMPLEMENT YOUR FUNCTION HERE, adds ghost at specified coordinates
        self.grid_representation[x][y]=1
        
    def remove_ghost(self, x : int, y: int) -> None:
        # IMPLEMENT YOUR FUNCTION HERE, removes ghost from specified coordinates
        self.grid_representation[x][y]=0
        
        
    def is_ghost(self, x : int, y: int) -> bool:
        # IMPLEMENT YOUR FUNCTION HERE, checks if ghost is present
        if self.grid_representation[x][y]==1:
            return True
        else :
            return False
            
            
    def print_grid(self) -> None:
        # IMPLEMENT YOUR FUNCTION HERE, prints how the grid looks
        for i in range(len(self.grid_representation)):
            for j in range(len(self.grid_representation[0])):
                print(self.grid_representation[i][j], end=" ")
            print()
           
        