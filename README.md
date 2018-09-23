## tb

make tables in terminal

### Usage

examples
```
t = Table()
t.header = ['First', 'Last']
t.rows.append(['Julian', 'Jasablancas'])
t.rows.append(['Someone', 'Else'])
t.render()

# or with init
t = Table(
	['First', 'Last'],
	[
		['Julian', 'Casablancas'],
		['Someone', 'Else'],
	]
)

```
will output

```
+---------+-------------+
| First   | Last        |
+---------+-------------+
| julian  | casablancas |
| someone | else        |
+---------+-------------+
```
