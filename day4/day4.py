import os

dirname = os.path.dirname(__file__)

def problem_1():
    total_points = 0
    with open(dirname + "/input.txt") as f:
        for line in f.readlines():
            scratchons = line.split(":")[1]
            scratchons = scratchons.split("|")
            winning_numbers = scratchons[0].split()
            my_numbers = scratchons[1].strip("\n") 
            my_numbers = scratchons[1].split()
            current_numbers_found = 0
            for i in my_numbers:
                if i in winning_numbers:
                    if current_numbers_found == 0:
                        current_numbers_found = 1
                    else:
                        current_numbers_found = current_numbers_found * 2
            total_points += current_numbers_found
            current_numbers_found = 0

    print(total_points)


def problem_2():
    arr = []
    with open(dirname + "/input.txt") as f:
        lines = f.readlines()
        arr = [1]*len(lines)

    counter = 0
    with open(dirname + "/input.txt") as f:
        for line in f.readlines():
            scratchons = line.split(":")[1]
            scratchons = scratchons.split("|")
            winning_numbers = scratchons[0].split()
            my_numbers = scratchons[1].strip("\n") 
            my_numbers = scratchons[1].split()
            current_numbers_found = 0
            for i in my_numbers:
                if i in winning_numbers:
                    current_numbers_found += 1

            for j in range(1, current_numbers_found + 1):
                arr[counter + j] += arr[counter]

            current_numbers_found = 0
            counter += 1
    print(sum(arr))

problem_1()
problem_2()