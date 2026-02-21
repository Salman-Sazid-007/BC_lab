import hashlib
import datetime


# -----------------------------------
# Block Class
# -----------------------------------
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    # Generate SHA-256 hash
    def calculate_hash(self):
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()


# -----------------------------------
# Blockchain Class
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
    def print_blockchain(self):
        print("\n========== Blockchain ==========")
        for block in self.chain:
            print("\nBlock Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Current Hash:", block.hash)
            print("----------------------------------")

    # Verify Blockchain Integrity
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Recalculate hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check previous hash link
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# -----------------------------------
# Main Program
# -----------------------------------
if __name__ == "__main__":

    blockchain = Blockchain()

    # Add Blocks
    blockchain.add_block("Alice pays Bob 10 BTC")
    blockchain.add_block("Bob pays Charlie 5 BTC")
    blockchain.add_block("Charlie pays David 2 BTC")

    # Print Blockchain
    blockchain.print_blockchain()

    # Verify Blockchain
    print("\nIs Blockchain Valid?", blockchain.is_chain_valid())

    # ----------------------------
    # Demonstrate Tampering
    # ----------------------------
    print("\n⚠ Tampering with block data...")
    blockchain.chain[1].data = "Alice pays Bob 1000 BTC"

    # Check again
    print("Is Blockchain Valid After Tampering?", blockchain.is_chain_valid())
