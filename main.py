from graph import Graph
from queue2050 import Queue
import math


def findSolution(a, b, goal_amount):
    """ Creates a graph, uses bfs to find distance, and then returns the
    shortest path to a goal_amount as a list. """
    if validJug(a, b, goal_amount):
        g = buildGraph(a, b)
        bfs(g)
    else:
        return 'This scenario is not possible'
    return path2root(g, goal_amount)


def getEligibleStates(a, b, curr_state):
    """ Returns all the possible state that the jars can be changed to in
    one move. """
    current = []
    if validJug(a, b, curr_state):
        g = buildGraph(a, b)
        v = g.getVertex(curr_state)
        if v is not None:
            for i in v.getConnections():
                current.append(i.getId())
        else:
            current = 'This scenario is not possible.'
    else:
        current = 'This scenario is not possible.'
    return current


def validJug(a, b, goal_amount):
    """ Checks if you can reach get to the goal_amount with the maximum jug
    amount. Also rules out some of the eligible states that won't work.
    Doesn't rule them all out."""
    valid = False
    if type(goal_amount) is int:
        if goal_amount > a and goal_amount > b:
            return valid
        if goal_amount % math.gcd(a, b) == 0:
            valid = True
    elif type(goal_amount) is tuple:
        a1 = goal_amount[0]
        a2 = goal_amount[1]
        if (a1 % math.gcd(a, b) == 0) and (a2 % math.gcd(a, b) == 0) and a1 \
                <= a and a2 <= b:
            valid = True
    return valid


def buildGraph(a, b):
    """ Creates a Graph with all possible vertices and edges. Required
    arguments are the maximum amount that jug a and jug b can hold as an
    integer."""
    state = (0, 0)
    q = Queue()
    g = Graph()
    g.addVertex(state)
    q.enqueue(state)
    while q.size() > 0:
        state = q.dequeue()
        x = state[0]
        y = state[1]
        # Empty jug a
        if x > 0:
            if g.getVertex((0, y)):
                g.addEdge(state, (0, y))
            else:
                q.enqueue((0, y))
                g.addEdge(state, (0, y))
        # Empty jug b
        if y > 0:
            if g.getVertex((x, 0)):
                g.addEdge(state, (x, 0))
            else:
                q.enqueue((x, 0))
                g.addEdge(state, (x, 0))
        # Fill jug a
        if x < a:
            if g.getVertex((a, y)):
                g.addEdge(state, (a, y))
            else:
                q.enqueue((a, y))
                g.addEdge(state, (a, y))
        # Fill jug b
        if y < b:
            if g.getVertex((x, b)):
                g.addEdge(state, (x, b))
            else:
                q.enqueue((x, b))
                g.addEdge(state, (x, b))
        # Poor jug b into jug a
        if x < a and y > 0:
            tx = x
            ty = y
            while tx < a and ty > 0:
                tx += 1
                ty -= 1
            if g.getVertex((tx, ty)):
                g.addEdge(state, (tx, ty))
            else:
                q.enqueue((tx, ty))
                g.addEdge(state, (tx, ty))
        # Poor jug a into jug b
        if y < b and x > 0:
            tx = x
            ty = y
            while ty < b and tx > 0:
                tx -= 1
                ty += 1
            if g.getVertex((tx, ty)):
                g.addEdge(state, (tx, ty))
            else:
                q.enqueue((tx, ty))
                g.addEdge(state, (tx, ty))
    return g


def bfs(g, start=(0, 0)):
    """ Uses breadth first search to assign predecessors and get the
    distance from  the provided states."""
    start = g.getVertex(start)
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def path2root(g, goal_amount):
    """ Returns the shortest path to the goal_amount as a list. """
    min_dis = len(g.getVertices())
    for i in g.getVertices():
        z = i[0]
        y = i[1]
        if (z == goal_amount or y == goal_amount) and g.getVertex(
                i).getDistance() < min_dis:
            x = g.getVertex(i)
            min_dis = g.getVertex(i).getDistance()
    path = []
    while x.getPred():
        path.insert(0, x.getId())
        x = x.getPred()
    path.insert(0, x.getId())
    return path


bg = buildGraph(1, 98)
print(bg.getVertices())
print(findSolution(1, 98, 2))
print(getEligibleStates(1, 98, (1, 11)))
