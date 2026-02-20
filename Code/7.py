import hashlib
import time
import random


# -----------------------------
# Validator Class
# -----------------------------
class Validator:
    def __init__(self, name, stake):
        self.name = name
        self.stake = stake


# -----------------------------
# Block Class
# -----------------------------
class Block:
    def __init__(self, index, data, previous_hash, validator):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.validator = validator
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.validator)
        return hashlib.sha256(block_string.encode()).hexdigest()


# -----------------------------
# Blockchain with PoS
# -----------------------------
class PoSBlockchain:
    def __init__(self):
        self.chain = []
        self.validators = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0", "System")
        self.chain.append(genesis_block)

    def add_validator(self, name, stake):
        validator = Validator(name, stake)
        self.validators.append(validator)

    # PoS Selection Algorithm
    def select_validator(self):
        total_stake = sum(v.stake for v in self.validators)
        pick = random.uniform(0, total_stake)
        current = 0

        for validator in self.validators:
            current += validator.stake
            if current > pick:
                return validator

    def add_block(self, data):
        validator = self.select_validator()
        previous_hash = self.chain[-1].hash
        new_block = Block(len(self.chain), data, previous_hash, validator.name)
        self.chain.append(new_block)

        print(f"\n✅ Block added by validator: {validator.name}")
        print(f"Stake: {validator.stake}")

    def print_blockchain(self):
        print("\n========== Blockchain ==========")
        for block in self.chain:
            print("\nBlock Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Validator:", block.validator)
            print("Hash:", block.hash)


# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":

    blockchain = PoSBlockchain()

    # Add Validators with stake
    blockchain.add_validator("Alice", 50)
    blockchain.add_validator("Bob", 30)
    blockchain.add_validator("Charlie", 20)

    # Add new blocks
    blockchain.add_block("Transaction Data 1")
    blockchain.add_block("Transaction Data 2")
    blockchain.add_block("Transaction Data 3")

    # Print blockchain
    blockchain.print_blockchain()