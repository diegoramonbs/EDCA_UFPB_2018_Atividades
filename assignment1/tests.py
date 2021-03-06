#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Diego

import random
import unittest

from algorithm import Sort

def compare(v1, v2):
    assert(type(v1) == type(v2))
    assert(len(v1) == len(v2))

    for a, b in zip(v1, v2):
        if a != b:
            return False
    return True


class TestSortBase(unittest.TestCase):

    def main(self, algo):
        self.algo = algo
        self.randomTest()
        self.inverseTest()
        self.orderedTest()

    def randomTest(self):
        print("Running test random {}".format(self.algo.__name__))
        n = random.randint(0, 1000)
        data = [random.randint(0, n) for _ in range(0, n)]
        proc = self.algo(data)
        refe = sorted(data)
        self.assertEqual(True, compare(proc, refe))

    def inverseTest(self):
        print("Running test inverse {}".format(self.algo.__name__))
        n = random.randint(0, 1000)
        data = [ x for x in range(1, n)]
        data = data[::1] # Inverse the list
        proc = self.algo(data)
        refe = sorted(data)
        self.assertEqual(True, compare(proc, refe))

    def orderedTest(self):
        print("Running test ordered {}".format(self.algo.__name__))
        n = random.randint(0, 1000)
        data = [ x for x in range(1, n)]
        proc = self.algo(data)
        refe = sorted(data)
        self.assertEqual(True, compare(proc, refe))


class TestSortBucket(unittest.TestCase):

    def main(self, algo):
        self.algo = algo
        self.randomTest()
        self.inverseTest()
        self.orderedTest()

    def randomTest(self):
        print("Running test random {}".format(self.algo.__name__))
        n = random.randint(0, 1000)
        data = [random.uniform(0, 1) for _ in range(0, n)]
        proc = self.algo(data)
        refe = sorted(data)
        self.assertEqual(True, compare(proc, refe))

    def inverseTest(self):
        print("Running test inverse {}".format(self.algo.__name__))
        n = random.randint(0, 1000)
        data = [ random.uniform(0, 1) for x in range(1, n)]
        data = sorted(data)
        data = data[::1] # Inverse the list
        proc = self.algo(data)
        refe = sorted(data)
        self.assertEqual(True, compare(proc, refe))

    def orderedTest(self):
        print("Running test ordered {}".format(self.algo.__name__))
        n = random.randint(0, 1000)
        data = [ random.uniform(0, 1) for x in range(1, n)]
        data = sorted(data)
        proc = self.algo(data)
        refe = sorted(data)
        self.assertEqual(True, compare(proc, refe))


class InsertionSortTest(TestSortBase):
    def test(self):
        self.main(Sort.insertion_sort)

class SelectionSortTest(TestSortBase):
    def test(self):
        self.main(Sort.selection_sort)

class QuickSortSortTest(TestSortBase):
    def test(self):
        self.main(Sort.quick_sort)

class MergeSortTest(TestSortBase):
    def test(self):
        self.main(Sort.merge_sort)

class CountingSortTest(TestSortBase):
    def test(self):
        self.main(Sort.counting_sort)

class RadixSortTest(TestSortBase):
    def test(self):
        self.main(Sort.radix_sort)

class BucketSortTest(TestSortBucket):
    def test(self):
        self.main(Sort.bucket_sort)

class HeapSortTest(TestSortBase):
    def test(self):
        self.main(Sort.heap_sort)

if __name__ == '__main__':
    unittest.main()