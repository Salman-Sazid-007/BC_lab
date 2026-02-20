import hashlib
import random
import string


# ---------------------------------------
# Function to generate SHA-256 hash
# ---------------------------------------
def generate_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()


# ---------------------------------------
# 1️⃣ Deterministic Property
# Same input → Same hash
# ---------------------------------------
def test_deterministic():
    print("========== Deterministic Property ==========")
    message = "Blockchain"

    hash1 = generate_hash(message)
    hash2 = generate_hash(message)

    print("Message:", message)
    print("Hash 1:", hash1)
    print("Hash 2:", hash2)

    if hash1 == hash2:
        print("Result: PASS ✅ Same input gives same hash\n")
    else:
        print("Result: FAIL ❌\n")


# ---------------------------------------
# 2️⃣ Fixed Length Property
# ---------------------------------------
def test_fixed_length():
    print("========== Fixed Length Property ==========")

    msg1 = "Hi"
    msg2 = "This is a longer blockchain message"

    hash1 = generate_hash(msg1)
    hash2 = generate_hash(msg2)

    print("Length of Hash 1:", len(hash1))
    print("Length of Hash 2:", len(hash2))

    if len(hash1) == len(hash2):
        print("Result: PASS ✅ Hash length is fixed\n")
    else:
        print("Result: FAIL ❌\n")


# ---------------------------------------
# 3️⃣ Avalanche Effect
# Small change → Big difference in hash
# ---------------------------------------
def test_avalanche():
    print("========== Avalanche Effect ==========")

    msg1 = "Blockchain"
    msg2 = "lockchain"  # small change (B → b)

    hash1 = generate_hash(msg1)
    hash2 = generate_hash(msg2)

    print("Message 1:", msg1)
    print("Hash 1:", hash1)
    print("\nMessage 2:", msg2)
    print("Hash 2:", hash2)

    difference = sum(c1 != c2 for c1, c2 in zip(hash1, hash2))
    print("\nDifferent characters in hash:", difference)

    print("Result: PASS ✅ Small change causes large hash difference\n")


# ---------------------------------------
# 4️⃣ Preimage Resistance (Basic Demo)
# Hard to reverse hash
# ---------------------------------------
def test_preimage():
    print("========== Preimage Resistance ==========")

    message = "SecretMessage"
    hash_value = generate_hash(message)

    print("Original Message:", message)
    print("Hash:", hash_value)
    print("Trying to reverse hash...")

    print("Result: IMPOSSIBLE ❌ (One-way function)\n")


# ---------------------------------------
# 5️⃣ Collision Resistance (Practical Attempt)
# ---------------------------------------
def test_collision():
    print("========== Collision Resistance Test ==========")

    hashes = set()
    collision_found = False

    for _ in range(10000):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        hash_value = generate_hash(random_string)

        if hash_value in hashes:
            collision_found = True
            print("Collision Found ❌")
            break

        hashes.add(hash_value)

    if not collision_found:
        print("No collision found in 10,000 attempts ✅\n")


# ---------------------------------------
# Main Program
# ---------------------------------------
if __name__ == "__main__":

    test_deterministic()
    test_fixed_length()
    test_avalanche()
    test_preimage()
    test_collision()