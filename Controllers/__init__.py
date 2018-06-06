import os

__all__ = []

for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    __all__ += [module[:-3]]
    __import__(("Controllers."+module[:-3]), locals(), globals(), [module[:-3]], -1)

del module
del os
