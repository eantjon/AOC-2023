import os
import math
dirname = os.path.dirname(__file__)


f = open(dirname + "/input.txt")
lines = f.readlines()

def all_equal(lst):
    return not lst or [lst[0]]*len(lst) == lst

def problem_1():
    res = 0
    for i in lines:
        line = i.split()
        for j in range(len(line)):
            line[j] = int(line[j])
        all_differences = [line]
        differences = []
        found = False
        while not found:
            if all_equal(line):
                found = True
            else:
                for j in range(1, len(line)):
                    differences.append(line[j] - line[j - 1])
                all_differences.append(differences)
                line = differences
                differences = []
        for j in range(2, len(all_differences) + 1):
            all_differences[-j].append(all_differences[-j+1][-1] + all_differences[-j][-1])
        res += all_differences[0][-1]
    print(res)



def problem_2():
    res = 0
    for i in lines:
        line = i.split()
        for j in range(len(line)):
            line[j] = int(line[j])
        all_differences = [line]
        differences = []
        found = False
        while not found:
            if all_equal(line):
                found = True
            else:
                for j in range(1, len(line)):
                    differences.append(line[j] - line[j - 1])
                all_differences.append(differences)
                line = differences
                differences = []
        for j in range(2, len(all_differences) + 1):
            all_differences[-j].insert(0, all_differences[-j][0] - all_differences[-j+1][0])
        res += all_differences[0][0]
    print(res)

problem_1()
problem_2()