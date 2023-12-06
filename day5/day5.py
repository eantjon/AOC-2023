import os
dirname = os.path.dirname(__file__)

with open(dirname + "/input.txt") as f:
    lines = f.readlines()

    
    def problem_1(): 
        def make_dictionaries(data, i, j):
            return [{"dest": int(line.split()[0]), "source": int(line.split()[1]), "length": int(line.split()[2])} for line in data[i:j]]

        def calculate(input, mapping):
            result = []
            for i in input:
                res = None
                for map in mapping:
                    if i >= map["source"] and i <= map["source"] + map["length"]:
                        res = map["dest"] + i - map["source"]
                        break
                if res == None:
                    res = i
                result.append(res)
            return result

        seeds = [int(x) for x in lines[0].split()[1:]]
        seedtosoil = make_dictionaries(lines, 3, 5)
        soiltofertilizer = make_dictionaries(lines, 7, 10)
        fertilizertowater = make_dictionaries(lines, 12, 16) 
        watertolight = make_dictionaries(lines, 18, 20) 
        lighttotemp = make_dictionaries(lines, 22, 25) 
        temperaturetohumidty = make_dictionaries(lines, 27, 29)
        humidtytolocation = make_dictionaries(lines, 31, 33)

        soils = calculate(seeds, seedtosoil)
        fertilizer = calculate(soils, soiltofertilizer)
        water = calculate(fertilizer, fertilizertowater)
        light = calculate(water, watertolight)
        temperature = calculate(light, lighttotemp)
        humidty = calculate(temperature, temperaturetohumidty)
        location = calculate(humidty, humidtytolocation)

        return min(location)



    def problem_2(): 
        print("start problem 2: ")
        def make_dictionaries(data, i, j):
            return [{"dest": int(line.split()[0]), "source": int(line.split()[1]), "length": int(line.split()[2])} for line in data[i:j]]

        def calculate(input, mapping):
            result = []
            for i in input:
                res = None
                for map in mapping:
                    if i >= map["source"] and i <= map["source"] + map["length"]:
                        res = map["dest"] + i - map["source"]
                        break
                if res == None:
                    res = i
                result.append(res)
            return result

        seeds = [int(x) for x in lines[0].split()[1:]]
        seedtosoil = make_dictionaries(lines, 3, 46)
        soiltofertilizer = make_dictionaries(lines, 48, 61)
        fertilizertowater = make_dictionaries(lines, 63, 108) 
        watertolight = make_dictionaries(lines, 110, 145) 
        lighttotemp = make_dictionaries(lines, 147, 160) 
        temperaturetohumidty = make_dictionaries(lines, 162, 196)
        humidtytolocation = make_dictionaries(lines, 198, 245)

        min_found = None

        seeds = [int(x) for x in lines[0].split()[1:]]
        for i in range(0, len(seeds), 2):
            for j in range(seeds[i+1]):
                soils = calculate([seeds[i]+ j], seedtosoil)
                fertilizer = calculate(soils, soiltofertilizer)
                water = calculate(fertilizer, fertilizertowater)
                light = calculate(water, watertolight)
                temperature = calculate(light, lighttotemp)
                humidty = calculate(temperature, temperaturetohumidty)
                location = calculate(humidty, humidtytolocation)
                if not min_found or location[0] < min_found:
                    min_found = location[0] - 1
                    print(min_found)

    print("problem 1: " + str(problem_1()))
    print("problem 2: " + str(problem_2()))