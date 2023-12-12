from math import inf

class Almanac:
    def __init__(self, data):
        data = [x.split(":")[1].strip() for x in data]
        
        self.seeds = [int(x) for x in data[0].split()]
        self.seed_pairs = [
            range(self.seeds[0], self.seeds[0] + self.seeds[1]),
            range(self.seeds[2], self.seeds[2] + self.seeds[3]),
            range(self.seeds[4], self.seeds[4] + self.seeds[5]),
            range(self.seeds[6], self.seeds[6] + self.seeds[7]),
            range(self.seeds[8], self.seeds[8] + self.seeds[9])
        ]
        self.optimised_seed_pairs = self.reduce_ranges(self.seed_pairs)

        self.seed_to_soil = Map([x.split(" ") for x in data[1].split("\n")])
        self.soil_to_fertiliser = Map([x.split(" ") for x in data[2].split("\n")])
        self.fertiliser_to_water = Map([x.split(" ") for x in data[3].split("\n")])
        self.water_to_light = Map([x.split(" ") for x in data[4].split("\n")])
        self.light_to_temperature = Map([x.split(" ") for x in data[5].split("\n")])
        self.temperature_to_humidity = Map([x.split(" ") for x in data[6].split("\n")])
        self.humidity_to_location = Map([x.split(" ") for x in data[7].split("\n")])


    def navigate_level(self, seed, level):
        for section in level.map:
            if seed in section:
                offset = seed - section[0]
                return level.map[section][0] + offset

        return seed
    
    def navigate_levels(self, seed, direction=False):
        levels = [
            self.seed_to_soil,
            self.soil_to_fertiliser,
            self.fertiliser_to_water,
            self.water_to_light,
            self.light_to_temperature,
            self.temperature_to_humidity,
            self.humidity_to_location,
        ]
        
        if direction:
            levels = levels[::-1]

        seed = seed
        while len(levels):
            seed = self.navigate_level(seed, levels[0])
            levels.pop(0)

        return seed
    
    def check_overlaps(self, seed_pairs):
        overlaps = list()
        for i in range(len(seed_pairs) - 1):
            for j in range(i + 1, len(seed_pairs)):
                overlaps.append(
                    self.overlap(
                        seed_pairs[i][0],
                        seed_pairs[j][0],
                        seed_pairs[i][1],
                        seed_pairs[j][1],
                    )
                )
        return overlaps

    def overlap(self, start1, end1, start2, end2):
        """Does the range (start1, end1) overlap with (start2, end2)?"""
        return  end1 >= start2 and end2 >= start1
    
    def reduce_ranges(self, seed_pairs):
        # Sort the ranges based on their start values
        sorted_ranges = sorted(seed_pairs, key=lambda x: x.start)

        # Initialize a list to store the reduced ranges
        reduced_ranges = [sorted_ranges[0]]

        # Iterate through the sorted ranges
        for current_range in sorted_ranges[1:]:
            # Get the last reduced range
            last_range = reduced_ranges[-1]

            # Check for overlap and merge if necessary
            if current_range.start <= last_range.stop:
                # Merge the ranges if there is an overlap
                reduced_ranges[-1] = range(last_range.start, max(last_range.stop, current_range.stop))
            else:
                # Add the current range to the reduced list if no overlap
                reduced_ranges.append(current_range)

        return reduced_ranges

    def seed_pairs_bs(self, seed_pairs):
        lowest = inf
        
        for section in seed_pairs:
            for i in section:
                lowest = self.navigate_levels(i) if self.navigate_levels(i) < lowest else lowest
                self.navigate_levels(i)
        
        return lowest

class Map:
    def __init__(self, targets):
        self.map = self.targets_to_map(targets)
    
    def targets_to_map(self, targets):
        targets = sorted([(int(x[0]), int(x[1]), int(x[2])) for x in targets], key=lambda x: x[1])
        return {range(x[1], x[1] + x[2]): (x[0], x[2]) for x in targets}
