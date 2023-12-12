import re
from collections import defaultdict
def valid_position(x, y, i, j):
    if (x < 0 or y < 0 or x > i - 1 or y > j - 1):
        return False
    return True

def parse(data):
    data = data.replace("\n", " ").split(" ")
    return data

def solve(input):
    graph = [[[y, False, False] for y in x] for x in input]
    
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            node = graph[i][j]
            if not node[0].isalnum() and not node[0] == ".":
                node[1] = True
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if valid_position(x, y, len(graph), len(graph[i])):
                            graph[x][y][1] = True if graph[x][y][0].isnumeric() else False
    
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            node = graph[i][j]
            if node[1] is True:
                left = j - 1
                while valid_position(i, left, len(graph), len(graph[i])) and (graph[i][left][0].isnumeric()):
                    neighbour = graph[i][left]
                    neighbour[1] = True
                    left -= 1
                
                right = j + 1
                while valid_position(i, right, len(graph), len(graph[i])) and (graph[i][right][0].isnumeric()):
                    neighbour = graph[i][right]
                    neighbour[1] = True
                    right += 1
    
    numbers = list()
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            string = ""
            while valid_position(i, j, len(graph), len(graph[i])) and graph[i][j][1] is True and graph[i][j][0].isnumeric() and graph[i][j][2] is False:
                graph[i][j][2] = True
                string += graph[i][j][0]
                j += 1

            if string:
                numbers.append(string)

    solution1 = sum([int(x) for x in numbers])

    graph = [[[y, False, 0] for y in x] for x in input]
    
    coodict= dict()
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            node = graph[i][j]
            if not node[0].isalnum() and node[0] == "*":
                node[1] = True
                num = 0
                coordinates = defaultdict(list)
                for y in range(j - 1, j + 2):
                    for x in range(i - 1, i + 2):
                        if valid_position(x, y, len(graph), len(graph[i])) and graph[x][y][0].isnumeric():
                            while graph[x][y][0].isnumeric() and graph[x][y][1] is False and y in range(j - 1, j + 2):
                                graph[x][y][1] = True
                                num += 1 if (y-1, x) not in coordinates else 0
                                coordinates[x].append(y)
                                y += 1
                node[2] = num
                coodict[i, j] = coordinates

    for dicts in coodict:
        touching = 0
        for row in coodict[dicts]:
            touching += 1 if sorted(coodict[dicts][row]) == list(range(min(coodict[dicts][row]), max(coodict[dicts][row]) + 1 )) else 2
        coodict[dicts]["touching"] = touching

    
    coodict = {
        k: v for k, v in coodict.items() if v["touching"] == 2
    }

    
    numbers = list()
    for dic in coodict:
        nums = set()
        for row in coodict[dic]:
            if row != "touching":
                for j in coodict[dic][row]:
                    number = graph[row][j][0]
                    left = j - 1
                    while valid_position(row, left, len(graph), len(graph[row])) and (graph[row][left][0].isnumeric()):
                        neighbour = graph[row][left]
                        neighbour[1] = True
                        left -= 1
                        number = neighbour[0] + number
                    
                    right = j + 1
                    while valid_position(row, right, len(graph), len(graph[row])) and (graph[row][right][0].isnumeric()):
                        neighbour = graph[row][right]
                        neighbour[1] = True
                        right += 1
                        number = number + neighbour[0]

                    nums.add(number)

        numbers.append([int(num) for num in nums])

    solution2 = [x[0] * x[1] for x in numbers]

    solution2 = sum(solution2)
    return solution1, solution2
