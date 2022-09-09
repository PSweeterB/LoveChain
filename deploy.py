import os

from solcx import compile_standard
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

with open("./contracts/SimplStorage.sol", 'r') as contract:
    love = contract.read()

compiled_col = compile_standard(
    {
    "language": "Solidity",
    "sources" : {"SimplStorage.sol": {"content": love}},
    "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}}}
    },
    solc_version="0.8.0",
    )

bytecode = compiled_col['contracts']['SimplStorage.sol']['Storage']["evm"]["bytecode"]["object"]
abi = compiled_col['contracts']['SimplStorage.sol']['Storage']['abi']

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
chain_id = 1337
my_address = "0xAc7d669BECFFb546698776e6382609Cb5308bC39"
pk = os.getenv("PRIVATE_KEY")

# SimplStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# nonce = w3.eth.getTransactionCount(my_address)
# print(nonce)
# transaction = SimplStorage.constructor().buildTransaction(
#     {"gasPrice": w3.eth.gas_price,
#      "chainId": chain_id,
#      "from": my_address,
#      "nonce": nonce})
# signet_thx = w3.eth.account.sign_transaction(transaction, pk)
# sanded_thx = w3.eth.send_raw_transaction(signet_thx.rawTransaction)
# tx_receipt = w3.eth.wait_for_transaction_receipt(sanded_thx)

# simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
simple_storage = w3.eth.contract(address="0xef972cfe5a9ef84a1e7bf3d92597117e7ea08d70", abi=abi)

print(simple_storage.functions.retrieve().call())

nonce = w3.eth.getTransactionCount(my_address)
transaction = simple_storage.functions.store(100).buildTransaction(
    {"gasPrice": w3.eth.gas_price,
     "chainId": chain_id,
     "from": my_address,
     "nonce": nonce})
signet_thx = w3.eth.account.sign_transaction(transaction, pk)
sanded_thx = w3.eth.send_raw_transaction(signet_thx.rawTransaction)
print(simple_storage.functions.retrieve().call())