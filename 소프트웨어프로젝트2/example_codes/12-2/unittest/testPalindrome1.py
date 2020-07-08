import unittest

from palindrome1 import Palindrome

class TestPalindrome(unittest.TestCase):

# stepinto -> 실행하는 동작 안으로 들어감(F7)
# stepover -> 실행하는 그 다음 동작으로 넘어감(F8)
    def setUp(self):
        self.p1 = Palindrome('abcd')
        self.p2 = Palindrome('abcdedcba')   #회문

    def tearDown(self):
        pass

    def testNormal(self):
        self.assertFalse(self.p1.normal())
        self.assertTrue(self.p2.normal())

if __name__ == '__main__':
    unittest.main()

