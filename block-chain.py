import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, product_id, source, destination, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.product_id = product_id
        self.source = source
        self.destination = destination
        self.hash = hash
        self.nonce = nonce

class SupplyChainBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(0, "0", int(time.time()), "GenesisProduct", "GenesisSource", "GenesisDestination", self.calculate_hash(0, "0", int(time.time()), "GenesisProduct", "GenesisSource", "GenesisDestination", 0), 0)
        self.chain.append(genesis_block)

    def add_movement(self, product_id, source, destination):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = int(time.time())
        previous_hash = previous_block.hash
        nonce = self.proof_of_work(index, previous_hash, timestamp, product_id, source, destination)
        new_hash = self.calculate_hash(index, previous_hash, timestamp, product_id, source, destination, nonce)
        new_block = Block(index, previous_hash, timestamp, product_id, source, destination, new_hash, nonce)
        self.chain.append(new_block)

    def proof_of_work(self, index, previous_hash, timestamp, product_id, source, destination):
        nonce = 0
        while True:
            new_hash = self.calculate_hash(index, previous_hash, timestamp, product_id, source, destination, nonce)
            if new_hash[:4] == "0000":
                return nonce
            nonce += 1

    def calculate_hash(self, index, previous_hash, timestamp, product_id, source, destination, nonce):
        value = str(index) + str(previous_hash) + str(timestamp) + str(product_id) + str(source) + str(destination) + str(nonce)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def print_chain(self):
        for block in self.chain:
            print(vars(block))

if __name__ == '__main__':
    supply_chain_blockchain = SupplyChainBlockchain()
    supply_chain_blockchain.add_movement("Product_1", "Factory_A", "Warehouse_B")
    supply_chain_blockchain.add_movement("Product_2", "Warehouse_B", "Retailer_C")
    supply_chain_blockchain.add_movement("Product_3", "Factory_A", "Retailer_C")
    supply_chain_blockchain.print_chain()