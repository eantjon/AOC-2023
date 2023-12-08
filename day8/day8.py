import os
import math
dirname = os.path.dirname(__file__)

def lcm(*integers):
    a = integers[0]
    for b in integers[1:]:
        a = (a * b) // math.gcd (a, b)
    return a


f = open(dirname + "/input.txt")
lines = f.readlines()

def problem_1():
    steps = lines[0].strip("\n")
    mapping = {}
    order = []

    for i in lines[2:]:
        variable = (i.split("=")[:1])[0].strip()
        order.append(variable)
        possible_next_step = i.split("=")[1:][0].strip().strip("\n")
        possible_next_step = possible_next_step.strip("(").strip(")").split(",")

        mapping[variable] = (possible_next_step[0], possible_next_step[1].strip())

    counter = 0
    found = False
    current_i = "AAA"
    while not found:
        for i in steps:
            if i == "L":
                current_i = mapping[current_i][0]
                counter += 1
                if current_i == 'ZZZ':
                    found = True
            else:
                current_i = mapping[current_i][1]
                counter += 1
                if current_i == 'ZZZ':
                    found = True
                

    print(counter)


def problem_2():
    steps = lines[0].strip("\n")
    mapping = {}
    order = []

    for i in lines[2:]:
        variable = (i.split("=")[:1])[0].strip()
        order.append(variable)
        possible_next_step = i.split("=")[1:][0].strip().strip("\n")
        possible_next_step = possible_next_step.strip("(").strip(")").split(",")

        mapping[variable] = (possible_next_step[0], possible_next_step[1].strip())

    ends_with_a = []
    res = []
    for i in order:
        if i[2] == "A":
            ends_with_a.append(i)
        
    for i in ends_with_a:
        counter = 0
        current_i = i
        found = False
        while not found:
            for i in steps:
                if i == "L":
                    current_i = mapping[current_i][0]
                    counter += 1
                    if current_i[2] == 'Z':
                        found = True
                        res.append(counter)
                else:
                    current_i = mapping[current_i][1]
                    counter += 1
                    if current_i[2] == 'Z':
                        res.append(counter)
                        found = True
                

    print(lcm(*res))

problem_1()
problem_2()
