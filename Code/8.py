import requests
import json

# 🔑 Replace with your actual Etherscan API key
API_KEY = "YOUR_API_KEY"

# Base URL
BASE_URL = "https://api.etherscan.io/api"


# ---------------------------------
# Step 1: Get Latest Block Number
# ---------------------------------
def get_latest_block_number():
    url = f"{BASE_URL}?module=proxy&action=eth_blockNumber&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "result" in data:
        # Convert hex block number to integer
        latest_block = int(data["result"], 16)
        return latest_block
    else:
        print("Error fetching latest block number")
        return None


# ---------------------------------
# Step 2: Get Block Details
# ---------------------------------
def get_block_details(block_number):
    # Convert block number to hex
    block_hex = hex(block_number)

    url = f"{BASE_URL}?module=proxy&action=eth_getBlockByNumber&tag={block_hex}&boolean=true&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "result" in data:
        return data["result"]
    else:
        print("Error fetching block details")
        return None


# ---------------------------------
# Main Program
# ---------------------------------
if __name__ == "__main__":

    print("Fetching latest Ethereum block information...\n")

    latest_block_number = get_latest_block_number()

    if latest_block_number:
        print("Latest Block Number:", latest_block_number)

        block_data = get_block_details(latest_block_number)

        if block_data:
            print("\n========== Block Details ==========")
            print("Block Hash:", block_data["hash"])
            print("Parent Hash:", block_data["parentHash"])
            print("Miner:", block_data["miner"])
            print("Timestamp:", int(block_data["timestamp"], 16))
            print("Gas Used:", int(block_data["gasUsed"], 16))
            print("Gas Limit:", int(block_data["gasLimit"], 16))
            print("Transaction Count:", len(block_data["transactions"]))
            print("Difficulty:", int(block_data["difficulty"], 16))