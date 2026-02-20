import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 4
        self.create_genesis_block()

    def create_genesis_block(self):
        self.chain.append(Block(0, "Genesis Block", "0"))

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        return new_block

# Run
bc = Blockchain()
new_block = bc.add_block("Mined Transaction")

print("\nNew Block Mined:")
print(vars(new_block))