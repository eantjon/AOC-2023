import os
dirname = os.path.dirname(__file__)

with open(dirname + "/input.txt") as f:
    lines =  f.readlines()
    input = [i for i in lines]

def problem_1(input):
    symbol = {'#', '$', '!', '@', '%', '/', '&', '*', '=', '_', '-', '+'}

    def check_if_found_symbol(input, i , j):
        try: 
            if input[i][j+1] in symbol:
                return True
        except: pass
        try: 
            if input[i][j-1] in symbol:
                return True
        except: pass
        try: 
            if input[i+1][j] in symbol:
                return True
        except: pass
        try: 
            if input[i+1][j+1] in symbol:
                return True
        except: pass
        try: 
            if input[i+1][j-1] in symbol:
                return True
        except: pass
        try: 
            if input[i-1][j] in symbol:
                return True
        except: pass
        try: 
            if input[i-1][j+1] in symbol:
                return True
        except: pass
        try: 
            if input[i-1][j-1] in symbol:
                return True
        except: pass

        return False

    total_sum = 0
    for i in range(len(input)):
        found_number = False
        found_symbol = False
        number = 0
        for j in range(len(input[i])):
            if not found_number and input[i][j].isnumeric():
                found_number = True
                number = input[i][j]
                if found_symbol == False:
                    if check_if_found_symbol(input, i, j) == True:
                        found_symbol = True
            elif found_number and input[i][j].isnumeric():
                number += input[i][j]
                if found_symbol == False:
                    if check_if_found_symbol(input, i, j) == True:
                        found_symbol = True
                test = len(input[i][j])
                if found_symbol and j == len(input[i]) - 1:
                    total_sum += int(number)
                    found_symbol = False
                    found_number = False
                    number = 0
            elif found_number and (not input[i][j].isnumeric()):
                if found_symbol:
                    total_sum += int(number)
                found_symbol = False
                found_number = False
                number = 0
    print(total_sum)

def problem_2(input):
    symbol = '*'

    def check_if_found_symbol(input, i , j):
        try: 
            if input[i][j+1] == symbol:
                return str(i) + str(j+1)
        except: pass
        try: 
            if input[i][j-1] == symbol:
                return str(i) + str(j-1)
        except: pass
        try: 
            if input[i+1][j] == symbol:
                return str(i+1) + str(j)
        except: pass
        try: 
            if input[i+1][j+1] == symbol:
                return str(i+1) + str(j+1)
        except: pass
        try: 
            if input[i+1][j-1] == symbol:
                return str(i+1) + str(j-1)
        except: pass
        try: 
            if input[i-1][j] == symbol:
                return str(i-1) + str(j)
        except: pass
        try: 
            if input[i-1][j+1] == symbol:
                return str(i-1) + str(j+1)
        except: pass
        try: 
            if input[i-1][j-1] == symbol:
                return str(i-1) + str(j-1)
        except: pass

        return False

    gears = {}
    for i in range(len(input)):
        found_number = False
        found_symbol = False
        number = 0
        for j in range(len(input[i])):
            if not found_number and input[i][j].isnumeric():
                found_number = True
                number = input[i][j]
                if not found_symbol:
                    found_symbol = check_if_found_symbol(input, i, j)
            elif found_number and input[i][j].isnumeric():
                number += input[i][j]
                if not found_symbol:
                    found_symbol = check_if_found_symbol(input, i, j)
                if found_symbol and j == len(input[i]) - 1:
                    if found_symbol not in gears:
                        gears[found_symbol] = [int(number)]
                    else:
                        gears[found_symbol].append(int(number))
                    found_symbol = False
                    found_number = False
                    number = 0
            elif found_number and (not input[i][j].isnumeric()):
                if found_symbol:
                    if found_symbol not in gears:
                        gears[found_symbol] = [int(number)]
                    else:
                        gears[found_symbol].append(int(number))
                found_symbol = False
                found_number = False
                number = 0

    total_sum = 0
    for v in gears.values():
        if len(v) == 2:
            total_sum += (v[0] * v[1])
    print(total_sum)

problem_1(input)
problem_2(input)