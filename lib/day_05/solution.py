from .almanac import Almanac

def parse(data):
    data = data.split("\n\n")
    return data

def overlap(start1, end1, start2, end2):
    """Does the range (start1, end1) overlap with (start2, end2)?"""
    return (
        start1 <= start2 <= end1 or
        start1 <= end2 <= end1 or
        start2 <= start1 <= end2 or
        start2 <= end1 <= end2
    )

def solve(input):
    almanac = Almanac(input)

    locations = [almanac.navigate_levels(seed, False) for seed in almanac.seeds]

    solution1 = min(locations)

    solution2 = almanac.seed_pairs_bs(almanac.optimised_seed_pairs)

    return solution1, solution2