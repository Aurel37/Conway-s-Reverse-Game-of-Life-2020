import numpy as np
import random as rd


class grid:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.mat = np.zeros((n, p))

    def setCell(self, i, j):
        """Useful to init the grid"""
        if (0 <= i < self.n and 0 <= j < self.p):
            self.mat[i, j] = 1

    def setRandom(self):
        for i in range(self.n):
            for j in range(self.p):
                if (rd.random() > 0.6):
                    self.mat[i, j] = 1

    def setState(self, i, j):
        """Considering a position in the grid
           Update the position"""
        cases = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]
        livingCell = 0
        if (0 <= i < self.n and 0 <= j < self.p):
            for case in cases:
                try:
                    livingCell += self.mat[i + case[0], j + case[1]]
                except:
                    pass 
            if (livingCell > 3 or livingCell < 2):
                self.mat[i, j] = 0
            elif (self.mat[i, j] == 0 and livingCell == 3):
                self.mat[i, j] = 1

    def runGame(self, Time):
        for t in range(Time):
            for i in range(self.n):
                for j in range(self.p):
                    self.setState(i, j)
            print(self.mat, end='\r')
