from collections import defaultdict
import numpy as np

def parse(data):
    data = data.split("\n")
    return data

def solve(input):
    data = [x.split(":")[1].strip() for x in input]
    data = [x.split() for x in data]
    data1 = [(int(x), int(y)) for x, y in zip(data[0], data[1])]

    game = Game(data1)

    solution1 = np.prod([x.victories for x in game.rounds])
    
    data2 = [(int("".join(data[0])), int("".join(data[1])))]
    game2 = Game(data2)

    solution2 = game2.rounds[0].victories
    return solution1, solution2


class Game():
    def __init__(self, rounds) -> None:
        self.rounds = [Round(x) for x in rounds]


class Round():
    def __init__(self, pair):
        self.time = pair[0]
        self.distance = pair[1]
        self.possibilities = self.distances()
        self.victories = self.solutions()

    def distances(self):
        distances = dict()

        for i in range(1, self.time + 1):
            distances[i] = (self.time - i) * i

        return distances    
    
    def solutions(self):
        return len([x for x in self.possibilities.values() if x > self.distance])
