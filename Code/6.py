import hashlib
import time


class ProofOfWork:
    def __init__(self, data, difficulty):
        self.data = data
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = None

    # Function to calculate hash
    def calculate_hash(self):
        text = self.data + str(self.nonce)
        return hashlib.sha256(text.encode()).hexdigest()

    # Mining function (PoW Algorithm)
    def mine(self):
        print("⛏ Mining started...")
        start_time = time.time()

        target = "0" * self.difficulty

        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith(target):
                break
            else:
                self.nonce += 1

        end_time = time.time()

        print("✅ Block mined successfully!")
        print("Data:", self.data)
        print("Nonce:", self.nonce)
        print("Hash:", self.hash)
        print("Mining Time:", round(end_time - start_time, 4), "seconds")


# ----------------------
# Main Program
# ----------------------
if __name__ == "__main__":

    user_data = input("Enter block data: ")
    difficulty = int(input("Enter difficulty level (number of leading zeros): "))

    pow = ProofOfWork(user_data, difficulty)
    pow.mine()