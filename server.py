from flask import Flask, request
from app.node import Blockchain, app
import time
import json

blockchain = Blockchain()


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data), "chain": chain_data})

app.run(debug=True)