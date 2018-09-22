import sys
from os.path import dirname, realpath
sys.path.append(dirname(dirname(realpath(__file__))))
import unittest
from tb import Table


def test_table():
	t = Table()
	t.set_header(['First', 'Last'])
	t.add_row(['julian', 'casablancas'])
	t.add_row(['someone', 'else'])
	assert str(t) == """
+---------+-------------+
| First   | Last        |
+---------+-------------+
| julian  | casablancas |
| someone | else        |
+---------+-------------+
"""


def test_table_with_single_column():
	t = Table()
	t.set_header(['First'])
	t.add_row(['julian'])
	t.add_row(['someone'])
	assert str(t) == """
+---------+
| First   |
+---------+
| julian  |
| someone |
+---------+
"""


def test_table_with_many_columns():
	t = Table()
	t.set_header(['First', 'Last', 'Hobby'])
	t.add_row(['Julian', 'Casablancas', 'Music'])
	t.add_row(['Timmy', 'Turner', 'Magic'])
	t.add_row(['Marty', 'McFly', 'Music'])
	t.add_row(['Emmett', 'Brown', 'Science'])
	t.add_row(['someone', 'else', 'something'])
	assert str(t) == """
+---------+-------------+-----------+
| First   | Last        | Hobby     |
+---------+-------------+-----------+
| Julian  | Casablancas | Music     |
| Timmy   | Turner      | Magic     |
| Marty   | McFly       | Music     |
| Emmett  | Brown       | Science   |
| someone | else        | something |
+---------+-------------+-----------+
"""


def test_table_with_custom_symbols():
	t = Table()
	t.sep_char = '='
	t.column_char = '|'
	t.corner_char = '*'
	t.set_header(['First', 'Last'])
	t.add_row(['julian', 'casablancas'])
	t.add_row(['someone', 'else'])
	assert str(t) == """
*=========*=============*
| First   | Last        |
*=========*=============*
| julian  | casablancas |
| someone | else        |
*=========*=============*
"""


def test_table_with_missing_header():
	t = Table()
	t.set_header(['First'])
	t.add_row(['julian', 'casablancas'])
	t.add_row(['someone', 'else'])
	assert str(t) == """
+---------+-------------+
| First   |             |
+---------+-------------+
| julian  | casablancas |
| someone | else        |
+---------+-------------+
"""


def test_table_with_without_header():
	t = Table()
	t.set_header([])
	t.add_row(['julian', 'casablancas'])
	t.add_row(['someone', 'else'])
	assert str(t) == """
+---------+-------------+
| julian  | casablancas |
| someone | else        |
+---------+-------------+
"""

