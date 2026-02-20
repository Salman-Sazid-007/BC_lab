import hashlib
import json
import time
import uuid


# -----------------------------
# Transaction Class
# -----------------------------
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.tx_id = str(uuid.uuid4())
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def to_dict(self):
        return {
            "tx_id": self.tx_id,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount
        }


# -----------------------------
# Block Class
# -----------------------------
class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "previous_hash": self.previous_hash
        }, sort_keys=True)

        return hashlib.sha256(block_string.encode()).hexdigest()


# -----------------------------
# Blockchain Class with UTXO
# -----------------------------
class Blockchain:
    def __init__(self):
        self.chain = []
        self.utxo = {}  # UTXO set
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_tx = Transaction("System", "Alice", 100)
        self.utxo[genesis_tx.tx_id] = {
            "owner": "Alice",
            "amount": 100
        }
        genesis_block = Block(0, [genesis_tx], "0")
        self.chain.append(genesis_block)

    def get_balance(self, user):
        balance = 0
        for tx_id, output in self.utxo.items():
            if output["owner"] == user:
                balance += output["amount"]
        return balance

    def create_transaction(self, sender, receiver, amount):
        balance = self.get_balance(sender)
        if balance < amount:
            print("❌ Transaction Failed: Insufficient balance")
            return None

        # Spend UTXOs
        total = 0
        spent_tx_ids = []
        for tx_id, output in list(self.utxo.items()):
            if output["owner"] == sender:
                total += output["amount"]
                spent_tx_ids.append(tx_id)
                del self.utxo[tx_id]
                if total >= amount:
                    break

        # Create new transaction
        new_tx = Transaction(sender, receiver, amount)

        # Add receiver UTXO
        self.utxo[new_tx.tx_id] = {
            "owner": receiver,
            "amount": amount
        }

        # If change exists, return back to sender
        if total > amount:
            change = total - amount
            change_tx = Transaction(sender, sender, change)
            self.utxo[change_tx.tx_id] = {
                "owner": sender,
                "amount": change
            }

        return new_tx

    def add_block(self, transactions):
        previous_hash = self.chain[-1].hash
        new_block = Block(len(self.chain), transactions, previous_hash)
        self.chain.append(new_block)

    def print_blockchain(self):
        print("\n========== BLOCKCHAIN ==========")
        for block in self.chain:
            print("\nBlock Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print("Transactions:")
            for tx in block.transactions:
                print(tx.to_dict())

    def print_utxo(self):
        print("\n========== UTXO SET ==========")
        for tx_id, output in self.utxo.items():
            print("TxID:", tx_id, "Owner:", output["owner"], "Amount:", output["amount"])


# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":

    # Create Blockchain
    blockchain = Blockchain()

    print("Initial Balance:")
    print("Alice:", blockchain.get_balance("Alice"))
    print("Bob:", blockchain.get_balance("Bob"))

    # Alice sends 40 coins to Bob
    tx1 = blockchain.create_transaction("Alice", "Bob", 40)

    if tx1:
        blockchain.add_block([tx1])

    print("\nAfter Transaction:")
    print("Alice:", blockchain.get_balance("Alice"))
    print("Bob:", blockchain.get_balance("Bob"))

    # Print blockchain
    blockchain.print_blockchain()

    # Print UTXO set
    blockchain.print_utxo()