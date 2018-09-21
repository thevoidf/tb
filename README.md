## tb

make tables in terminal

### Usage

examples
```
t = Table()
t.set_header(['First', 'Last'])
t.add_row(['julian', 'casablancas'])
t.add_row(['someone', 'else'])
t.render()

# or with init
t = Table(
	['First', 'Last'],
	[
		['julian', 'casablancas'],
		['someone', 'else'],
	]
)

```
will output

```
+--------+-------------+
| First  | Last        |
+--------+-------------+
| julan  | casablancas |
| tobias | forge       |
+--------+-------------+
```
