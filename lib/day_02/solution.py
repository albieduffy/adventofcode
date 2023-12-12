import numpy
def parse(data):
    data = data.replace("\n", "#").split("#")
    return data

def dict_giver(input):
    output = {x.strip(" ").split(" ")[1]: int(x.strip(" ").split(" ")[0]) for x in input}
    return output


def solve(input):
    limits = {
        "blue": 14,
        "blu": 14,
        "green": 13,
        "red": 12
    }

    data = [x.strip("Game ").split(": ") for x in input]
    data = {
        int(x[0]): [
            y.split(",") for y in x[1].split("; ")
        ] for x in data
    }
    data = {
        k: 
            [dict_giver(z) for z in v]
         for k, v in data.items()
    }
    
    count = 0
    for game in data:
        for round in data[game]:
            if any(round[x] > limits[x] for x in round):
                break
        else:
            count += game

    mins = list()
    for game in data:
        tmp = {}
        for round in data[game]:
            for x in round:
                if x == "blu":
                    tmp["blue"] = round[x] if round[x] > tmp.get("blue", 0) else tmp["blue"]
                else:
                    tmp[x] = round[x] if round[x] > tmp.get(x, 0) else tmp[x]

        mins.append(numpy.prod(list(tmp.values())))

    prods = sum(mins)


    return count, prods
