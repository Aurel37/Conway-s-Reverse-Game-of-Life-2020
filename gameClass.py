import numpy as np
import random as rd
from time import sleep
import matplotlib.pyplot as plt



class grid:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.mat = np.zeros((n, p))
        self.col = ['red', 'green']

    def initialization(self, matrix):
        if matrix.shape() == [self.n, self.p]:
            self.mat = np.copy(matrix)

    def setCell(self, i, j):
        """Useful to init the grid"""
        if (0 <= i < self.n and 0 <= j < self.p):
            self.mat[i, j] = 1

    def setRandom(self):
        for i in range(self.n):
            for j in range(self.p):
                if (rd.random() > 0.6):
                    self.mat[i, j] = 1

    def setState(self, i, j, mat):
        """Considering a position in the grid
           Update the position"""
        cases = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]
        livingCell = 0
        if (0 <= i < self.n and 0 <= j < self.p):
            for case in cases:
                try:
                    livingCell += mat[i + case[0], j + case[1]]
                except:
                    pass 
            if (livingCell > 3 or livingCell < 2):
                self.mat[i, j] = 0
            elif (mat[i, j] == 0 and livingCell == 3):
                self.mat[i, j] = 1
    


    def oneStep(self):
        mat = self.mat.copy()
        for i in range(self.n):
            for j in range(self.p):
                self.setState(i, j, mat)
    
    def printGrid(self, ax):
        for i in range(self.n):
            for j in  range(self.p):
                a_circle = plt.Circle((i + 0.5, j + 0.5), .45, color = self.col[int(self.mat[i, j])])
                ax.add_artist(a_circle)


    def showGame(self, time):

        fig, ax = plt.subplots()
        ax.set(xlim=(0, self.n), ylim = (0, self.p))
        self.printGrid(ax)
        for _ in range(time):
            plt.pause(0.5)
            self.oneStep()
            self.printGrid(ax)


    def game(self, time):
        for _ in range(time):
            self.oneStep()
            print(self.mat)



test = grid(5, 5)

test.setRandom()
test.showGame(10)