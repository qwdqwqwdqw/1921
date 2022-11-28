import inspect
print(inspect.ismodule(inspect))
print(callable(inspect))
if inspect.ismodule(inspect) or callable(inspect):
    for method1 in dir(inspect):
        print(method1)
        for method2 in dir(method1):
            print(method2)
