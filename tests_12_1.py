import Blame  # исходный код, который нужно обложить тестами с GitHub.
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        rn = Blame.Runner(name='Бегун')
        for _ in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    def test_run(self):
        rn = Blame.Runner(name='Бегун')
        for _ in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    def test_challenge(self):
        rn_1 = Blame.Runner(name='Rn_1')
        rn_2 = Blame.Runner(name='Rn_2')
        for _ in range(10):
            rn_1.run()
            rn_2.walk()
        self.assertNotEqual(rn_1.distance, rn_2.distance)


if __name__ == '__main__':
    unittest.main()
      