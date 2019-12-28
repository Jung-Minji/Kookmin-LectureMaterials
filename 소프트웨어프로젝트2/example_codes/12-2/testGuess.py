import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('x')
        self.assertEqual(self.g1.displayCurrent(),  '_ e _ a u _ t ')
        self.g1.guess('y')
        self.assertEqual(self.g1.displayCurrent(),  '_ e _ a u _ t ')


    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('x')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u x ')
        self.g1.guess('y')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u x y ')

    def testGuess(self):
        # 리턴 값이 올바른가?
        self.assertTrue(self.g1.guess('d'))
        self.assertTrue(self.g1.guess('l'))
        self.assertFalse(self.g1.guess('s'))
        self.assertFalse(self.g1.guess('z'))

        # 부분적으로 맞추어진 단어의 상태가 올바르게 유지되는가?
        self.assertEqual(self.g1.currentStatus, 'de___l_')
        self.g1.guess('e')
        self.assertEqual(self.g1.currentStatus, 'de___l_')
        self.g1.guess('x')
        self.assertEqual(self.g1.currentStatus, 'de___l_')

        # 이용된 글자들의 집합을 나타내는 데이터는 올바르게 유지되는가?
        self.assertEqual(self.g1.guessedChars, {'z', 'e', 'x', 'd', 'l', 's'})

    def testFinished(self):
        # 단어의 전체를 다 맞춘 경우에 대한 처리가 올바른가?
        self.g1.guess('d')
        self.g1.guess('e')
        self.g1.guess('f')
        self.g1.guess('a')
        self.g1.guess('u')
        self.g1.guess('l')
        self.assertFalse(self.g1.finished())

        self.g1.guess('t')
        self.assertTrue(self.g1.finished())


if __name__ == '__main__':
    unittest.main()

# ※ 각 test메서드에서 class 메서드에 적용한 파라미터들은 각각의  test메서드 안에서만 작용한다!