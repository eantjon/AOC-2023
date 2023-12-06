import os
dirname = os.path.dirname(__file__)

with open(dirname + "/input.txt") as f:
    lines =  f.readlines()
    input_data = [i for i in lines]

def problem_1(input_data):
    total_sum = 0
    for word in input_data:
        combi = ''
        for i in word:
            if i.isnumeric():
                combi += i
                break
        for i in word[::-1]:
            if i.isnumeric():
                combi += i
                break
        total_sum += int(combi)
    return(total_sum)

def problem_2(input_data):
    total_sum = 0
    numbers = {"one": "1",
               "two": "2",
               "three": "3",
               "four": "4",
               'five': "5",
               "six": "6",
               "seven": "7",
               "eight": "8",
               "nine": "9"}

    for word in input_data:
        combi = ''
        for i in range(len(word)):
            if word[i].isnumeric():
                combi += word[i]
                break
            found_word = False
            for key,value in numbers.items():
                try:
                    if word[i:i+len(key)+1] == key:
                        combi += value
                        found_word = True
                        break
                except:
                    pass
            if found_word:
                break
            
        for i in range(len(word)-1, -1, -1):
            if word[i].isnumeric():
                combi += word[i]
                break
            found_word= False
            for key in numbers:
                try:
                    if word[i-len(key)+1:i+1] == key:
                        combi += numbers[key]
                        found_word = True
                        break
                except:
                    pass
            if found_word:
                break
        total_sum += int(combi)
    return(total_sum)

print(problem_1(input_data))
print(problem_2(input_data))
