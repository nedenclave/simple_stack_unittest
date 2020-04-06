# -*- coding: utf-8 -*-
# Author: Ned

import unittest
from Stack import Stack

class Test(unittest.TestCase):
  def test_push(self):
    stack = Stack()
    stack.push("Bao")
    stack.push("Ned")
    self.assertEqual(stack.get_stack(), ["Bao", "Ned"])

  def test_isEmpty(self):
    stack = Stack()
    self.assertTrue(stack.isEmpty())
    stack.push("Ned")
    self.assertFalse(stack.isEmpty())

  def test_pop(self):
    stack = Stack()
    self.assertEqual(stack.pop(), None)
    stack.push("Bao")
    stack.push("Ned")
    self.assertEqual(stack.pop(), "Ned")
    self.assertEqual(stack.get_stack(), ["Bao"])

  def test_contains(self):
    stack = Stack()
    stack.push("Ned")
    self.assertFalse(stack.contains("Bao"))
    self.assertTrue(stack.contains("Ned"))
  
  def test_clear(self):
    stack = Stack()
    stack.push("Ned")
    stack.clear()
    self.assertEqual(stack.get_stack(), [])

  def test_peek(self):
    stack = Stack()
    self.assertEqual(stack.peek(), None)
    stack.push("Bao")
    stack.push("Ned")
    self.assertEqual(stack.peek(), "Ned")

if __name__ == '__main__':
  # begin the unittest.main()
  unittest.main()