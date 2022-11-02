import inspect
import colorama
print(inspect.ismodule(colorama))
print(callable(colorama))
for method in dir(colorama):
    print(method)
print(inspect.isclass(colorama.Cursor))
print(callable(colorama.Cursor))
for method in dir(colorama.Cursor):
    print(method)
