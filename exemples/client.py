from xmlrpc.client import *

proxy = ServerProxy('http://127.0.0.1:7001')

print(proxy.addtogether('x', 'y', 'z'))

print(proxy.addtogether(1, 2, 3, 4, 5))

print(proxy.quadratic(2, -4, 0))

print(proxy.quadratic(1, 2, 1))
