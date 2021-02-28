from multiprocessing.connection import Client
import sys

c = Client(('localhost', 5000))

c.send(sys.argv[1])
# c.send("partially_passed")
# c.send(sys.argv[2])
# print('Got:', c.recv())

# c.send({'a': 123})
# print('Got:', c.recv())
