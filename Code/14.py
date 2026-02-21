import hashlib


# -----------------------------------
# Function to calculate SHA-256 hash
# -----------------------------------
def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


# -----------------------------------
# Function to create Merkle Tree
# -----------------------------------
def create_merkle_tree(transactions):

    print("\n========== Building Merkle Tree ==========\n")

    # Step 1: Hash all transactions (Leaf Nodes)
    current_level = [calculate_hash(tx) for tx in transactions]

    print("Level 0 (Leaf Nodes):")
    for h in current_level:
        print(h)

    level = 0

    # Step 2: Continue until only one hash remains
    while len(current_level) > 1:
        next_level = []
        level += 1

        # If odd number of hashes → duplicate last one
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])

        print(f"\nLevel {level}:")

        # Pairwise hashing
        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i + 1]
            new_hash = calculate_hash(combined)
            next_level.append(new_hash)
            print(new_hash)

        current_level = next_level

    # Final hash is Merkle Root
    merkle_root = current_level[0]
    return merkle_root


# -----------------------------------
# Main Program
# -----------------------------------
if __name__ == "__main__":

    transactions = [
        "Alice pays Bob 10 BTC",
        "Bob pays Charlie 5 BTC",
        "Charlie pays David 2 BTC",
        "David pays Eva 1 BTC"
    ]

    merkle_root = create_merkle_tree(transactions)

    print("\n========== Merkle Root ==========")
    print("Merkle Root:", merkle_root)
