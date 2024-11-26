import runners as rn
import unittest

"""Создается класс TournamentTest, наследующий от класса unittest.TestCase. 
Этот класс будет содержать тесты для проверки работы турнира. """


class TournamentTest(unittest.TestCase):


    """Метод setUpClass вызывается перед запуском всех тестов в классе.
    Он создает пустой список all_results, который будет использоваться для хранения результатов каждого теста."""
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    """Метод setUp выполняется перед каждым тестовым методом. 
    В нем создаются три объекта типа Runner с различными именами и скоростями."""
    def setUp(self):
        self.rn1 = rn.Runner("Усейн", 10)
        self.rn2 = rn.Runner("Андрей", 9)
        self.rn3 = rn.Runner("Ник", 3)

    """Метод tearDownClass вызывается после выполнения всех тестов в классе. 
    Он выводит результаты всех тестов, которые были сохранены в списке all_results."""
    @classmethod
    def tearDownClass(cls):
        for i, v in enumerate(cls.all_results):  # С помощью функции enumerate() каждому элементу списка присваивается
            # индекс. Полученный итерируемый объект можно преобразовывать в словарь и обрабатывать в цикле.
            print(v)

    """Тестовый метод test_run_1 создает объект Tournament с двумя участниками (self.rn1 и self.rn3), 
    запускает турнир и сохраняет результат в виде словаря. Затем проверяется, что участник "Ник" занял второе место."""
    def test_run_1(self):
        t1 = rn.Tournament(90, self.rn1, self.rn3)
        t1_result = {k: str(v) for k, v in t1.start().items()}
        TournamentTest.all_results.append(t1_result)
        self.assertTrue(t1_result[2], 'Ник')

    """Аналогично предыдущему тестовому методу, но с другими участниками (self.rn2 и self.rn3)."""
    def test_run_2(self):
        t2 = rn.Tournament(90, self.rn2, self.rn3)
        t2_result = {k: str(v) for k, v in t2.start().items()}
        TournamentTest.all_results.append(t2_result)
        self.assertTrue(t2_result[2], 'Ник')

    """Тестовый метод test_run_3 создает объект Tournament с тремя участниками (self.rn1, self.rn2 и self.rn3), 
    запускает турнир и проверяет, что участник "Ник" занял третье место."""
    def test_run_3(self):
        t3 = rn.Tournament(90, self.rn1, self.rn2, self.rn3)
        t3_result = {k: str(v) for k, v in t3.start().items()}
        TournamentTest.all_results.append(t3_result)
        self.assertTrue(t3_result[3], 'Ник')


"""Если файл запущен как основной скрипт, то вызывается функция unittest.main(), 
которая ищет и выполняет все тесты, определенные в классе."""
if __name__ == "__main__":
    unittest.main()
