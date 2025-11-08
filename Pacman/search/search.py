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
import time
import util
from util import *

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        util.raiseNotDefined()

    def isGoalState(self, state):
        util.raiseNotDefined()

    def getSuccessors(self, state):
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    start_time = time.time()
    currState = problem.getStartState()
    currPath = []
    if problem.isGoalState(currState):
        print(f"DFS took {time.time() - start_time:.4f} seconds")
        return currPath
    frontier = Stack()
    frontier.push((currState, currPath))
    explored = set()
    while not frontier.isEmpty():
        currState, currPath = frontier.pop()
        if problem.isGoalState(currState):
            print(f"DFS took {time.time() - start_time:.4f} seconds")
            return currPath
        if currState not in explored:
            explored.add(currState)
            for nextState, action, _ in problem.getSuccessors(currState):
                if nextState not in explored:
                    frontier.push((nextState, currPath + [action]))
    print(f"DFS took {time.time() - start_time:.4f} seconds")
    return []

def breadthFirstSearch(problem):
    start_time = time.time()
    currState = problem.getStartState()
    currPath = []
    if problem.isGoalState(currState):
        print(f"BFS took {time.time() - start_time:.4f} seconds")
        return currPath
    frontier = Queue()
    frontier.push((currState, currPath))
    explored = set()
    while not frontier.isEmpty():
        currState, currPath = frontier.pop()
        if problem.isGoalState(currState):
            print(f"BFS took {time.time() - start_time:.4f} seconds")
            return currPath
        if currState not in explored:
            explored.add(currState)
            for nextState, action, _ in problem.getSuccessors(currState):
                if nextState not in explored:
                    frontier.push((nextState, currPath + [action]))
    print(f"BFS took {time.time() - start_time:.4f} seconds")
    return []

def uniformCostSearch(problem):
    start_time = time.time()
    currState = problem.getStartState()
    frontier = PriorityQueue()
    frontier.push((currState, [], 0), 0)
    explored = {}
    while not frontier.isEmpty():
        currState, currPath, costSoFar = frontier.pop()
        if problem.isGoalState(currState):
            print(f"UCS took {time.time() - start_time:.4f} seconds")
            return currPath
        if currState not in explored or explored[currState] > costSoFar:
            explored[currState] = costSoFar
            for nextState, action, cost in problem.getSuccessors(currState):
                newCost = costSoFar + cost
                frontier.push((nextState, currPath + [action], newCost), newCost)
    print(f"UCS took {time.time() - start_time:.4f} seconds")
    return []

def nullHeuristic(state, problem=None):
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    start_time = time.time()
    currState = problem.getStartState()
    frontier = PriorityQueue()
    frontier.push((currState, [], 0), heuristic(currState, problem))
    explored = {}
    while not frontier.isEmpty():
        currState, currPath, costSoFar = frontier.pop()
        if problem.isGoalState(currState):
            print(f"A* took {time.time() - start_time:.4f} seconds")
            return currPath
        if currState not in explored or explored[currState] > costSoFar:
            explored[currState] = costSoFar
            for nextState, action, cost in problem.getSuccessors(currState):
                newCost = costSoFar + cost
                priority = newCost + heuristic(nextState, problem)
                frontier.push((nextState, currPath + [action], newCost), priority)
    print(f"A* took {time.time() - start_time:.4f} seconds")
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch