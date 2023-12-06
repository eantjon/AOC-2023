import os
dirname = os.path.dirname(__file__)
with open(dirname + "/input.txt") as f:
    lines =  f.readlines()

    def problem_1():
            time = [int(i) for i in (lines[0].split(":")[1]).split()]
            distance = [int(i) for i in (lines[1].split(":")[1]).split()]
            ways = 1

            for i in range(len(time)):
                curr_ways = 0
                for j in range(time[i]):
                    if j * (time[i] - j) > distance[i]:
                        curr_ways += 1
                ways = ways * curr_ways
            print(ways)

    def problem_2():

        with open(dirname + "/input.txt") as f:
            lines =  f.readlines()
            time = lines[0].split(":")[1].strip("\n").strip()
            final_time = ""
            final_distance = ""
            for i in time:
                if i != " ":
                    final_time += i
            distance = lines[1].split(":")[1].strip("\n").strip()
            for i in distance:
                if i != " ":
                    final_distance += i
            final_time = [int(final_time)]
            final_distance = [int(final_distance)]
            ways = 1

            for i in range(len(final_time)):
                curr_ways = 0
                for j in range(final_time[i]):
                    if j * (final_time[i] - j) > final_distance[i]:
                        curr_ways += 1
                ways = ways * curr_ways
            print(ways)
    
    problem_1()
    problem_2()