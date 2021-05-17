from unittest import TestCase

from hash import Hash


class Hashtest(TestCase):
    def setUp(self):
        self.Hash = Hash()

    def test_getitem(self):
        m = {'Вода': 457,
             'Сок': 876,
             'Кола': 826,
             'Апероль': 235,
             'Смузи': 174}
        for k, v in m.items():
            self.Hash.__setitem__(k, v)
        self.assertEqual(291, self.Hash.__getitem__('Манго'))