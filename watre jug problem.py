from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    """Solves the water jug problem using BFS."""
    # To keep track of visited states
    visited = set()

    # Queue for BFS: each element is a tuple (jug1, jug2)
    queue = deque([(0, 0)])

    # Store the steps for the solution
    steps = []

    while queue:
        jug1, jug2 = queue.popleft()

        # If the current state has been visited, skip it
        if (jug1, jug2) in visited:
            continue

        # Mark the current state as visited
        visited.add((jug1, jug2))
        steps.append((jug1, jug2))

        # If we reach the target, return the solution
        if jug1 == target or jug2 == target:
            return steps

        # Generate all possible next states
        possible_moves = [
            (jug1_capacity, jug2),  # Fill Jug 1
            (jug1, jug2_capacity),  # Fill Jug 2
            (0, jug2),              # Empty Jug 1
            (jug1, 0),              # Empty Jug 2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  # Pour Jug 1 -> Jug 2
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)),  # Pour Jug 2 -> Jug 1
        ]

        # Add valid moves to the queue
        for move in possible_moves:
            if move not in visited:
                queue.append(move)

    # If no solution is found, return None
    return None

# Example usage
if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2

    solution = water_jug_problem(jug1_capacity, jug2_capacity, target)

    if solution:
        print("Steps to solve the problem:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")
