from collections import deque

def is_valid_state(state):
    """Check if a state is valid."""
    m_left, c_left, m_right, c_right = state
    # Ensure no side has more cannibals than missionaries (unless missionaries are 0)
    if (m_left < c_left and m_left > 0) or (m_right < c_right and m_right > 0):
        return False
    return True

def get_successors(state):
    """Generate all possible successors of a given state."""
    m_left, c_left, boat = state[:3]
    successors = []
    moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]  # Possible moves: (m, c)

    for m, c in moves:
        if boat == 1:  # Boat on the left
            new_state = (m_left - m, c_left - c, 0, state[3] + m, state[4] + c)
        else:  # Boat on the right
            new_state = (m_left + m, c_left + c, 1, state[3] - m, state[4] - c)

        # Check if the move is valid
        if 0 <= new_state[0] <= 3 and 0 <= new_state[1] <= 3 and 0 <= new_state[3] <= 3 and 0 <= new_state[4] <= 3:
            if is_valid_state(new_state[:4]):
                successors.append(new_state)

    return successors

def missionaries_and_cannibals():
    """Solve the Missionaries and Cannibals problem using BFS."""
    initial_state = (3, 3, 1, 0, 0)  # (m_left, c_left, boat, m_right, c_right)
    goal_state = (0, 0, 0, 3, 3)

    queue = deque([(initial_state, [])])  # (current state, path)
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state[:4] == goal_state[:4]:  # Check if goal is reached
            return path + [current_state]

        if current_state in visited:
            continue

        visited.add(current_state)

        for successor in get_successors(current_state):
            queue.append((successor, path + [current_state]))

    return None

def print_solution(solution):
    """Print the solution path."""
    if not solution:
        print("No solution found!")
        return

    print("Solution:")
    for step in solution:
        print(f"Left: {step[0]}M, {step[1]}C | Boat: {'Left' if step[2] == 1 else 'Right'} | Right: {step[3]}M, {step[4]}C")

if __name__ == "__main__":
    solution = missionaries_and_cannibals()
    print_solution(solution)
