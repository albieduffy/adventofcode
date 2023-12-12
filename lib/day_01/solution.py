import re
nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1":"1",
    "2":"2",
    "3":"3",
    "4":"4",
    "5":"5",
    "6":"6",
    "7":"7",
    "8":"8",
    "9":"9"
}
def parse(data):
    data = data.replace("\n", " ").split(" ")
    data = [list(x[i:j] for i in range(len(x)) for j in range(i+1, len(x)+1) if (x[i:j] in nums)) for x in data]
    return data


def solve(input):
    solution = sum([int(nums[x[0]] + nums[x[-1]]) for x in input])
    return solution
