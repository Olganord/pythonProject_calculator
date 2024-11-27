import runners as rn
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.rn1 = rn.Runner("Усейн", 10)
        self.rn2 = rn.Runner("Андрей", 9)
        self.rn3 = rn.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, v in enumerate(cls.all_results):
            print(v)

    def test_run_1(self):
        t1 = rn.Tournament(90, self.rn1, self.rn3)
        t1_result = {k: str(v) for k, v in t1.start().items()}
        TournamentTest.all_results.append(t1_result)
        self.assertTrue(t1_result[2], 'Ник')

    def test_run_2(self):
        t2 = rn.Tournament(90, self.rn2, self.rn3)
        t2_result = {k: str(v) for k, v in t2.start().items()}
        TournamentTest.all_results.append(t2_result)
        self.assertTrue(t2_result[2], 'Ник')

    def test_run_3(self):
        t3 = rn.Tournament(90, self.rn1, self.rn2, self.rn3)
        t3_result = {k: str(v) for k, v in t3.start().items()}
        TournamentTest.all_results.append(t3_result)
        self.assertTrue(t3_result[3], 'Ник')


if __name__ == "__main__":
    unittest.main()
