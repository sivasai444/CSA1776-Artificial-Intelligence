from itertools import permutations

def solve_cryptarithmetic():
    # Letters used in the problem
    letters = 'SENDMORY'

    # Ensure each letter gets a unique digit
    for perm in permutations(range(10), len(letters)):
        # Map letters to digits
        mapping = dict(zip(letters, perm))

        # Extract numbers based on the mapping
        S, E, N, D = mapping['S'], mapping['E'], mapping['N'], mapping['D']
        M, O, R, Y = mapping['M'], mapping['O'], mapping['R'], mapping['Y']

        # Leading letters cannot be zero
        if S == 0 or M == 0:
            continue

        # Form the numbers SEND, MORE, and MONEY
        SEND = S * 1000 + E * 100 + N * 10 + D
        MORE = M * 1000 + O * 100 + R * 10 + E
        MONEY = M * 10000 + O * 1000 + N * 100 + E * 10 + Y

        # Check if the equation SEND + MORE = MONEY holds
        if SEND + MORE == MONEY:
            print(f"SEND = {SEND}, MORE = {MORE}, MONEY = {MONEY}")
            return

    print("No solution found.")

if __name__ == "__main__":
    solve_cryptarithmetic()
