# -*- coding: utf-8 -*-
# Author: Ned

from interface import Interface

class IStack(Interface):
  def __init__(self):
    pass
  def get_stack(self):
    pass
  def clear(self):
    pass
  def contains(self, item):
    pass
  def isEmpty(self):
    pass
  def peek(self):
    pass
  def push(self, item):
    pass
  def pop(self):
    pass