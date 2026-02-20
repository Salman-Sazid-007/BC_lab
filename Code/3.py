import hashlib
import datetime


# ---------------------------
# Step 1: Define Block Class
# ---------------------------
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    # Function to calculate SHA-256 hash
    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()


# ---------------------------
# Step 2: Define Blockchain Class
# ---------------------------
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    # Create the first block (Genesis Block)
    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    # Get last block
    def get_last_block(self):
        return self.chain[-1]

    # Add new block
    def add_block(self, data):
        previous_block = self.get_last_block()
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    # Traverse and print blockchain
    def print_blockchain(self):
        print("\n========== Blockchain ==========\n")
        for block in self.chain:
            print("Block Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print("--------------------------------------")


# ---------------------------
# Step 3: Main Program
# ---------------------------
if __name__ == "__main__":
    
    # Create Blockchain
    my_blockchain = Blockchain()

    # Add four new blocks
    my_blockchain.add_block("Transaction Data Block 1")
    my_blockchain.add_block("Transaction Data Block 2")
    my_blockchain.add_block("Transaction Data Block 3")
    my_blockchain.add_block("Transaction Data Block 4")

    # Traverse and print all blocks
    my_blockchain.print_blockchain()