import sys
from os.path import dirname, realpath
sys.path.append(dirname(dirname(realpath(__file__))))
from tb import Table

t = Table()
t.header = ['First', 'Last']
t.rows.append(['Julian', 'Jasablancas'])
t.rows.append(['Someone', 'Else'])
t.render()

t = Table()
t.header = ['First', 'Last']
t.rows.append(['Ethan', 'Kath'])
print(t)

t = Table(
	['First', 'Last', 'More'],
	[
		['first', 'second', 'more'],
		['third', 'fourth', 'more'],
	]
)
t.render()
