# list = [1,2,3]
# iterator = iter(list)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for elem in iterator:
#     print(elem)
#
# """__ITER__ \ __NEXT__"""
# def kvadrat(number, max_degree):
#     i = 0
#     for _ in range(max_degree):
#         yield number**i
#         i+=1
# res = kvadrat(666,6)
# print(res)
# for _ in res:
#     print(_)
#
# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         res = kvadrat(666,6)
#         for _ in res:
#             print(_)
#
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
# count = Counter(5)
# for elem in count:
#     print(elem)
#
# def kvadrat(number, max_degree):
#     i = 0
#     for _ in range(max_degree):
#         yield number**i
#         i+=1
# res = kvadrat(666,6)
# print(res)
# for _ in res:
#     print(_)

# def kvadrat(number):
#     i = 0
#     while True:
#         result = number**i
#         yield result
#         if result > 10**20:
#             return
#         i +=1
# res = kvadrat(666)
# print(res)
# for _ in res:
#     print(_)

# def helper(work):
#     work_in_memory = work
#     def helper(work):
#         return f"I will help with your {work_in_memory}. Afterwards i will help you with {work}"
#     return helper
# helper = helper("homework")
# print(helper("cleaning"))
# print(helper("driving"))

def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"Y nas problemu {exc}")
        else:
            print(f"Y nas nety problem. Resultat - {result}")
    return checker

@checker
def calculate(expression):
    return eval(expression)
calculate("2+2")

@checker
def test_text(text):
    return print(text)
test_text("Vse zaschiBisb")
