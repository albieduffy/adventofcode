from collections import defaultdict
def parse(data):
    data = data.split("\n")
    return data

def solve(input):
    data = [x.split(":")[1].strip() for x in input]
    data = [x.split("|") for x in data]
    data = [(set(x[0].split(" ")), list(x[1].split(" "))) for x in data]
    
    solution1 = 0
    for game in range(len(data)):
        count = 0
        for number in data[game][1]:
            if number and number in data[game][0]:
                count += 1
        if count == 1:
            solution1 += count
        elif count > 1:
            solution1 += (1 * (2 ** (count - 1)))

    cards = {i: 1 for i in range(len(data))}

    for game in range(len(data)):
        count = 0
        for number in data[game][1]:
            if number and number in data[game][0]:
                count += 1
        for i in range(1, count + 1):
            cards[game + i] += 1 * cards[game]

    solution2 = sum(cards.values())
    return solution1, solution2