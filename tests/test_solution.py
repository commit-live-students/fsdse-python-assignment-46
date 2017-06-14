from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        from collections import Counter

        fpath = './files/testfile.txt'
        res = solution(fpath)

        self.assertEqual(res['Python'], 3)
        self.assertEqual(res['and'], 6)
        self.assertIsInstance(res, Counter)
