import argparse
import random
import time
from pathlib import Path

from colorama import Fore, init

# Initialize colorama
init(autoreset=True)


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


def load_board_state(file_path):
    """
    Load a board state from a file.
    Each line in the file represents a row,
    with '0' for DEAD and '1' for ALIVE cells.
    """
    with open(file_path, 'r') as file:
        return [[int(char) for char in line.strip()] for line in file if
                line.strip()]


def render(board):
    """
    Pretty-print the board state to the terminal with rainbow colors for
    ALIVE cells.
    """
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE,
              Fore.MAGENTA]
    color_index = 0

    print("-" * (len(board[0]) + 2))
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == 1:
                print(colors[color_index % len(colors)] + "█", end="")
                color_index += 1
            else:
                print(" ", end="")
        print("|")
    print("-" * (len(board[0]) + 2))


def next_board_state(initial_state, neighborhood):
    """
    Calculate the next state of the board based on the Game of Life rules and a
    given neighborhood.
    """
    height = len(initial_state)
    width = len(initial_state[0])
    new_state = dead_state(width, height)

    for y in range(height):
        for x in range(width):
            live_neighbors = 0
            for dy, dx in neighborhood:
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


MOORE_NEIGHBORHOOD = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),
                      (1, 0), (1, 1)]

VON_NEUMANN_NEIGHBORHOOD = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Run Life forever
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Conway's Game of Life.")
    parser.add_argument("-i", "--input", type=str, default=None,
                        help="Name of the initial pattern file (without "
                             "extension) in the templates folder.")
    parser.add_argument("-r", "--rules", type=str, default="moore",
                        choices=["moore", "von_neumann"],
                        help="Choose the ruleset: 'moore' for Moore "
                             "Neighborhood, 'von_neumann' for Von Neumann "
                             "Neighborhood.")
    args = parser.parse_args()

    width, height = 20, 10

    if args.input:
        template_path = Path.cwd() / "templates" / f"{args.input}.txt"
        if not template_path.exists():
            print(f"Error: File '{template_path}' not found.")
            exit(1)
        current_state = load_board_state(template_path)
    else:
        current_state = random_state(width, height)

    neighbourhood_dict = {"moore": MOORE_NEIGHBORHOOD,
                          "von_neumann": VON_NEUMANN_NEIGHBORHOOD}

    neighborhood = neighbourhood_dict.get(args.rules)

    try:
        while True:
            render(current_state)
            current_state = next_board_state(current_state, neighborhood)
            time.sleep(0.5)  # Add a short delay for better visualization
    except KeyboardInterrupt:
        print("\nGame of Life terminated.")
