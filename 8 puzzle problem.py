import heapq

class PuzzleState:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(board, goal):
    # Manhattan distance heuristic
    distance = 0
    for i in range(1, 9):
        x1, y1 = divmod(board.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_neighbors(state):
    neighbors = []
    blank_idx = state.index(0)
    x, y = divmod(blank_idx, 3)

    moves = {
        'UP': (x - 1, y),
        'DOWN': (x + 1, y),
        'LEFT': (x, y - 1),
        'RIGHT': (x, y + 1),
    }

    for move, (new_x, new_y) in moves.items():
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_idx = new_x * 3 + new_y
            new_state = state[:]
            new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]
            neighbors.append((new_state, move))

    return neighbors

def reconstruct_path(node):
    path = []
    while node.parent:
        path.append(node.move)
        node = node.parent
    return path[::-1]

def solve_puzzle(start, goal):
    open_set = []
    heapq.heappush(open_set, PuzzleState(start, None, None, 0, heuristic(start, goal)))
    closed_set = set()

    while open_set:
        current = heapq.heappop(open_set)

        if current.board == goal:
            return reconstruct_path(current)

        closed_set.add(tuple(current.board))

        for neighbor, move in get_neighbors(current.board):
            if tuple(neighbor) in closed_set:
                continue

            new_cost = current.depth + 1 + heuristic(neighbor, goal)
            heapq.heappush(open_set, PuzzleState(neighbor, current, move, current.depth + 1, new_cost))

    return None

if __name__ == "__main__":
    start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # Example start state
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]   # Goal state

    solution = solve_puzzle(start_state, goal_state)

    if solution:
        print("Solution found! Moves:", solution)
    else:
        print("No solution exists.")
