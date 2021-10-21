from operator import *
from math import *
from xmlrpc.server import *
from functools import *


def addtogether(*things):
    return reduce(add, things)


def quadratic(a, b, c):
    b24ac = sqrt(b*b - 4.0*a*c)
    return list(({(-b - b24ac) / 2.0 * a, (-b + b24ac) / 2.0 * a}))


s = SimpleXMLRPCServer(('127.0.0.1', 7001))

s.register_introspection_functions()

s.register_multicall_functions()

s.register_function(addtogether)

s.register_function(quadratic)

print("Server ready")

s.serve_forever()
