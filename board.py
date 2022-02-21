#
# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1
        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for i in range(len(digitstr)):
            self.tiles[i//3][i%3] = digitstr[i]
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] == '0':
                    self.blank_r = i
                    self.blank_c = j
    ### Add your other method definitions below. ###
    def __repr__(self):
        """ returns a string representation of a Board object.
        """
        #'1 4 2 \n3 5 8 \n6 _ 7 \n'
        storestr = ''
        for i in range(3):
            for j in range(3):
                storestr += str(self.tiles[i][j]) + ' '
            storestr += '\n'
        storestr = storestr.replace('0','_')
        return storestr
    
    def move_blank(self, direction):
        """input a string direction that specifies the direction in which 
        the blank should move, and that attempts to modify the contents of
        the called Board object accordingly
        """
        i, j = self.blank_r, self.blank_c  
        if direction == "up":
            if self.blank_r == 0:
                return False
            self.tiles[i][j], self.tiles[i-1][j] = self.tiles[i-1][j], self.tiles[i][j]
            self.blank_r -= 1
            return True
        elif direction == "down":
            if self.blank_r == 2:
                return False
            self.tiles[i][j], self.tiles[i+1][j] = self.tiles[i+1][j], self.tiles[i][j]
            self.blank_r += 1
            return True
        elif direction == "right":
            if self.blank_c == 2:
                return False
            self.tiles[i][j], self.tiles[i][j+1] = self.tiles[i][j+1], self.tiles[i][j]
            self.blank_c += 1
            return True
        elif direction == "left":
            if self.blank_c == 0:
                return False
            self.tiles[i][j], self.tiles[i][j-1] = self.tiles[i][j-1], self.tiles[i][j]
            self.blank_c -= 1
            return True
        else:
            return False
        
    def digit_string(self):
        """that creates and returns a string of digits that corresponds to 
        the current contents of the called Board object’s tiles attribute
        """
        myStr = ''
        for i in range(3):
            for j in range(3):
                myStr += str(self.tiles[i][j])
        myStr = myStr.replace('_','0')
        return myStr
    def copy(self):
        """returns a newly-constructed Board object that is a deep copy of 
        the called object (i.e., of the object represented by self).
        """
        digitstr = self.digit_string()
        return Board(str(digitstr))
    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object 
        that are not where they should be in the goal state
        """
        counter = 0
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] != GOAL_TILES[i][j] and self.tiles[i][j] != '0':
                    counter += 1
        return counter
    
    def __eq__(self, other):
        """ that can be called when the == operator is used to compare 
        two Board objects. The method should return True if the called 
        object (self) and the argument (other) have the same values for 
        the tiles attribute, and False otherwise"""
        if self.tiles == other.tiles:
            return True
        else:
            return False
    def numMisplacedButCooler(self):
        board = []
        s = 0
        for j in range(9):
            board += self.digit_string()[j]
        for i in range(len(board)):
            goal_x, goal_y = int(i/3) , int(i%3)
            current_x, current_y = int(board[i])//3, int(board[i])%3
            s += abs(current_x - goal_x) + abs(current_y - goal_y)
        return s//2
    """def (self):
        "compare row and column to goal and calculate the number difference"
        numDiff = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] not in GOAL_TILES[r] and self.tiles[r][c] != 0:
                    numDiff += 1
                if self.tiles[r][c] not in GOAL_TILES[c][r] and self.tiles[r][c] != 0:
                    numDiff += 1
        return numDiff"""
