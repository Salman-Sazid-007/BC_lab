import hashlib
import time


def solve_puzzle(input_string, difficulty):
    nonce = 0
    target = "0" * difficulty
    start_time = time.time()

    while True:
        # Combine input string and nonce
        text = input_string + str(nonce)

        # Generate SHA-256 hash
        hash_result = hashlib.sha256(text.encode()).hexdigest()

        # Check if hash starts with required leading zeros
        if hash_result.startswith(target):
            end_time = time.time()
            return nonce, hash_result, round(end_time - start_time, 4)

        nonce += 1


# ------------------------
# Main Program
# ------------------------
if __name__ == "__main__":

    user_string = input("Enter a string: ")
    difficulty = int(input("Enter number of leading zeros required: "))

    print("\n⛏ Solving the Leading Zeros Puzzle...\n")

    nonce, final_hash, mining_time = solve_puzzle(user_string, difficulty)

    print("✅ Puzzle Solved!")
    print("Input String:", user_string)
    print("Difficulty (Leading Zeros):", difficulty)
    print("Nonce Value Found:", nonce)
    print("Generated Hash:", final_hash)
    print("Time Taken:", mining_time, "seconds")