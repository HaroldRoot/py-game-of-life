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


def next_board_state(initial_state):
    """
    Calculate the next state of the board based on the Game of Life rules.
    """
    height = len(initial_state)
    width = len(initial_state[0])
    new_state = dead_state(width, height)

    for y in range(height):
        for x in range(width):
            live_neighbors = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < width:
                        live_neighbors += initial_state[ny][nx]

            if initial_state[y][x] == 1:  # ALIVE cell
                if live_neighbors < 2 or live_neighbors > 3:
                    new_state[y][x] = 0  # Dies
                else:
                    new_state[y][x] = 1  # Stays alive
            else:  # DEAD cell
                if live_neighbors == 3:
                    new_state[y][x] = 1  # Becomes alive

    return new_state


# Testing the functions
if __name__ == "__main__":
    width, height = 5, 5

    print("Dead State:")
    a_dead_state = dead_state(width, height)
    render(a_dead_state)

    print("\nRandom State:")
    a_random_state = random_state(width, height)
    render(a_random_state)

    print("\nNext State:")
    next_state = next_board_state(a_random_state)
    render(next_state)
