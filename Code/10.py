import hashlib
import datetime


# -----------------------------------
# Part 1: Demonstrate SHA-256 Hashing
# -----------------------------------
def sha256_demo():
    print("========== SHA-256 Hash Demo ==========")
    message = input("Enter a message to hash: ")
    
    # Encode message to bytes
    message_bytes = message.encode()
    
    # Generate SHA-256 hash
    hash_result = hashlib.sha256(message_bytes).hexdigest()
    
    print("Original Message:", message)
    print("SHA-256 Hash:", hash_result)
    print()


# -----------------------------------
# Part 2: Block Class
# -----------------------------------
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    # Calculate block hash using SHA-256
    def calculate_hash(self):
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()


# -----------------------------------
# Part 3: Blockchain Class
# -----------------------------------
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    # Create Genesis Block
    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    # Get Last Block
    def get_last_block(self):
        return self.chain[-1]

    # Add New Block
    def add_block(self, data):
        previous_block = self.get_last_block()
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    # Print Blockchain
    def print_chain(self):
        print("\n========== Blockchain ==========")
        for block in self.chain:
            print("\nBlock Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Current Hash:", block.hash)
            print("----------------------------------")


# -----------------------------------
# Main Program
# -----------------------------------
if __name__ == "__main__":

    # Step 1: Demonstrate SHA-256
    sha256_demo()

    # Step 2: Create Blockchain
    blockchain = Blockchain()

    # Step 3: Add some blocks
    blockchain.add_block("Transaction Data 1")
    blockchain.add_block("Transaction Data 2")
    blockchain.add_block("Transaction Data 3")

    # Step 4: Print Blockchain
    blockchain.print_chain()