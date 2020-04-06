# -*- coding: utf-8 -*-
# Author: Ned

from IStack import IStack
from interface import implements

class Stack(implements(IStack)):
  def __init__(self):
    self.stack = []

  def get_stack(self):
    return self.stack

  def clear(self):
    self.stack = []

  def contains(self, item):
    return item in self.stack

  def isEmpty(self):
    return self.stack == []

  def peek(self):
    if self.isEmpty():
      return None
    else:
      return self.stack[-1]

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    if self.isEmpty():
      return None
    else:
      return self.stack.pop()


