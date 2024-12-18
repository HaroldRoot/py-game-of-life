from game_of_life import next_board_state


def test_next_board_state():
    """
    Unit tests for the next_board_state function.
    """
    # TEST 1: Dead cells with no live neighbors should stay dead
    init_state1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    expected_next_state1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    actual_next_state1 = next_board_state(init_state1)
    assert actual_next_state1 == expected_next_state1, f"Test 1 Failed: {actual_next_state1} != {expected_next_state1}"

    # TEST 2: Dead cells with exactly 3 neighbors should become alive
    init_state2 = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    expected_next_state2 = [
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    actual_next_state2 = next_board_state(init_state2)
    assert actual_next_state2 == expected_next_state2, f"Test 2 Failed: {actual_next_state2} != {expected_next_state2}"

    # TEST 3: Live cell with fewer than 2 neighbors should die
    init_state3 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    expected_next_state3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    actual_next_state3 = next_board_state(init_state3)
    assert actual_next_state3 == expected_next_state3, f"Test 3 Failed: {actual_next_state3} != {expected_next_state3}"

    # TEST 4: Live cell with 2 or 3 neighbors stays alive
    init_state4 = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    expected_next_state4 = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    actual_next_state4 = next_board_state(init_state4)
    assert actual_next_state4 == expected_next_state4, f"Test 4 Failed: {actual_next_state4} != {expected_next_state4}"

    # TEST 5: Cells on the edge of the board behave correctly
    init_state5 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    expected_next_state5 = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]
    actual_next_state5 = next_board_state(init_state5)
    assert actual_next_state5 == expected_next_state5, f"Test 5 Failed: {actual_next_state5} != {expected_next_state5}"

    print("All tests passed!")


if __name__ == "__main__":
    test_next_board_state()
