import unittest
import task
import random
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        randNum = random.random()
        oracle = (math.pi)*((randNum)*randNum)
        pred = task.area(randNum)
        self.assertEqual(oracle, pred)


if __name__ == '__main__':
    unittest.main()
