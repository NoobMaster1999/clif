# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for clif.pybind11.staging.number_methods.

This file is a subset of clif/testing/python/number_methods_test.py.
"""

import unittest
from clif.pybind11.staging import number_methods


class NumberMethodsTest(unittest.TestCase):

  def testAdd(self):
    n1 = number_methods.Number(1.0)
    n2 = number_methods.Number(2.0)
    n3 = n1 + n2
    self.assertEqual(n3.value, 3.0)

  def testSubtract(self):
    n1 = number_methods.Number(2.0)
    n2 = number_methods.Number(1.0)
    n3 = n1 - n2
    self.assertEqual(n3.value, 1.0)

  def testMultiply(self):
    n1 = number_methods.Number(2.0)
    n2 = number_methods.Number(3.0)
    n3 = n1 * n2
    self.assertEqual(n3.value, 6.0)

  def testMod(self):
    n1 = number_methods.Number(7.0)
    n2 = number_methods.Number(3.0)
    n3 = n1 % n2
    self.assertEqual(n3.value, 1.0)

  def testInvert(self):
    n = number_methods.Number(5.0)  # 5(0b0101)
    self.assertEqual((~n).value, -6)  # -6(0b1010)

  def testLshift(self):
    n = number_methods.Number(5.0)  # 5(0b0101)
    self.assertEqual((n << 1).value, 10)  # 10(0b1010)

  def testRshift(self):
    n = number_methods.Number(5.0)  # 5(0b0101)
    self.assertEqual((n >> 1).value, 2)  # 2(0b0010)

  def testAnd(self):
    n1 = number_methods.Number(5.0)  # 5(0b0101)
    n2 = number_methods.Number(6.0)  # 6(0b0110)
    self.assertEqual((n1 & n2).value, 4)  # 2(0b0100)

  def testXor(self):
    n1 = number_methods.Number(5.0)  # 5(0b0101)
    n2 = number_methods.Number(6.0)  # 6(0b0110)
    self.assertEqual((n1 ^ n2).value, 3)  # 2(0b0011)

  def testOr(self):
    n1 = number_methods.Number(5.0)  # 5(0b0101)
    n2 = number_methods.Number(6.0)  # 6(0b0110)
    self.assertEqual((n1 | n2).value, 7)  # 2(0b0111)

  def testInt(self):
    n1 = number_methods.Number(6.0)
    self.assertEqual(int(n1), 6)

  def testFloat(self):
    n1 = number_methods.Number(6)
    self.assertEqual(float(n1), 6.0)

  def testInplaceAdd(self):
    n1 = number_methods.Number(1.0)
    n2 = number_methods.Number(2.0)
    n1 += n2
    self.assertEqual(n1.value, 3.0)

  def testInplaceSubtract(self):
    n1 = number_methods.Number(2.0)
    n2 = number_methods.Number(1.0)
    n1 -= n2
    self.assertEqual(n1.value, 1.0)

  def testInplaceMultiply(self):
    n1 = number_methods.Number(2.0)
    n2 = number_methods.Number(3.0)
    n1 *= n2
    self.assertEqual(n1.value, 6.0)

  def testInplaceMod(self):
    n1 = number_methods.Number(7.0)
    n2 = number_methods.Number(3.0)
    n1 %= n2
    self.assertEqual(n1.value, 1.0)

  def testTrueDivide(self):
    n1 = number_methods.Number(6.0)
    n2 = number_methods.Number(3.0)
    n3 = n1 / n2
    self.assertEqual(n3.value, 2.0)

  def testInplaceTrueDivede(self):
    n1 = number_methods.Number(6.0)
    n2 = number_methods.Number(3.0)
    n1 /= n2
    self.assertEqual(n1.value, 2.0)

  def testInplaceLshift(self):
    n = number_methods.Number(5.0)  # 5(0b0101)
    n <<= 1
    self.assertEqual(n.value, 10)  # 10(0b1010)

  def testInplaceRshift(self):
    n = number_methods.Number(5.0)  # 5(0b0101)
    n >>= 1
    self.assertEqual(n.value, 2)  # 2(0b0010)

  def testInplaceAnd(self):
    n1 = number_methods.Number(5.0)  # 5(0b0101)
    n2 = number_methods.Number(6.0)  # 6(0b0110)
    n1 &= n2
    self.assertEqual(n1.value, 4)  # 2(0b0100)

  def testInplaceXor(self):
    n1 = number_methods.Number(5.0)  # 5(0b0101)
    n2 = number_methods.Number(6.0)  # 6(0b0110)
    n1 ^= n2
    self.assertEqual(n1.value, 3)  # 2(0b0011)

  def testInplaceOr(self):
    n1 = number_methods.Number(5.0)  # 5(0b0101)
    n2 = number_methods.Number(6.0)  # 6(0b0110)
    n1 |= n2
    self.assertEqual(n1.value, 7)  # 2(0b0111)


if __name__ == '__main__':
  unittest.main()
