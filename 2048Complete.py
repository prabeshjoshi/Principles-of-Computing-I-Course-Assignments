"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def ini_cell(direction,width,height):
    """ returns first cells in grid to process move method for given direction"""
    if direction == UP:
              start_cell = [(0,i) for i in range(width)]   
    elif direction == RIGHT:
              start_cell = [(i,width-1) for i in range(height)]    
    elif direction == DOWN:
              start_cell = [(height-1,i) for i in range(width)]
    elif direction == LEFT:
               start_cell = [(i,0) for i in range(height-1,-1,-1)]
    return start_cell

def traverse_grid(grid,start_cell, direction):
    """ returns a list of elements in a grid given start_cell and direction"""
    height = len(grid)
    width = len(grid[0])
    numsteps = abs(OFFSETS[direction][0])*height + abs(OFFSETS[direction][1])*abs(OFFSETS[direction][1])*width
    out = []
    direc = OFFSETS[direction]
    for step in range(numsteps):
       
        
        row = start_cell[0] + step* direc[0]
        col = start_cell[1] +step*direc[1]
        if row < height and col < width:
            
            out.append(grid[row][col])
    return out

def list_non_zeros(line):
        """generates a list of non zero elements in the list line"""
        list_non_0 = []
        for item in range(len(line)):
            if line[item] != 0:
                list_non_0.append(line[item])
        return list_non_0    

def locate_zeros(grid):
    """ returns a list of positions with no tile"""
    position = []    
    for jindex  in range(len(grid)):
        for index in range(len(grid[jindex])):
            if grid[jindex][index] == 0:
                position.append((jindex,index)) 
    return position

def list_of_pairs(lst):
        """generates a list of all posible indices for first part of pair"""
        pairs_index = []
        for item in range(len(lst)):
            if item+1 <= len(lst) -1:
                if lst[item] == lst[item+1]:
                    pairs_index.append(item)
    
        for item in range(len(pairs_index)):
            if item+1 <= len(pairs_index) -1:
                if pairs_index[item] +1 == pairs_index[item+1]:
                    del pairs_index[item+1]
                    
        return pairs_index

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    result = []
    result_list = []

    for item in range(len(line)):
        result.append(0)
        

    for item in range(len(list_non_zeros(line))):
        result[item] = list_non_zeros(line)[item]

    result_copy = result
    for item in list_of_pairs(result_copy):
        result[item] *= 2
        result[item+1] = 0
    
    for item in range(len(line)):
        result_list.append(0)
        
    
    
    for item in range(len(list_non_zeros(result))):
        result_list[item]=list_non_zeros(result)[item]

    return result_list

def reposition(line,grid, start, direction) :
    """ repositions a merged line into its original place"""
    height = len(grid)
    width = len(grid[0])
    numsteps = abs(OFFSETS[direction][0])*height + abs(OFFSETS[direction][1])*abs(OFFSETS[direction][1])*width
    offs = OFFSETS[direction]
    linepos = 0
    st0 = start[0]
    st1 = start[1]
    for _ in range(numsteps):
        grid[st0][st1] = line[linepos]
        st0 += offs[0]
        st1 += offs[1]
        linepos += 1


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid = [[0 for _ in range(grid_width)]
                              for _ in range(grid_height)]
        self._height = grid_height
        self._width = grid_width
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
       # replace with your code
        self._grid = [[0 for _ in range(self._width)]
                              for _ in range(self._height)]
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        out = ""
        for one_row in self._grid:
            out+= str(one_row)+ "\n"
        return out    
            
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        height=self._height
        width=self._width
        # replace with your code
        
        start = ini_cell(direction,width,height)
        
        change= []
        for startpos in start:
            
            temp1 = traverse_grid(self._grid,startpos, direction)
            temp = merge(temp1)
            reposition(temp,self._grid, startpos, direction)
            change.append(temp1==temp)

        if False in change:
            self.new_tile()
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        if not len(locate_zeros(self._grid)) == 0:
            choices_list = [2,2,2,2,2,2,2,2,2,4]
            zero_pos1 = random.choice(locate_zeros(self._grid))
            self.set_tile(zero_pos1[0],zero_pos1[1],random.choice(choices_list))
            print locate_zeros(self._grid)      
            
        else:
            pass
            
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]
       
  

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
