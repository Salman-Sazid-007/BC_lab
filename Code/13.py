import hashlib
import datetime
import time


# -----------------------------------
# Block Class
# -----------------------------------
class Block:
    def __init__(self, index, data, previous_hash, difficulty):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine_block()

    # Calculate hash
    def calculate_hash(self):
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Mining Process (Proof of Work)
    def mine_block(self):
        print(f"\n⛏ Mining Block {self.index}...")
        start_time = time.time()

        target = "0" * self.difficulty

        while True:
            hash_result = self.calculate_hash()
            if hash_result.startswith(target):
                end_time = time.time()
                print(f"✅ Block {self.index} Mined!")
                print("Nonce:", self.nonce)
                print("Hash:", hash_result)
                print("Time Taken:", round(end_time - start_time, 4), "seconds")
                return hash_result
            else:
                self.nonce += 1


# -----------------------------------
# Blockchain Class
# -----------------------------------
class Blockchain:
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0", self.difficulty)
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_last_block()
        new_block = Block(
            len(self.chain),
            data,
            previous_block.hash,
            self.difficulty
        )
        self.chain.append(new_block)

    def print_blockchain(self):
        print("\n========== Blockchain ==========")
        for block in self.chain:
            print("\nBlock Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Nonce:", block.nonce)
            print("Hash:", block.hash)
            print("----------------------------------")


# -----------------------------------
# Main Program
# -----------------------------------
if __name__ == "__main__":

    difficulty = int(input("Enter mining difficulty (number of leading zeros): "))

    blockchain = Blockchain(difficulty)

    blockchain.add_block("Alice pays Bob 5 BTC")
    blockchain.add_block("Bob pays Charlie 2 BTC")
    blockchain.add_block("Charlie pays David 1 BTC")

    blockchain.print_blockchain()
