import hashlib


# ---------------------------------------
# SHA-256 Hash Function
# ---------------------------------------
def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


# ---------------------------------------
# Build Merkle Tree and Store All Levels
# ---------------------------------------
def build_merkle_tree(transactions):
    tree = []
    current_level = [calculate_hash(tx) for tx in transactions]
    tree.append(current_level)

    while len(current_level) > 1:
        next_level = []

        # If odd number → duplicate last
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])

        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i + 1]
            next_hash = calculate_hash(combined)
            next_level.append(next_hash)

        tree.append(next_level)
        current_level = next_level

    return tree


# ---------------------------------------
# Get Merkle Root
# ---------------------------------------
def get_merkle_root(tree):
    return tree[-1][0]


# ---------------------------------------
# Generate Membership Proof
# ---------------------------------------
def get_proof(tree, transaction, transactions):
    try:
        index = transactions.index(transaction)
    except ValueError:
        return None  # Not found

    proof = []

    for level in tree[:-1]:
        if len(level) % 2 != 0:
            level = level + [level[-1]]

        is_right_node = index % 2
        sibling_index = index - 1 if is_right_node else index + 1

        proof.append((level[sibling_index], is_right_node))
        index = index // 2

    return proof


# ---------------------------------------
# Verify Membership Proof
# ---------------------------------------
def verify_proof(transaction, proof, root):
    current_hash = calculate_hash(transaction)

    for sibling_hash, is_right_node in proof:
        if is_right_node:
            combined = sibling_hash + current_hash
        else:
            combined = current_hash + sibling_hash

        current_hash = calculate_hash(combined)

    return current_hash == root


# ---------------------------------------
# Main Program
# ---------------------------------------
if __name__ == "__main__":

    transactions = [
        "Alice pays Bob 10 BTC",
        "Bob pays Charlie 5 BTC",
        "Charlie pays David 2 BTC",
        "David pays Eva 1 BTC"
    ]

    # Build Merkle Tree
    merkle_tree = build_merkle_tree(transactions)
    merkle_root = get_merkle_root(merkle_tree)

    print("========== Merkle Root ==========")
    print(merkle_root)

    # ----------------------------
    # Membership Proof
    # ----------------------------
    tx_to_verify = "Bob pays Charlie 5 BTC"
    proof = get_proof(merkle_tree, tx_to_verify, transactions)

    if proof:
        print("\nMembership Proof Generated")
        is_valid = verify_proof(tx_to_verify, proof, merkle_root)
        print("Transaction Verified?", is_valid)
    else:
        print("\nTransaction Not Found (Non-Membership)")

    # ----------------------------
    # Non-Membership Demo
    # ----------------------------
    fake_tx = "Alice pays John 100 BTC"
    fake_proof = get_proof(merkle_tree, fake_tx, transactions)

    if fake_proof:
        print("\nFake Transaction Verified?",
              verify_proof(fake_tx, fake_proof, merkle_root))
    else:
        print("\nNon-Membership Proven: Transaction not in Merkle Tree")
    
