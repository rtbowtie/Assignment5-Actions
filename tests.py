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

    def test4(self):
        num = random.radnint(2, 25)
        list = []
        for i in (num-1):
            var = random.randint(0, 100)
            list.append(var)
        oracle = [list[0], list[num-2]]
        listCheck = task.listFun(list)
        self.assertEqual(oracle, listCheck)


if __name__ == '__main__':
    unittest.main()
