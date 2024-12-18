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


def render(board):
    """
    Pretty-print the board state to the terminal.
    Use '#' to represent ALIVE cells and ' ' for DEAD cells.
    """
    print("-" * (len(board[0]) + 2))
    for row in board:
        print("|" + "".join('#' if cell == 1 else ' ' for cell in row) + "|")
    print("-" * (len(board[0]) + 2))


# Testing the functions
if __name__ == "__main__":
    width, height = 5, 5

    print("Dead State:")
    a_dead_state = dead_state(width, height)
    render(a_dead_state)

    print("\nRandom State:")
    a_random_state = random_state(width, height)
    render(a_random_state)
