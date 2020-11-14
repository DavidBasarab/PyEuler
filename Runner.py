import sys
from importlib import import_module

print('')

mod = import_module(f'Problems.Problem{sys.argv[1]}.Problem{sys.argv[1]}')

met = getattr(mod, 'execute')

met()

print('')