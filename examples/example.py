import sys
from os.path import dirname, realpath
sys.path.append(dirname(dirname(realpath(__file__))))
from tb import Table

t = Table()
t.set_header(['First', 'Last'])
t.add_row(['julian', 'casablancas'])
t.add_row(['someone', 'else'])
t.render()

t = Table()
t.set_header(['first', 'last'])
t.rows.append(['ethan', 'kath'])
t.rows.append(['alice', 'glass'])
print(t)

t = Table(
	['first', 'last', 'more'],
	[
		['first', 'second', 'more'],
		['third', 'fourth', 'more'],
	]
)
t.render()
