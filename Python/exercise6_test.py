def checkNum(num1, num2):
    return num1 == num2

import unittest

class Test_checkNum(unittest.TestCase):
    def setUp(self):            # 테스트 함수 전에 호출
        pass

    def tearDown(self):         # 테스트 함수 후에 호출
        pass

    def test_first(self):
        num1 = 1
        num2 = 1
        result = checkNum(num1, num2)
        self.assertEqual(result, True)

    def test_second(self):
        num1 = 1
        num2 = 2
        result = checkNum(num1, num2)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()

---------------------------------------------------------------------------

def checkNum(num1, num2):
    '''
    >>> checkNum(1, 1)
    True
    >>> checkNum(1, 2)
    True
    '''

    return num1 == num2

if __name__ == '__main__':
    import doctest
    doctest.testmod()           # 모든 테스트가 통과되면 아무것도 표시 안됨


---------------------------------------------------------------------------
