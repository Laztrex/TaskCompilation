import unittest
from unittest.mock import Mock
from termcolor import cprint
from collections import defaultdict
from caesar_encryptor import CaesarEncrypt
from vijener_encryptor import VijenerEnc


class GlobalCaesarTest(unittest.TestCase):
    VALUES_FOR_TEST_NORMAL = [('скиллбокс', 3, 'encode', 'ru'), ('привет', 5, 'encode', 'ru'),
                              ('а с русским текстом выйдет?', 1, 'encode', 'ru')]
    VALUES_FOR_TEST_UPPER = [('СКИЛЛБОКС', 3, 'encode', 'ru'), ('ПРИВЕТ', 5, 'encode', 'ru'),
                             ('А С РУССКИМ ТЕКСТОМ ВЫЙДЕТ?', 1, 'encode', 'ru'), ('AVE CAESAR', 3, 'encode', 'en'),
                             ('ПРАКТИКУМ ПО МАТЕМАТИКЕ И ПАЙТОН', 22, 'encode', 'ru'), ('HIDEO KOJIMA', 12, 'encode', 'en')]
    VALUES_FOR_TEST_UPPER_LOWER = [('СКиЛлБоКс', 3, 'encode', 'ru'), ('ПривЕТ', 5, 'encode', 'ru'),
                                   ('А с РУсСКим тЕкСТОм ВыЙдЕт?', 1, 'encode', 'ru'), ('Ave CAeSaR', 3, 'encode', 'en'),
                             ('ПРАКтикУМ по МАтемаТИКЕ И ПАйТоН', 22, 'encode', 'ru'), ('HIdeO KOjiMA', 12, 'encode', 'en')]
    VALUES_FOR_TEST_MIX = [('Английский Do you speak it?', 9, 'encode'), ('50 центов is rapper', 14, 'encode'),
                           ('Рунглиш, русслиш, руглиш, или русинглиш (англ. Runglish, Russlish, Ruglish, Rusinglish) '
                            '— это смесь русского и английского...', 5, 'encode')]

    def setUp(self):
        self.caesar_test = defaultdict(lambda: [])
        for num, name_test in enumerate([self.VALUES_FOR_TEST_NORMAL,
                                         self.VALUES_FOR_TEST_UPPER,
                                         self.VALUES_FOR_TEST_UPPER_LOWER,
                                         self.VALUES_FOR_TEST_MIX]):
            self.caesar_test[num] = [CaesarEncrypt(*data) for data in name_test]
        cprint(f'Вызван {self.shortDescription()}', flush=True, color='cyan')

    def tearDown(self):
        cprint(f'Результаты будут прологированы, но потом :)')

    def test_normal(self):
        """Тест при нормальных условиях"""
        results = ['фнлоодснф', 'фхнжйч', 'бтсфттлйнуёлтупнгькеёу']

        for num, data in enumerate(self.caesar_test[0]):
            caesar_test = data.run()
            self.assertEqual(caesar_test, results[num])

    def test_upper(self):
        """Тест при верхнем регистре user_word"""
        results = ['фнлоодснф', 'фхнжйч', 'бтсфттлйнуёлтупнгькеёу', 'dyhfdhvdu',
                   'еёхазюаиведвхзъвхзюаъюехяздг', 'tupqawavuym']

        for num, data in enumerate(self.caesar_test[1]):
            caesar_test = data.run()
            self.assertEqual(caesar_test, results[num])

    def test_upper_lower(self):
        """Тест при смешанном регистре user_word"""
        results = ['фнлоодснф', 'фхнжйч', 'бтсфттлйнуёлтупнгькеёу', 'dyhfdhvdu',
                   'еёхазюаиведвхзъвхзюаъюехяздг', 'tupqawavuym']

        for num, data in enumerate(self.caesar_test[2]):
            caesar_test = data.run()
            self.assertEqual(caesar_test, results[num])

    def test_mix(self):
        """Тест при смешанном алфавите"""
        results = ['ицлфстъустmxhxdbynjtrc', '50дтыаьпwgfoddsf',
                   'хштзрнэхшццрнэхшзрнэнрнхшцнтзрнэетзрwzslqnxmwzxxqnxmwzlqnxmwzxnslqnxmвчуцсйцбхшццпузунетзрноцпузу']

        for num, data in enumerate(self.caesar_test[3]):
            caesar_test = data.run()
            self.assertEqual(caesar_test, results[num])


class GlobalVijenerTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
