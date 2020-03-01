import unittest
import task
import random
import math
from datetime import datetime
import radar


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

    def test4(self):
        num = random.randint(2, 25)
        list = []
        for i in range(0, num-1):
            var = random.randint(0, 100)
            list.append(var)
        oracle = [list[0], list[num-2]]
        listCheck = task.listFunc(list)
        self.assertEqual(oracle, listCheck)

    def test5(self):
        d1 = radar.random_datetime()
        d2 = radar.random_datetime()
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        oracle = ((d2 - d1).days)
        diffCheck = task.duration(d1, d2)
        self.assertEqual(oracle, diffCheck)


if __name__ == '__main__':
    unittest.main()
