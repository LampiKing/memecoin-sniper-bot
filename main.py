from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
TARGET_TOKEN = os.getenv("TARGET_TOKEN")

print("🚀 Connecting to blockchain...")
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.is_connected():
    print("❌ Connection failed.")
    exit()

account = web3.eth.account.from_key(PRIVATE_KEY)
print(f"✅ Connected as {account.address}")
