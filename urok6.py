# try - except
# try:
#     print("start")
#     print(error)
#     print("OK")
# except:
#     print("Error")
# print("cod posle")

# try:
#     print("start")
#     print(10/0)
#     print("OK")
# # except NameError:
# #     print("NE ZDECb")
# # except ZeroDivisionError:
# #     print("ZD Error")
# # except (NameError, ZeroDivisionError):
# #     print("vse herovo")
# except (NameError, ZeroDivisionError) as error: #!!!!!!!!!!!!!!
#     print(error)


##Ucklychenie

# def a(var_1):
#     if type(var_1) != str:
#         raise TypeError(f"Never tip dannih{type(var_1)},"
#         f"nado string")
#     else:
#         return var_1
# first_var = 10
# a(first_var)

# class BuildingError(Exception):
#     def __str__(self):
#         return f"Nuzhno bolsche zolota"
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return "dostatochno materiala"
#     else:
#         raise BuildingError(amount_of_material)
#
# check_material(299, 300)

import warnings

warnings.simplefilter("ignore", SyntaxWarning)

try:
    warnings.warn("Syntax poehal", SyntaxWarning)
    print("test")
except:
    print("warning processed")
