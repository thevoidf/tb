import sys
from os.path import dirname, realpath
sys.path.append(dirname(dirname(realpath(__file__))))
import unittest
from tb import Item


def test_item():
	i = Item('item', 2, '|')
	assert str(i) == '| item '

	i = Item('col', 2, '!')
	assert str(i) == '! col '

