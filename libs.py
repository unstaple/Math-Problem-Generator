# Libraries for Math Problem Generator
import random
import math
import numpy as np
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
        self.answers = None
    
    def linear_algebra(self, answers=None, variablenum=random.randint(3,4), equationsAnswersRange=[(-10,-1),(1,10)], difficulty=random.randint(4,6)) -> None:
        """
        function for generate linear algebra problem
        parameters :    answers (list, optional): A predefined list of answers for the variables.
                        variablenum (int): The number of variables (used if 'answers' is not provided).
                        equationsAnswerRange (tuple): The range for random answers.
                        difficulty (int): The number of random row operations to perform.
        """
        if answers is not None:
            variablenum = len(answers)
            equationsAnswers = np.array(answers, dtype=float)
        else:
            equationsAnswers = []
            for _ in range(variablenum):
                positive = random.randint(0, 1)
                if positive:
                    equationsAnswers.append(random.randint(*equationsAnswersRange[1]))
                else:
                    equationsAnswers.append(random.randint(*equationsAnswersRange[0]))
            equationsAnswers = np.array(equationsAnswers, dtype=float)
            
        self.answers = equationsAnswers.copy() # Set self.answers to the correct solutions
        baseMatrix = np.identity(variablenum, dtype=float) # generate idendity matrix
        
        for i in range(baseMatrix.shape[0]): # loop and plus every row with each row to make every entries become 1 to avoid entries stuck at 0
            temp = [k for k in range(baseMatrix.shape[0])] # create temp list
            temp.remove(i)
            for j in temp:
                baseMatrix[j] = baseMatrix[j]+baseMatrix[i]
                equationsAnswers[j] = equationsAnswers[j]+equationsAnswers[i]
                
        for _ in range(difficulty):
            row1 = random.randint(0, variablenum - 1)
            row2 = random.randint(0, variablenum - 1)
            
            # Ensure row1 and row2 are different for addition/subtraction
            while row1 == row2:
                row2 = random.randint(0, variablenum - 1)

            operation = random.choice(['add', 'multiply', 'divide'])

            if operation == 'add':
                baseMatrix[row1] += baseMatrix[row2]
                equationsAnswers[row1] += equationsAnswers[row2]
            elif operation == 'multiply':
                multiplier = random.randint(2, 4)
                baseMatrix[row1] *= multiplier
                equationsAnswers[row1] *= multiplier
            else: # divide
                divider = random.randint(2, 4)
                baseMatrix[row1] /= divider
                equationsAnswers[row1] /= divider
                
        d = {i:chr(i+97) for i in range(26)} # variable mapping d[0] is number in range 1-26 and d[1] is alphabet a-z
        variable = [d[i] for i in range(variablenum)]
        
        equations = []
        for i in range(baseMatrix.shape[0]):
            equation = ""
            for j in range(baseMatrix.shape[1]):
                coeff = baseMatrix[i][j]
                # Skip terms with a zero coefficient
                if coeff == 0:
                    continue
                
                # Format coefficient and sign
                if len(equation) > 0:
                    sign = " + " if coeff > 0 else " - "
                    equation += sign
                elif coeff < 0:
                     equation += "-"
                
                coeff = abs(coeff)

                # Add coefficient if it's not 1
                if coeff == 1:
                    equation += f"{variable[j]}"
                else:
                    # Format floating point numbers
                    formatted_coeff = f"{coeff:.2f}".rstrip('0').rstrip('.')
                    equation += f"{formatted_coeff}{variable[j]}"

            equation += f" = {equationsAnswers[i]:.2f}".rstrip('0').rstrip('.')
            equations.append(equation)
            
        self.problem = equations
        
        
             
if __name__ == "__main__":
    problemOne = Problem()
    problemOne.linear_algebra()
    for i in problemOne.problem:
        print(i)
    print(problemOne.answers)