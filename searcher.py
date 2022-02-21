##
# searcher.py (Final project)
# classes for objects that perform state-space search on Eight Puzzle
# name:
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
import random

from state import *
 

class Searcher:
    # Add your Searcher method definitions here.
    def __init__(self, depth_limit):
        """ 
        constructs a new Searcher object by initializing the following 
        attributes states for the Searcher‘s list of untested states
        num_tested that will keep track of how many states the Searcher tests
        depth_limit that specifies how deep in the state-space search tree 
        the Searcher will go
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def add_state(self, new_state):
        """ takes a single State object called new_state and adds it 
        to the Searcher‘s list of untested states"""
        self.states.append(new_state)

    def should_add(self, state):
        """takes a State object called state and returns True 
        if the called Searcher should add state to its list of untested 
        states, and False otherwise.""" 
        if self.depth_limit != -1 and self.depth_limit < state.num_moves:
            return False
        elif state.creates_cycle():
            return False
        else:
            return True

    def add_states(self, new_states):
        """takes a list State objects called new_states, and that processes 
        the elements of new_states one at a time as follows"""
        for state in new_states:
            if self.should_add(state):
                self.add_state(state)

    def next_state(self):
        """ chooses the next state to be tested from the list of
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    def find_solution(self, init_state):
        """performs a full state-space search that begins at the specified 
        initial state init_state and ends when the goal state is found or when
        the Searcher runs out of untested states."""
        self.add_state(init_state)
        while self.states:
            curr_state = self.next_state()
            self.num_tested += 1
            if curr_state.is_goal() == True:
                return curr_state
            else:
                self.add_states(curr_state.generate_successors())
        return None

    def __repr__(self):

        """ returns a string representation of the Searcher object

            referred to by self.

        """

        # You should *NOT* change this method.

        s = type(self).__name__ + ': '

        s += str(len(self.states)) + ' untested, '

        s += str(self.num_tested) + ' tested, '

        if self.depth_limit == -1:

            s += 'no depth limit'

        else:

            s += 'depth limit = ' + str(self.depth_limit)

        return s



# Add your BFSeacher and DFSearcher class definitions below.

class BFSearcher(Searcher):   
    
    def next_state(self):
        """obtain the next state to be tested,"""
        for s in self.states:
            self.states.remove(s)
            return s

class DFSearcher(Searcher):      

    def next_state(self):
        """obtain the next state to be tested"""
        s = self.states[-1]
        self.states.remove(self.states[-1])
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0
### Add your other heuristic functions here. ###





class GreedySearcher(Searcher):

    """ class for greedy searcher in eightpuzzle
    """



    ### Add your GreedySearcher method definitions here. ###



    def __init__(self, heuristic):
        """"constructs a new GreedySearcher object"""

        self.heuristic = heuristic

        super().__init__(-1)

        

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

     
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
        

    def add_state(self, state):
        """overrides (i.e., replaces) 
        the add_state method that is inherited
        from Searcher."""
        self.states.append([self.priority(state), state])

    
    def next_state(self):
        """overrides (i.e., replaces) the 
        next_state method that is inherited
        from Searcher. """

        a = max(self.states)
        self.states.remove(a)
        return a[-1]

def h1(state):
    return state.board.num_misplaced()

### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    """A* is an informed search algorithm 
    that assigns a priority to each state based on
    a heuristic function, 
    and that selects the next state based on 
    those priorities. 
    However, when A* assigns a priority to a state,
    it also takes into account the cost 
    that has already been expended
    to get to that state 
    (i.e. the number of moves to that state)."""

    def __init__(self, heuristic):
        super().__init__(heuristic)
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        return super().__repr__()
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)

def h2(state):
    """takes a single State object and returns an integer but uses the 
    sum of col and row misplaced instead of just nummisplaced functoin
    """
    return state.board.numMisplacedButCooler()





     

