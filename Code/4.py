import hashlib
import time

class Block:
    def __init__(self, number, miner, transactions, previous_hash, difficulty):
        self.number = number
        self.timestamp = time.time()
        self.miner = miner
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce = 0
        self.gas_used = len(transactions) * 21000
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.number)+str(self.timestamp)+str(self.transactions)+str(self.previous_hash)+str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

block = Block(1, "Miner1", ["Tx1","Tx2"], "00000abc", 4)

print(vars(block))