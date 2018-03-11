# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
"""
I have implemented my own generic methods for search, which accepts the Queuing strategy to follow, depending on the search in use.
"""
def aStarHeuristic(problem,heuristic,cost,node):
    return heuristic(node,problem)+cost

def addSuccessorsToFringe(problem,fringe,node,visited,algoType,heuristic):
    for successor in problem.getSuccessors(node[0]):
        if successor[0] not in visited:
            pathToSuccessor = list(node[1])
            pathToSuccessor.append(successor[1])
            if algoType==0:
                successor = (successor[0],pathToSuccessor,successor[2],node[3])
                fringe.push(successor)
            elif algoType==1:
                successor = (successor[0],pathToSuccessor,successor[2]+node[2],node[3])
                fringe.push(successor,successor[2])
            else:
                successor = (successor[0],pathToSuccessor,successor[2]+node[2],node[3])
                fringe.push(successor,aStarHeuristic(problem,heuristic,successor[2],successor[0]))

def mySearchMethod(problem,fringe,algoType=0,heuristic=nullHeuristic):
    startNode = problem.getStartState()
    visited = {}
    visited[startNode] = 1
    if hasattr(problem,'corners'):
        startNode = (startNode,())
    addSuccessorsToFringe(problem,fringe,(startNode,[],0,{}),visited,algoType,heuristic)

    while not fringe.isEmpty():
        currentNode = fringe.pop()
        if problem.isGoalState(currentNode[0])==True:
            return currentNode[1]
        if currentNode[0] not in visited:
            visited[currentNode[0]] = 1
            addSuccessorsToFringe(problem,fringe,currentNode,visited,algoType,heuristic)

    return []
""" 
My generic function ends here..
"""

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    return mySearchMethod(problem,util.Stack())

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    return mySearchMethod(problem,util.Queue())

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    return mySearchMethod(problem,util.PriorityQueue(),1)

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    return mySearchMethod(problem,util.PriorityQueue(),2,heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
