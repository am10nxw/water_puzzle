# water_puzzle

This is the final project I worked on in my CS2050 course. This shows the experience I gained in this class.
# Assignment 6
©Steve Geinitz and others

For inspiration: https://youtu.be/BVtQNK_ZUJg

Solve the “water puzzle” using a
Graph and BFS.

Instead of only a 3-gallon container and 5-gallon container, we will solve
it for any two size containers!

Example for containers with capacity 3 and 4, and a target amount of 2:

We will keep track of how much water is in the containers at any time using a Python 2-
tuple; e.g. if the current state is: (0, 4) then that means that Container A currently has 0
gallons and Container B currently has 4 gallons.

Our program should tell us give us the list of states, which will tell us:
- state = (0, 0) Start - the starting state.
- state = (3,0) Fill Container A
- state = (0, 3) Pour contents of Container A into Container B
- state = (3,3) Fill Container A
- state = (2, 4) Pour from Container A into Container B until B is full
- Done! Since Container A has exactly the desired amount in itMay 6,2021 CS 2050: Lecture 29

Requirements:
- findSolution(a, b, goal_amount) - this function (along with any
helper functions it calls) will perform the tasks of
- building the graph as needed
- performing BFS
- navigating result to return solution as a Python list of tuples
- getEligibleStates(a, b, curr_state) - return a list of tuples
that are possible states that be reached from the current state
(denoted by curr_state)