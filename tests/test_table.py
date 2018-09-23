import sys
from os.path import dirname, realpath
sys.path.append(dirname(dirname(realpath(__file__))))
import unittest
from tb import Table


def test_table():
	t = Table()
	t.header = ['First', 'Last']
	t.rows.append(['julian', 'casablancas'])
	t.rows.append(['someone', 'else'])
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
	t.header = ['First']
	t.rows.append(['julian'])
	t.rows.append(['someone'])
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
	t.header = ['First', 'Last', 'Hobby']
	t.rows.append(['Julian', 'Casablancas', 'Music'])
	t.rows.append(['Timmy', 'Turner', 'Magic'])
	t.rows.append(['Marty', 'McFly', 'Music'])
	t.rows.append(['Emmett', 'Brown', 'Science'])
	t.rows.append(['someone', 'else', 'something'])
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
	t.header = ['First', 'Last']
	t.rows.append(['julian', 'casablancas'])
	t.rows.append(['someone', 'else'])
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
	t.header = ['First']
	t.rows.append(['julian', 'casablancas'])
	t.rows.append(['someone', 'else'])
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
	t.header = []
	t.rows.append(['julian', 'casablancas'])
	t.rows.append(['someone', 'else'])
	assert str(t) == """
+---------+-------------+
| julian  | casablancas |
| someone | else        |
+---------+-------------+
"""
