# import logging
#
# logging.basicConfig(level=logging.DEBUG,
#                     filename= "logs.log",
#                     filemode = "w",
#                     format = "We have next logging message: %(asctime)s:%(levelname)s - %(message)s")
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")
# try:
#     print(10/0)
# except Exception:
#     logging.exception("Exceptions")

# 0.5 ! ASSERT
# assert 2+2==5, "ne rabotaet"

#!! DOCTEST
# """
# >>> 2+2
# 5
# """
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

#!!! UNITTEST
def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result

  
  import unittest
from urok8 import*

class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2,2), 4)

    def test_kwargs(self):
        self.assertEqual(adder(a=10, b=11), 21)
    def test_mixed(self):
        self.assertEqual(adder(1, a=2),3)
    def test_diff(self):
        x = 10
        y = 0
        self.assertEqual(adder(0, -5, y, a=x), 5)
    def test_wrong_datatype(self):
        self.assertEqual(adder("5", "abc", 10), 15)

if __name__ =="__main__":
    unittest.main()
