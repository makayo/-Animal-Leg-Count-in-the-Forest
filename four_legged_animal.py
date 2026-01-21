LEG_MAP = {
    "lion": 4, "deer": 4, "elephant": 4, "horse": 4, "dog": 4, "cat": 4,
    "monkey": 2, "parrot": 2, "ostrich": 2,
    "snake": 0, "worm": 0,
    "spider": 8, "ant": 6, "centipede": 100
}

def count_four_legged_animals(animals):
    count = 0
    for animal in animals:
        if LEG_MAP.get(animal, -1) == 4:
            count += 1
    return count
