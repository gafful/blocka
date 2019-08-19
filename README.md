# blocka

A simple blockchain app.

## Runing locally
Get a local copy:
```sh
$ git clone https://github.com/gafful/blocka.git
```

In your [virtual environment](https://realpython.com/python-virtual-environments-a-primer/), install the requirements:
```sh
$ pip install -r requirements.txt
```

Run the blockchain node instance:
```sh
$ FLASK_APP=node.py flask run --port 5001
```

Run the REST API server:
```sh
$ python server.py
```

View the node's copy of the chain:
```sh
$ curl http://127.0.0.1:5000/chain
```

## Dependencies
[Flask](https://github.com/pallets/flask)