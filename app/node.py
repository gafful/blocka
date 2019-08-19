from hashlib import sha256
import json
import time
from flask import Flask, request
import requests

class Block:
    def __init__(self, idx, trx, timestamp, prev_hash):
        self.idx = idx
        self.trx = trx
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.nonce = 0

    def compute_hash(self):
        """
        Create has of given block
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

class Blockchain:
    difficulty = 2

    def __init__(self):
        self.unconfirmed_trx = []
        self.chain = []
        self.create_genesis_block()

    @property
    def last_block(self):
        return self.chain[-1]

    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def proof_of_work(self, block):
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        
        return computed_hash

    def add_block(self, block, proof):
        prev_hash = self.last_block.hash

        if prev_hash != block.prev_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof

    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.compute_hash())

    def add_new_transaction(self, trx):
        self.unconfirmed_trx.append(trx)

    def mine(self):
        if not self.unconfirmed_trx:
            return False

        last_block = self.last_block

        new_block = Block(last_block.idx + 1, self.unconfirmed_trx, time.time(), last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_trx = []
        return new_block.idx


app = Flask(__name__)