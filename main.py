import random


def dead_state(width, height):
    """
    Generate a 2D grid (list of lists) of the given width and height,
    with all cells initialized to 0 (DEAD).
    """
    return [[0 for _ in range(width)] for _ in range(height)]


def random_state(width, height):
    """
    Generate a 2D grid of the given width and height,
    with each cell randomly initialized to 0 (DEAD) or 1 (ALIVE).
    """
    state = dead_state(width, height)
    for y in range(height):
        for x in range(width):
            state[y][x] = 1 if random.random() >= 0.5 else 0
    return state


# Testing the functions
if __name__ == "__main__":
    width, height = 5, 5

    print("Dead State:")
    for row in dead_state(width, height):
        print(row)

    print("\nRandom State:")
    for row in random_state(width, height):
        print(row)
