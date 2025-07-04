# Libraries for Math Problem Generator
import random
import math
import numpy
import matplotlib.pyplot as plt

class Problem:
    def __init__(self, randomSeed=random.randint(-999999, 999999)):
        """
        init a problem class for better usage
        parameters : randomSeed (int) -> seed for random library
        """
        self.seed = randomSeed
        random.seed(self.seed)
        self.problem = None
    
    def linear_algebra(self, variablenum=(3,4), equationsAnswersRange=(-300,300), coefficientRange=(1,20)) -> None:
        """
        function for generate linear algebra problem
        parameters : variablenums (trple) -> how much variable in the equations do you want.
                    equationsAnswerRange (tuple) -> what are the answer range do you want.
                    coefficientRange (tuple) -> what are the range of coefficient do you want.
        """
        variableNum = random.randint(*variablenum)
        d = {i:chr(i+96) for i in range(1,27)} # variable mapping d[0] is number in range 1-26 and d[1] is alphabet a-z
        equationsAnswers = [random.randint(*equationsAnswersRange) for i in range(variableNum)]
        variable = []
        for i in range(variableNum):
            coefficient = [[random.randint(*coefficientRange), random.randint(0, 1)] for _ in range(variableNum)]
            for j in coefficient:
                if j[1] == 1:
                    coefficient[coefficient.index(j)] = j[0]*-1
                else:
                    coefficient[coefficient.index(j)] = j[0]
            if variableNum <= 3:
                variable.append([coefficient, d[i+24]])
            else:
                variable.append([coefficient, d[i+1]])
        equations = []
        for i in range(variableNum):
            equation = ""
            for j in range(variableNum):
                if variable[i][0][j] > 0 and j != 0:
                    equation += (f"+{variable[i][0][j]}{variable[j][1]}")
                else:
                    equation += (f"{variable[i][0][j]}{variable[j][1]}")
                if j+1 == variableNum:
                    equation += f" = {equationsAnswers[i]}"
            equations.append(equation)
        self.problem = equations
        
        
        
if __name__ == "__main__":
    problemOne = Problem()
    problemOne.linear_algebra()
    print(problemOne.problem)