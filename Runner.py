import sys
from importlib import import_module

print('------------------------------------------------------------------------------------------------------')

mod = import_module(f'Problems.Problem{sys.argv[1]}.Solution')

met = getattr(mod, 'execute')

met()

print('------------------------------------------------------------------------------------------------------')
print('')