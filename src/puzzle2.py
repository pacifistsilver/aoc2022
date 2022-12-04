from collections import Counter
"""
A, X: ROCK 1 
B, Y: PAPER 2 
C, Z: SCISSORS 3

X = LOSE
Y = DRAW
Z = WIN

WIN: 6
LOSS: 0
DRAW: 3
Counter({'A X': 936, 'B X': 421, 'C X': 310, 'A Y': 295, 'B Y': 262, 'C Y': 127, 'A Z': 51, 'B Z': 50, 'C Z': 48})
"""

path = "./inputs/puzzle2input.txt"
with open(path, 'r') as file:
    rps_rounds = file.read().split("\n")

def determine_score(cases):
    all_cases = {'A X': 3 + 1, 'A Y': 6 + 2, 'A Z': 0 + 3, 
            'B X': 0 + 1, 'B Y': 3 + 2, 'B Z': 6 + 3, 
            'C X': 6 + 1, 'C Y': 0 + 2, 'C Z': 3 + 3}
    score = sum(all_cases[i] for i in cases)
    return score

def determine_case(cases):
    all_cases = {'A X': 0 + 3, 'A Y': 3 + 1, 'A Z': 6 + 2, 
                'B X': 0 + 1, 'B Y': 3 + 2, 'B Z': 6 + 3, 
                'C X': 0 + 2, 'C Y': 3 + 3, 'C Z': 6 + 1}
    score = sum(all_cases[i] for i in cases)
    return score

print(determine_case(rps_rounds))

 

